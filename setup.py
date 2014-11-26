from setuptools import setup

setup(
    name='tt_utils',
    description='TipTap utils library.',
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    version=open('VERSION').read().strip(),
    author='TipTap',
    install_requires=[
        'colander>=1.0b1',
        'leveldb',
        'tornado>=3.2.2',
        'PyYAML'
    ],
    package_dir={'tt_utils': 'src'},
    packages=['tt_utils']
)
