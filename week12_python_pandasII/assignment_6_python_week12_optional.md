# Week 12 — Optional Pandas and Data Visualization Assignment

**Dataset:** `states_covid.csv` (place in the same directory as your notebook).  
**Status:** Optional, ungraded practice.  
**Goal:** Practice importing, inspecting, filtering, grouping, and visualizing tabular data using pandas, matplotlib, and seaborn.

This dataset contains daily state-level COVID reporting records. `positiveIncrease` and `deathIncrease` are *daily reported changes*; `positive` and `death` are *cumulative totals*. Reporting artifacts and missing values are possible. **Do not sum cumulative totals across dates.** You do not need to use every column.

Use the Week 12 primer as a reference. Write code for each lettered task and briefly interpret your figures. The solutions below are only in the separate instructor notebook.

## 1. Import and inspect

#### A. Import pandas, matplotlib.pyplot, and seaborn; read `states_covid(1).csv` into a DataFrame called `df`.

#### B. Display the first five rows, the shape of the DataFrame, and the column names.

#### C. Use `.info()` and report how many missing values occur in `deathIncrease` and `positiveIncrease`.


## 2. Dates, filtering, and sorting

#### A. Convert `date` to a pandas datetime column using `pd.to_datetime()`.

#### B. Create `west_df` containing only Nevada (`NV`), California (`CA`), Oregon (`OR`), and Arizona (`AZ`). Keep only dates on or after `2020-06-01`.

#### C. Sort `west_df` by date, then display the five Nevada dates with the highest `positiveIncrease` values (show date and daily reported cases).


## 3. Group and summarize

#### A. Using `west_df`, calculate mean daily reported cases (`positiveIncrease`) and mean daily reported deaths (`deathIncrease`) for each state using `groupby()` and `.agg()`.

#### B. Add a count of non-missing daily case observations for each state. Which state has the highest mean daily reported cases in this period?

#### C. In one or two sentences, explain why the state with the highest *absolute* daily case count need not have the highest per-capita rate.


## 4. Visualize and interpret

#### A. Use seaborn to make a boxplot comparing `positiveIncrease` across the four states. Label both axes and add a title.

#### B. Make a line plot of daily reported cases in Nevada through time using matplotlib or seaborn. Add a seven-day rolling mean as a second line (sort by date first). Include a legend.

#### C. Save one figure as a PNG (`dpi=300`) and write two sentences describing one pattern and one limitation of the data.


**Optional extension:** Use `sns.relplot(..., col="state", col_wrap=2, kind="line")` to create four small-multiple time-series panels. Explain whether you would use shared or independent y-axis scales.
