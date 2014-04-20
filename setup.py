import os
from distutils.core import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

PACKAGE_DATA = {'mezzpaste': ['mezzpaste/templates/*.*']}


setup(
    name='mezzanine-dpaste',
    version='0',
    packages=['mezzpaste'],
    package_data=PACKAGE_DATA,
    license='GPLv3',
    description='A Mezzanine app to integrate dpaste, a Django pastebin.',
    long_description=README,
    url='http://github.com/prikhi/mezzanine-paste',
    author='Pavan Rikhi',
    author_email='pavan@sleepanarchy.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    requires=['dpaste', 'mezzanine'],
)
