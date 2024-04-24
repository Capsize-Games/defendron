from setuptools import setup, find_packages

setup(
    name="defendron",
    version="0.1.0",
    author="Capsize LLC",
    description="",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="",
    license="GPL-3.0",
    author_email="contact@capsizegames.com",
    url="https://github.com/Capsize-Games/defendron",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10.0",
    install_requires=[
    ],
    dependency_links=[
        "nullscream==0.1.0",
        "lockdown==0.1.0",
        "shadowlogger==0.1.0",
    ],
)