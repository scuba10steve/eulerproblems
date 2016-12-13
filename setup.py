try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test',
    'author': 'Steven Tompkins',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'stompkins@shelterinsurance.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Test'],
    'scripts': [],
    'name': 'Test'
}

setup(**config)