from setuptools import setup, find_packages

install_requires = [
    'lxml',
    'BeautifulSoup4',
    'bleach',
]

setup(
    name='TAGsieve',
    version='0.2.0',
    description='A small HTML/XML stripper GUI application.',
    long_description=open('README.rst').read(),
    author='Tom De Keyser',
    author_email = 'tomdekeyser7@gmail.com',
    license='GPLv3',
    url='http://github.com/willibrord/TAGsieve',
    packages=['TAGsieve'],
    package_data={'': ['README.rst']},
    install_requires=install_requires,
)