from setuptools import setup, find_packages

setup(
    name="bookstack-api",
    packages=find_packages(),
    version="0.1.0",
    description="A Python client for the BookStack API",
    author="Robin Niemann, Stina Niemann",
    author_email="robin@rn-software-services.de",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords=["bookstack", "api", "client"],
)
