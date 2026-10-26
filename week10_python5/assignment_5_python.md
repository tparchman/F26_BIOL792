# Python Assignment 5 — Data Management and Manipulation
## Data Science for Biology | Week 10

### Topics
- Reading and writing files; nested `for` loops
- Processing many files using `glob` or `sys.argv`
- Working with lists, strings, and regular expressions
- Organizing, cleaning, and checking real datasets

## Background: pika temperature loggers

This week we will work with a real data-management problem. Kelly Klingler, a former PhD student in the Peacock lab, collected microclimate data around pika haypiles in 2012–2014. Temperature loggers were placed at 19 haypile locations (H1–H19), with two loggers per location: one at the surface (`S`) and one deeper in the talus slope (`D`). There were 38 logger files for 2012–2013 (`13`) and 37 for 2013–2014 (`14`); one logger was lost to water damage. **There are 75 input files in total.**

The data are provided as `logfiles.tgz` on the course webpage. Download the archive and extract it from a terminal:

```bash
tar -zxvf logfiles.tgz
```

Look at several extracted files before writing code. Each logger file has five columns. **Ignore the first column** and retain the four fields containing date, time, AM/PM, and temperature. Pay attention to how columns are separated, whether there are any headers, and whether there are problematic characters.

A filename such as `1901302136_H15_D_14.txt.txt` encodes the logger ID (`1901302136`), haypile (`H15`), position (`D`), and collection year (`14`).

## The assignment

**Write a Python program that processes all 75 logger files and produces one combined output file.** Instead of retaining the input files' column-oriented arrangement, your output should have **four lines for each input file**: one line for all dates, one for times, one for AM/PM indicators, and one for temperatures. Every output line must begin with the four comma-separated fields extracted from its filename:

`logger_ID,haypile,position,year,values...`

For example, the beginning of the four output lines for `1901302108_H7_D_13.txt.txt` should resemble:

```text
1901302108,H7,D,13,10/7/2012,10/7/2012,10/7/2012,...
1901302108,H7,D,13,8:00:00,8:35:00,9:10:00,...
1901302108,H7,D,13,AM,AM,AM,...
1901302108,H7,D,13,41.4,41.4,41.4,...
```

The ellipses here indicate additional observations; **do not write literal `...` in your output**. Keep values in their original order. Do not add an extra comma at the end of each line. The output is a special, transposed format for this exercise, rather than a conventional one-observation-per-row CSV table.

### 1. Inspect and locate the files

#### A. Examine the input
Open at least two logger files, including files from different years. Identify how the five columns are separated and which four you need to retain.

#### B. Find the files
Use `glob.glob()` from a notebook **or** `sys.argv[1:]` in a command-line script to collect the input filenames. Confirm that your program finds 75 files. Be careful about the directory containing the files.

### 2. Process the filename and file contents

#### A. Extract logger information
For every input file, obtain the logger ID, haypile, position (`S` or `D`), and year (`13` or `14`) from its filename. You can use `split()`, string replacement, or a regular expression. Store these as four separate strings.

#### B. Read and clean the data
Open each file and loop through its lines. Remove newline and null (`\0`) characters as necessary. Skip any non-data header lines if present. Ignore the first data column.

#### C. Organize the measurements
For each file, build four separate lists: dates, times, AM/PM indicators, and temperatures. Make sure the lists are **reset for each new file**. The values should remain in their original order.

### 3. Write the combined output

#### A. Create one output file
Write the four lists for each input file as four comma-separated lines, preceded by the logger information. Open the **combined output file once, before** the loop through input files, and close it when processing is complete. Use a name such as `combined_logger_data.csv`.

#### B. Check your output
Report the number of input files processed and the number of output lines. With 75 files and four lines per file, the combined output should contain **300 lines**. Check that each group of four lines has matching logger information, and that the four lists for each logger have the same number of observations.

### 4. Turn in

#### A. Python code
Submit your working `.py` script or `.ipynb` notebook. Code should be readable and include brief comments describing the main steps.

#### B. Verification
Include the number of files processed and output lines written, and briefly indicate whether your checks passed. You do **not** need to submit the large combined data file unless requested.

## Hints (use these as needed)

**Loop through many files in Jupyter:**

```python
import glob
filelist = sorted(glob.glob("*.txt.txt"))  # Adjust path if files are in a subdirectory
print(len(filelist))
for filename in filelist:
    IN = open(filename, "r", encoding="utf-8", errors="ignore")
    # Process this file here
    IN.close()
```

**Or run a script with filenames as arguments:**

```python
import sys
filelist = sys.argv[1:]
```

For example, from the directory containing your logger files: `python3 logger.py *.txt.txt`.

**Clean a line:** `line = line.strip("\n").replace("\0", "")`.

**Convert a list of strings to one comma-separated string:** `",".join(values)`.

**Program structure to think about:** find files → open one input file → collect its four lists → write four lines → repeat for the next file → check results.

**Important:** The logger archive is not included in this assignment document. Test your code against the actual files and adjust the line parsing to their observed delimiter/header structure.
