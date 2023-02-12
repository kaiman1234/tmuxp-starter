from setuptools import setup

setup(
    name='tmuxp-starter',
    version='0.3',
    packages=['tmuxp_starter'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        txp=tmuxp_starter.cli:main
    ''',
)
