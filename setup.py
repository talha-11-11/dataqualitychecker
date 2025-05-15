from setuptools import setup, find_packages

setup(
    name='dataqualitychecker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
    ],
    author='Your Name',
    description='A tool to automatically check data quality in datasets.',
    url='https://github.com/yourusername/dataqualitychecker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
