import setuptools

setuptools.setup(
    name="peopleanalyticspython",
    version="0.1.0",
    url="https://github.com/akshayreddykotha/peopleanalyticspython",
    author="Akshay Kotha",
    author_email="kakr2795@gmail.com",
    description="Allows data access from Keith McNulty's R package on people analytics data sets",
    long_description=open('DESCRIPTION.rst').read(),
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