# Overview

Project name: peopleanalytics-python

This package is port of an R package associated with the [free online](http://peopleanalytics-regression-book.org/) book _Handbook of Regression Modeling in People Analytics_ by Keith McNulty. Some additional information about the inspiration [here](https://towardsdatascience.com/beginner-friendly-data-science-projects-accepting-contributions-3b8e26f7e88e#14bf).

# Background

At peopleanalytics-regression-book.org, McNulty makes the data referenced in _Handbook of Regression Modeling in People Analytics_ available [via an R package](https://cran.r-project.org/package=peopleanalyticsdata). McNulty explains:

_For R and Python users, each of the data sets used in this book can be downloaded individually by following the code in each chapter. Alternatively for R users who intend to work through all of the chapters, all data sets can be loaded into an R session in advance by installing and loading the peopleanalyticsdata R package._

Once fully developed, this package will bring the functionality of McNulty's R package to Python users. As an initial idea, following a `pip install ...` will make these data sets accessible for Python users. These data sets can also be used as an alternative to the very common public data sets (iris, wine quality, etc) available on UCI repository to understand the concepts of exploratory data analysis and predictive modeling.

# Usage

```Python
# import peopleanalyticsdata package
import peopleanalyticdata as pad
import pandas as pd

# see a list of data sets
pad.list_sets()

# find out more about a specific data set ('managers' example)
# pad.help(managers)

# load data into a dataframe
df = pad.managers()
```
# Data dictionary

The data dictionary pertinent to all the data sets can be found [here](https://cran.r-project.org/web/packages/peopleanalyticsdata/peopleanalyticsdata.pdf).

# LICENSE

- NEEDS LICENSE INFORMATION - The original was MIT which I think requires derivatives to also be MIT.
