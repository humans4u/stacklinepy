import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='stackline',
    version='0.0.1.dev1',
    license='GPL-3.0',
    python_requires='>=3.10.9',
    description='Simple pipeline management implemented in python.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=['stackline'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    project_urls={
        'Source': 'https://github.com/humans4u/stacklinepy/'
    }
)