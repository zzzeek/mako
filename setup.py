
from sys import version_info as v
if any([v < (2, 6), (3,) < v < (3, 3)]):
    raise Exception("Unsupported Python version %d.%d. Requires Python >= 2.6 "
                    "or >= 3.3." % v[:2])

from setuptools import setup, find_packages
from os.path import abspath, dirname, join

here = abspath(dirname(__file__))

with open(join(here, 'mako', '__init__.py')) as fp:
    _locals = {}
    exec(fp.read(), None, _locals)
    __version__ = _locals['__version__']

with open(join(here, 'README.rst')) as r:
    readme = r.read()

optional_requirements = [
    'Beaker>=1.1', 
    'babel', 
    'lingua',
    'pygments',
]

optional_tests_require = ['nose >= 0.11'] + optional_requirements
tests_require = optional_tests_require[:]
if v < (3,):
    tests_require.append('mock')

setup(
    name='Mako',
    version=__version__,
    description="A super-fast templating language that borrows the \
 best ideas from the existing templating languages.",
    long_description=readme,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='templates',
    author='Mike Bayer',
    author_email='mike@zzzcomputing.com',
    url='http://www.makotemplates.org/',
    license='MIT',
    packages=find_packages('.', exclude=['examples*', 'test*']),
    tests_require=tests_require,
    test_suite="nose.collector",
    
    zip_safe=False,
    install_requires=[
        'MarkupSafe>=0.9.2'
    ],
    extras_require={
        ':python_version == "2.6"': [
            'argparse'
        ],
        'optional': optional_requirements,
        'test' : optional_tests_require,
        'test:python_version == "2.6" or python_version == "2.7"': [
            'mock'
        ],
    },
    entry_points="""
        [python.templating.engines]
        mako = mako.ext.turbogears:TGPlugin

        [pygments.lexers]
        mako = mako.ext.pygmentplugin:MakoLexer
        html+mako = mako.ext.pygmentplugin:MakoHtmlLexer
        xml+mako = mako.ext.pygmentplugin:MakoXmlLexer
        js+mako = mako.ext.pygmentplugin:MakoJavascriptLexer
        css+mako = mako.ext.pygmentplugin:MakoCssLexer

        [babel.extractors]
        mako = mako.ext.babelplugin:extract

        [lingua.extractors]
        mako = mako.ext.linguaplugin:LinguaMakoExtractor

        [console_scripts]
        mako-render = mako.cmd:cmdline
        """
)
