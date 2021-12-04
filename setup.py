from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="chittariraghu",
    description=" ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chittariraghu/ann_implementation_03oct21",
    author_email="chittariraghu@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"
    ]
)