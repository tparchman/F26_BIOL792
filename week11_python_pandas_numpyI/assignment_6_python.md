# Optional Assignment 6: NumPy and an Introduction to pandas

**Week 11 — Introduction to Data Science for Biology**

This optional assignment practices NumPy arrays, numerical summaries, Boolean indexing, and a first look at pandas. Next week we will work more extensively with pandas.

Use the three CSV files provided with the assignment. Keep them in the same directory as your notebook or script. You can work in Jupyter or a Python script. Include code and printed answers for each part.

Start with:

```python
import numpy as np
import pandas as pd
```

## 1. Geographic coordinates with NumPy

The file `muricata_pops_lat_long.csv` contains latitude and longitude coordinates for sampled populations, with **no header row**. Latitude is in column 0 and longitude in column 1.

#### A. Read the file into a NumPy array using `np.loadtxt()`. Print the array and its `.shape`.

#### B. Use array slicing to create separate arrays for latitude and longitude. Print the minimum, maximum, and mean latitude.

#### C. Use Boolean indexing to select latitudes greater than 38 degrees north. Print those latitudes and the number of coordinates meeting the condition.

#### D. Create a new two-column array containing only the rows with latitude greater than 38. Save the resulting array as `muricata_north.csv` using `np.savetxt()`.

## 2. Fish traits: first steps with pandas

`Bloom_etal_2018_Reduced_Dataset.csv` contains fish taxa, log body size, trophic position, and a category (`Reg`) indicating whether a taxon is diadromous or non-diadromous.

#### A. Read the file using `pd.read_csv()`. Print the first five rows with `.head()` and inspect the number of rows and columns with `.shape`.

#### B. Select the `logbodysize` column and calculate its mean and standard deviation using `.mean()` and `.std()`.

#### C. Select rows where `Reg` is `diadromous`. Print the number of rows and the mean `trophic_position` for this subset.

## 3. Optional extension: exploring a larger dataset

`states_covid.csv` contains COVID-19 observations by state and date. It is much larger and has many missing entries. This problem is an optional extension, not a required introduction to pandas.

#### A. Read the file with `pd.read_csv()`. Print its `.shape` and the first five rows of just the `date`, `state`, and `positive` columns.

#### B. Select rows where `state` equals `NV`. Print how many rows remain.

#### C. Calculate the maximum value of `positive` for Nevada, ignoring missing values (pandas does this by default). What does this number describe? Why is it not necessarily the number of new cases on a particular day?

**Reminder:** For the pandas questions, the only new methods you need are `pd.read_csv()`, `.head()`, `.shape`, `.mean()`, `.std()`, `.max()`, and simple column selection/filtering. We will explore pandas in depth next week.
