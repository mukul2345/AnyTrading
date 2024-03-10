from setuptools import setup, find_packages

setup(
    name='Anytrading',
    version='2.0.0',
    packages=find_packages(),

    author='mukul2345',
    author_email='mukul798348@gmail.com',
    license='MIT',

    install_requires=[
        'gymnasium>=0.29.1',
        'numpy>=1.16.4',
        'pandas>=0.24.2',
        'matplotlib>=3.1.1'
    ],

    package_data={
        'gym_anytrading': ['datasets/data/*']
    }
)
