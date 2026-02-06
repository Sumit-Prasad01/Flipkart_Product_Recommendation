from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from config.config import Config
from utils.custom_exception import CustomException
from utils.logger import get_logger


logger = get_logger(__name__)


class RAGChainBuilder:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.model = ChatGroq(model=Config.RAG_MODEL, temperature=0.5)
        self.history_store = {}

    def _get_history(self, session_id: str) -> BaseChatMessageHistory:
        try:
            if session_id not in self.history_store:
                self.history_store[session_id] = ChatMessageHistory()
            return self.history_store[session_id]

        except Exception as e:
            logger.error(f"Error while retrieving session history: {e}")
            raise CustomException("Failed to retrieve session history.", e)

    def build_chain(self):
        try:
            retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

        
            rewrite_prompt = ChatPromptTemplate.from_messages([
                ("system", "Given the chat history and user question, rewrite it as a standalone question."),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}")
            ])

            
            qa_prompt = ChatPromptTemplate.from_messages([
                ("system", """You're an e-commerce bot answering product-related queries using reviews and titles.
            Only use the given context. If you don't know, say you don't know.

            CONTEXT:
            {context}
            """),

                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}")
            ])

            rewrite_chain = rewrite_prompt | self.model | StrOutputParser()
            
            retrieve_docs = RunnableLambda(lambda question: retriever.invoke(question))
           
            answer_chain = qa_prompt | self.model | StrOutputParser()
           
            rag_chain = (
                RunnableLambda(lambda x: {
                    "standalone_question": rewrite_chain.invoke(x),
                    "input": x["input"],
                    "chat_history": x["chat_history"]
                })
                | RunnableLambda(lambda x: {
                    "context": retrieve_docs.invoke(x["standalone_question"]),
                    "input": x["input"],
                    "chat_history": x["chat_history"]
                })
                | answer_chain
            )

            return RunnableWithMessageHistory(
                rag_chain,
                self._get_history,
                input_messages_key="input",
                history_messages_key="chat_history",
            )

        except Exception as e:
            logger.error(f"Error while building chain: {e}")
            raise CustomException("Failed to build chain.", e)
