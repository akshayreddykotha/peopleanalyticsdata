import setuptools

setuptools.setup(
    name="peopleanalyticsdata",
    version="0.1.5",
    url="https://github.com/akshayreddykotha/peopleanalyticsdata",
    author="Akshay Kotha",
    author_email="akotha@ucsd.edu",
    description="Allows data access from the book - Handbook of Regression Modeling in People Analytics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)