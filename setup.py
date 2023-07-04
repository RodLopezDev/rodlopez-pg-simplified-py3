from setuptools import setup

setup(
    name='pg_simplified_py',
    version='0.1.0',
    description='A simple utility to simplified connection to postgresql on python',
    author='RodLopez',
    author_email='rodrigolopezdev@gmail.com',
    packages=['lib'],
    install_requires=[
        'numpy>=1.0.0',  # Example dependency
        'SQLAlchemy==1.4.28',
        'pandas>=1.5.0'
    ],
)
