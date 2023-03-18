from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='update_changelog',
    version='0.0.1',
    url='https://github.com/budavariam/update_changelog',
    author='Mátyás Budavári',
    author_email='budavariam@gmail.com',
    description='Simple tool for keepachangelog formatted markdown updates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    py_modules=['main'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'update_changelog=main:main'
        ]
    },
)