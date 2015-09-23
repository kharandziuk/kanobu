from setuptools import setup

setup(
    name='my_project',
    version='0.1.0',
    packages=['project'],
    install_requires=[
        'Django',
        'pathlib',
    ],
    entry_points={
        'console_scripts': [
            'my_package = project.wsgi:application'
        ]
    },
)
