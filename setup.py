import os
from distutils.core import setup
from setuptools import find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name='mezzanine-dpaste',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='A Mezzanine app to integrate dpaste, a Django pastebin.',
    long_description=README,
    url='http://github.com/prikhi/mezzanine-paste',
    author='Pavan Rikhi',
    author_email='pavan@sleepanarchy.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=['dpaste', 'mezzanine'],
)
