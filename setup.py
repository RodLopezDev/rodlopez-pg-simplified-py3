from setuptools import setup

setup(
    name='simplepgconnection',
    version='0.0.1',
    description='A simple utility to simplified connection to postgresql on python',
    author='RodLopez',
    license='MIT',
    keywords='postgres pg connection sqlalchemy',
    author_email='rodrigolopezdev@gmail.com',
    packages=['lib'],
    install_requires=[
        'SQLAlchemy==1.4.28',
        'pandas>=1.5.0'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RodLopezDev/rodlopez-pg-simplified-py3',
)
