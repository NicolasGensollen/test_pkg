import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toy_pkg",
    version="0.0.1",
    author="Nicolas Gensollen",
    author_email="nicolas.gensollen@gmail.com",
    description="A small and useless example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NicolasGensollen/toy_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
