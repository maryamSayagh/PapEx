from setuptools import setup, find_packages

setup(
    name="papex",
    version="0.1",
    description="A library for fetching and normalizing academic papers from various providers (Elsevier, arXiv, PRISM, etc.)",
    #long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Maryam SAYAGH"
    author_email="maryamsayagho@gmail.com",
    url="https://github.com/yourusername/paper_lib",
    packages=find_packages(),
    install_requires=( "requests>=2.25.1",
        "orjson>=3.6.4",
        "lxml>=4.6.3",
        "arxiv>=1.4.8",
                       ),
    python_requires=">=3.7",
    classifiers=[
        #"Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
    ])
