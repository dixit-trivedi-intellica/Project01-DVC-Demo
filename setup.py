from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="dixit",
    description="A small package for DVC demo",
    long_description=long_description,
    author_email="dixit@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/dixit-trivedi-intellica/Project01-DVC-Demo",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "dvc",
        "dvc[gdrive]",
        "dvc[s3]",
        "pandas",
        "scikit-learn"
    ]
)
    