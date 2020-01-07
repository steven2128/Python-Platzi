from setuptools import setup


setup(
    name='Platzi Clean',
    version='1.0',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)

