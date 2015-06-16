from setuptools import setup, find_packages

setup(
    name='redis_wrapped_mkstemp',
    version='1.0.0',
    description="redis_wrapped_mkstemp is a utility for generating unique-named files using Redis.",
    url='https://github.com/rikonor/redis_wrapped_mkstemp',
    py_modules=["redis_wrapped_mkstemp"],
    author='Or Rikon',
    author_email='rikonor@gmail.com',
    license='MIT',
    keywords='redis'
)