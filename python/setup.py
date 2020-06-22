from setuptools import setup, find_packages


setup(
    name='zero-to-ai',
    version='0.0.0',
    description='Zero To AI project',
    author='James Cranston',
    author_email='jcranston92@gmail.com',
    classifiers=['Development Status :: 1 - Development',
                 'Intended Audience :: Students and Tech Professionals',
                 'Topic :: Educational Material :: Source Code',
                 'Programming Language :: Python :: 3.7'],
    packages=find_packages(exclude=('tests', 'tests.*')),
    namespace_packages=['zero2ai', 'test'],
    zip_safe=False,
    package_data={'': ['*.csv', '*.csv.gz', '*.tiny3']}
)
