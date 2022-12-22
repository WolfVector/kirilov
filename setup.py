import setuptools

setuptools.setup(
    name='kirilov',
    version='0.1.0',
    author='Alejandro Torres Hernandez',
    author_email='alejandro.torres9622@gmail.com',
    description='A python package to list and download new installed requirements',
    license='MIT',
    packages=['kirilov'],

    entry_points ={
        'console_scripts': [
            'kirilov = kirilov.cmpreq:main'
        ]
    }
)