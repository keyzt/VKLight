from setuptools import setup


version = "1.1.1"
author = "Ivan"
description = "Light wrapper for VK's API"

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="VKLight",
    license="MIT",
    python_requires=">=3.6",
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keyzt/VKlight",
    packages=["VKLight"],
    install_requires=['requests'],
    scripts=[
        "VKlight/VKlight"
    ],
    project_urls={
        "Documentation": "https://github.com/keyzt/VKLight/blob/master/README.md",
        "Source": "https://github.com/keyzt/VKlight",
        "Tracker": "https://github.com/keyzt/VKLight/issues",
    },
)