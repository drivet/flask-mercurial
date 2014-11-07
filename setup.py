"""
Flask-Mercurial
-------------

Flask extension to provide basic manipulation of mercurial repositories
"""
from setuptools import setup


setup(
    name='Flask-Mercurial',
    version='1.0',
    url='https://github.com/drivet/flask-mercurial/',
    license='MIT',
    author='Desmond Rivet',
    author_email='desmond.rivet@gmail.com',
    description='Flask extension to provide basic manipulation of mercurial repositories',
    long_description=__doc__,
    py_modules=['flask_mercurial'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
        'python-hglib'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
