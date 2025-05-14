from setuptools import setup, find_packages

setup(
    name='b64tool',
    version='1.0',
    author='Sebastian Peters',
    author_email='sebastian.peters@itsc.de',
    description='A tool for encoding and decoding text using Base64',
    py_modules=['b64tool'],
    install_requires=[],  # No external dependencies
    entry_points={
        'console_scripts': [
            'b64tool=b64tool:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)