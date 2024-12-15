from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Motorcycle maintenance tracker'

# Reading the long description from README.md
try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        LONG_DESCRIPTION = fh.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION  # Fallback if README.md is missing

# Setup parameters
setup(
    name='MotoMinder',
    version=VERSION,
    author="Jordan Kelley",
    author_email="jordan.d.kelley1@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',  # Specify content type if using Markdown
    packages=find_packages(),
    install_requires=[
        'kivy>=2.0.0',  # Ensures you get a compatible version of Kivy
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify minimum Python version
)
