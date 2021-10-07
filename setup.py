from setuptools import setup, version

setup(
    name = 'WayPy',
    version = '0.1.4',
    author = 'Guilherme Donizetti and Luiz Fernando Rodrigues',
    author_email = 'guilhermetecnologias@gmail.com',
    packages = ['waypy'],
    description = 'Package to find a path between two points in a graph.',
    long_description = 'By entering a list of nodes and edges, the package is able to try to find a path between any two points.<br>'
                     + 'The package contains different search methods that can get different results.',
    url = 'https://github.com/guilhermedonizetti/WayPy',
    project_urls = {
        'Source code': 'https://github.com/guilhermedonizetti/WayPy'
    },
    license = 'MIT',
    keywords = 'way graph',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent'
    ]
)