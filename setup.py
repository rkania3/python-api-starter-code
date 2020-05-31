import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-api-starter-code",
    version="0.0.1",
    author="Rahul Kanianchalil",
    author_email="rahul.kc1@gmail.com",
    description="Python API Sample Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkania3/python-api-starter-code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)