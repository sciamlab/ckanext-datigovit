from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-datigovit',
    version=version,
    description="",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='sciamlab',
    author_email='info@sciamlab.com',
    url='www.sciamlab.com',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datigovit'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.datigovit.plugin:PluginClass
        datigovit = ckanext.datigovit.plugin:DatiGovItPlugin	
    ''',
)
