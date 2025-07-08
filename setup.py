from setuptools import setup, find_packages

setup(
    name='novatask',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Database-agnostic CRUD + AI decision library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NeelBhadani/novatask',  # optional but recommended
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'tensorflow',
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
