from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Flipkart_Product_Recommendation",
    version="0.1",
    author="Sumit Prasad",
    packages=find_packages(),
    install_requires = requirements,
)