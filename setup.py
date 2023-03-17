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
        'PyYAML'
    ],
    packages=['tt_utils']
)
