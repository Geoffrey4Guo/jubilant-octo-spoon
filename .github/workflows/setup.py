from setuptools import setup, find_packages

setup(
    name='My-Math-App',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'my-math-app = my_math_app.main:main'
        ]
    },
    author='Geoffrey Guo',
    author_email='geoffreyg35@gmail.com',
    description='a math application that can add, subtract, multiply, and divide',
    url='https://github.com/Geoffrey4Guo/jubilant-octo-spoon',
)
