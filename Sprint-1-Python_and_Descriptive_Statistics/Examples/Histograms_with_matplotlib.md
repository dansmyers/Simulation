# Histograms

## Overview

This note shows how to plot a histogram using Matplotlib, a popular Python visualization library based on the visualization tools in the MATLAB language.

## Installing Matplotlib

Open the terminal in your Mimir IDE.

Install Matplotlib using `apt-get`, the basic package manager for Debian Linux distributions:

```
sudo apt-get install python-matplotlib
```

You may recall that `sudo` is the *substitute user do* command. Linux systems always make a distinction between regular users (i.e., your normal user account), who are restricted from performing potentially damaging or insecure operations, and the `root` account, which is allowed to modify pretty much anything on the system. `sudo` allows you to run a single command with root-level privileges, so it's typically used when you want to perform one operation that modifies the system, like installing a new program. Your Mimir account is automatically configured so that you can use `sudo` to install new programs.

## 

Here's an example Matplotlib script.

```
# Import matplotlib and configure it to save files in the web IDE
#
# These three lines should be at the start of any script that uses matplotlib on Mimir
import matplotlib
matplotlib.use('Agg')  # <-- Required if you're using matplotilb in Mimir, see below
from matplotlib import pyplt as plt

# Example data
data = [10, 12, 15, 25, 4, 8, 11, 64, 100]

# Create a new figure -- you must do this before calling a plotting function
plt.figure()

# Create a histogram with 15 bins
plt.hist(data, 15)

# Title and axis labels
plt.title('Example Histogram')
plt.xlabel('Data value')
ply.ylabel('Count')

# Save the figure to a file
plt.savefig('example_histogram.pdf', bbox_inches='tight')
```

Put this into a file named `histogram.py` and run it using `python3`.

```
python3 histogram.py
```

The final plot will be saved into `example_histogram.pdf`. You may need to reload Mimir to make it appear in your file browser pane; you can then download it and make sure that it appears the way you want.

Notes on the functions in this example:

- `matplotlib.use('Agg')` configures the output engine of matplotlib to a setting that works with web-based IDEs like Mimir's. Noramlly, Matplotlib would make any plots you create appear on your desktop, but that isn't possible in Mimir, so we'll just save everything to a PDF.

- `plt.hist` plots the histogram on the current figure. The second argument that specifies the number of bins; the default is ten.

- `plt.savefig` outputs the plot to a PDF file. The `bbox_inches = 'tight'` argument tells the output engine to eliminate unnecessary white space around the figure in the final PDF. It isn't required, but it makes the plot easier to use if you need to embed it in a document.
