from setuptools import setup, find_packages

setup(
    name="pkg_tzs5dd",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.6",
    description="A package for processing text data",
    author="Ran Gao",
    author_email="tzs5dd@virginia.edum",
    url="https://github.com/rgao77/tzs5dd_DS5111su24_lab_01",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

