from setuptools import setup, find_packages

setup(
    name='dqchkr',  # Must be unique on PyPI
    version='0.1.0',
    author='Talha Sarfraz',
    author_email='talhasarfraz29@gmail.com',
    description='A Python package for automated data profiling, missing value detection, outlier identification, and imputation suggestions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/talha-11-11/dataqualitychecker',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas>=1.1',
        'matplotlib>=3.3',
        'seaborn>=0.11',
        'numpy>=1.19'
    ],
    project_urls={
        'Source': 'https://github.com/talha-11-11/dataqualitychecker',
        'Tracker': 'https://github.com/talha-11-11/dataqualitychecker/issues',
    },
    include_package_data=True,
)
