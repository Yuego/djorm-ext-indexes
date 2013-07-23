#coding: utf-8
from __future__ import unicode_literals, absolute_import
from setuptools import setup, find_packages

description="""
Indexing support for Array and HStore fields
"""

setup(
    name="djorm-ext-indexes",
    version='0.1',
    url='https://github.com/Yuego/djorm-ext-indexes',
    license='MIT',
    platforms=['OS Independent'],
    description=description.strip(),
    author='Artem Vlasov',
    author_email = 'root@proscript.ru',
    maintainer = 'Artem Vlasov',
    maintainer_email = 'root@proscript.ru',
    packages = find_packages(),
    include_package_data = False,
    install_requires = [
        'djorm-ext-pgarray >= 0.4.0',
    ],
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ]
)

