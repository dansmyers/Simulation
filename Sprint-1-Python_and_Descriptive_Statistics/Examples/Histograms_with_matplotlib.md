# Plotting Histograms in `matplotlib`

## Overview

This note shows how to plot a histogram using `matplotlib`, a popular Python visualization library based on the visualization tools in the MATLAB language. Similar code will
work for creating box plots: just substitute the box plot function (hint: you can look it up in the documentation).

## Installing Matplotlib

Open the terminal in your Mimir IDE.

Install `matplotlib` using `pip`, the basic Python package manager.

```
pip install python-matplotlib
```

or 

```
pip install matplotlib
```

## Example Script

```
# Import matplotlib and configure it to save files in the web IDE
#
# These three lines should be at the start of any script that uses matplotlib on Mimir
import matplotlib
matplotlib.use('Agg')  # <-- Required if you're using matplotilb in Mimir, see below
from matplotlib import pyplot as plt

# Example data
data = [10, 12, 15, 25, 4, 8, 11, 64, 100]

# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(data, 15)

# Title and axis labels
plt.title('Example Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('example_histogram.png', bbox_inches='tight')
```

Put this into a file named `histogram.py` and run it using `python3`.

```
python3 histogram.py
```

## Output

The final plot will be saved into `example_histogram.pdf`. You may need to reload Mimir to make it appear in your file browser pane; you can then download it and make sure that it appears the way you want.

## Notes

Notes on the functions in this example:

- `matplotlib.use('Agg')` configures the output engine of matplotlib to a setting that works with web-based IDEs like Mimir's. Noramlly, Matplotlib would make any plots you create appear on your desktop, but that isn't possible in Mimir, so we'll just save everything to a PDF.

- `plt.hist` plots the histogram on the current figure. The second argument that specifies the number of bins; the default is ten.

- `plt.savefig` outputs the plot to a PDF file. The `bbox_inches = 'tight'` argument tells the output engine to eliminate unnecessary white space around the figure in the final PDF. It isn't required, but it makes the plot easier to use if you need to embed it in a document.
