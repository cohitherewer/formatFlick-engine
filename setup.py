from setuptools import setup, find_packages

setup(
    name="formatflick",
    version="0.0.2",
    author="Abhinaba Chakraborty",
    author_email="abhinabacr4@gmail.com",
    description="formatflick: change your file formats as you wish",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/cohitherewer/formatflick-engine",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["python", "file", "extension", "json", "xml", "csv", "pandas"],
    packages=find_packages(),
    install_requires=[
        "pandas>=2.1.4",
        "lxml>=5.1.0",
        "dask>=2024.1.0",
        "xmltodict",  # This dependency is missing in the original pyproject.toml
    ],
    python_requires=">=3.9",
)
