from codecs import open
from os.path import join, abspath, dirname
from setuptools import setup, find_packages
import os

requirementPath = 'requirements.txt'
install_requires = []

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

here = abspath(dirname(__file__))

# Get the long description from the README file
with open(join(here, 'README.md'), encoding='utf-8') as buff:
    long_description = buff.read()

setup(
    name="us_airline_sentiment_analysis",
    version="1.0",
    description="Sentiment Analysis Package",
    long_description=long_description,
    license='MIT',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=install_requires
)