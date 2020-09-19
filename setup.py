"""Package configuration."""
import setuptools

setuptools.setup(
    author="Jonathan Bowman",
    description="Python CSV handling demo",
    entry_points={"console_scripts": ["csvdemo=csvdemo:run"]},
    name="csvdemo",
    py_modules=["csvdemo"],
    version="0.1.0",
)
