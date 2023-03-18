from setuptools import setup

setup(
    name='update_changelog',
    version='0.0.1',
    py_modules=['update_changelog.src'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'update_changelog=update_changelog.src:main'
        ]
    }
)
