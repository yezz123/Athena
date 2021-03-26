import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="Athena",
    version="2.0",
    author="yezz123",
    author_email="yasserth19@protonmail.com",
    description="Athena is a web application developed in python / flask / SQLite that has two faces.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="Athena , Web Application , Python , SQLite , Flask",
    url="https://github.com/yezz123/Athena",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License (MIT)",
        "Topic :: Lab :: Web Application",
        "Operating System :: OS Independent"
    ),
)