from setuptools import setup
from mypyc.build import mypycify

setup(
    name="T1_cripto",
    version="0.1",
    packages=["."],
    ext_modules=mypycify([
        "main.py",
        "aes.py",
        "rlyeh.py",
    ]),
    entry_points={
        "console_scripts": [
            "T1_cripto = main:main",
        ],
    },
)