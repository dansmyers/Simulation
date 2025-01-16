# Brains

## Overview

We're going to practice basic descriptive statistics and plotting using a dataset of 237 individuals who were subject to post-mortem examination at the Middlesex Hospital in London around the turn of the 20th century. Study authors used cadavers to see if a relationship between brain weight and other, more easily measured, physiological characterizes such as age, sex, and head size could be determined. The end goal was to develop a way to estimate a person’s brain size while they were still alive (as the living aren’t keen on having their brains taken out and weighed).

## Data

Download the `Brainhead.xlsx` file posted to Canvas and copy it into your Codespace. You can do this by locating the file in Finder or Windows Explorer and then dragging and dropping it into the Codespace file browsing pane. Make sure it's in the `1-Statistics` directory we created to hold files for the first unit.

You can then create a Python script in the terminal using:
```
touch brains.py
```
and open it for editing using
```
code brains.py
```

Here's some starter code that loads the file into a Pandas data frame.
```
"""
Process the Brainhead data set
"""

import pandas as pd
from matplotlib import pyplot as plt

# Load the Excel file into a dataframe
df = pd.read_excel('Brainhead.xlsx')

# Display basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Display the first few rows
print("\nFirst few rows of the data:")
print(df.head())
```
Put the code into `brains.py` and then run it at the terminal by typing
```
python3 brains.py
```

## Installing a new package

The first time you run the script you'll probably see an error telling you that you need the `openpyxl` package. This is easily remedied using `pip`, the Package Installer for Python.
```
pip install openpyxl
```

The codespace comes pre-loaded with many useful packages, including `pandas`, `numpy`, and `matplotlib`, but it doesn't have everything. Sometimes you need to `pip install` a package, but it's almost always a one-time fix.

## Look at the data

Once you can run the script, you'll see output like the following:
```
First few rows of the data:
   Gender  Age  Head  Brain
0       1    1  4512   1530
1       1    1  3738   1297
2       1    1  4261   1335
3       1    1  3777   1282
4       1    1  4177   1590
```

Before proceeding, it's important to sanity-check the output and make sure what you see makes sense. Here, it's not immediately clear how to interpret the results:

- What is a Gender of 1?
- The first few rows have an Age of 1. Does that mean 1 year old, or some other encoding?
- What are the units of Head and Brain, and are they the same?

The answers to these questions are found in the **data dictionary**, a document that describes the fields of a dataset and explains the types, values, encodings, and other relevant information needed to use if effectively.

Look at the `Brainhead.doc` file posted to Canvas to see the data dictionary. How are Gender and Age encoded? What are the units of Head and Brain?

##  Five-number summary

Calculate the mean brain weight. Continue the analysis to calculate the five-number summary of the Brain field.

Identify any outliers using the 1.5 * IQR rule.


## Plot

Produce a histogram plot of the Brain data. Label the axis, making sure to specify the units.
```
plt.xlabel('Brain weight (grams)')
```
Save the histogram to a file named `brain_hist.png`.
```
plt.savefig('brain_hist.png', bbox_inches='tight')
```

Repeat to produce a box plot. Label the y-axis and save the file as `brain_box.png`.
