from setuptools import setup

setup(
    name="zuping",
    version="1.0.0",
    py_modules=["zuping"],
    entry_points={
        "console_scripts": [
            "zuping=zuping:main",
        ],
    },
    author="zuvisck",
    description="A simple library for pinging hosts.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
