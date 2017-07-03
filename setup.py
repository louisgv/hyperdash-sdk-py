from setuptools import setup


version = "0.1.6"

setup(
    name='hyperdash',
    packages=['hyperdash', 'hyperdash_cli'],
    install_requires=[
        'autobahn',
        'Twisted',
        'pyOpenSSL',
        'six'
    ],
    entry_points={
        'console_scripts': ['hyperdash = hyperdash_cli.cli:main']
    },
    version=version,
    description='Hyperdash.io CLI and SDK',
    author='Hyperdash',
    author_email='support@hyperdash.io',
    url='https://hyperdash.io',
)