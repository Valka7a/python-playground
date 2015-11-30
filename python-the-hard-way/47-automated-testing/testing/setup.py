try:
	from setuptools import setup
except ImportErrors:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Valka7a',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'valentin.durvenqkov91@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)