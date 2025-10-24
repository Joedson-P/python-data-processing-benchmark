from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="datacleaner-benchmark",
    version="0.1.0",
    author="Joedson Pereira",
    description="Benchmark de métodos de processamento de dados em Python com classe DataCleaner otimizada",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.3.3",
        "numpy>=2.3.4",
        "matplotlib>=3.10.7",
    ],
)
