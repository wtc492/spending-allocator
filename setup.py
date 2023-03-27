from setuptools import find_packages
from setuptools import setup

setup(
    name='spending_allocator',
    version='1.0',
    description='track spending by category with useful calculation tools',
    author='Will Campbell',
    author_email='will.campbell.492@gmail.com',
    url='https://github.com/wtc/spending-allocator',
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'spending-allocator-cli = spending_allocator.main:main',
            'splc = spending_allocator.main:main',
        ],
    },
)
