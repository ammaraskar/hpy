from setuptools import setup, Extension

setup(
    name="hpy",
    ext_modules = [
        Extension('hpy', ['src/hpymodule.c'])
    ]
)