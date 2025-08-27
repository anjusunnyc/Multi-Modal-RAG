from setuptools import setup, find_packages
import os

os.makedirs("data/source_data/", exist_ok=True)

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="End-to-End Multi Modal RAG Application",
    version="0.1",
    author="name",
    email="email",
    packages=find_packages(),
    install_requires = requirements,
)