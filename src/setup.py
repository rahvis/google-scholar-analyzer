# setup.py

from setuptools import setup, find_packages

setup(
    name="author_ranking",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'dash',
        'plotly',
        'networkx',
        'pandas',  # If you need it for processing
    ],
    include_package_data=True,
    package_data={
        'author_ranking': ['authors.json'],  # Include the JSON file in the package
    },
    entry_points={
        'console_scripts': [
            'author-ranking=author_ranking.app:main',  # Make sure the app.py entry point is correct
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
