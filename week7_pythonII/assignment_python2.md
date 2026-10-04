# Python Assignment 2. Lists, Conditionals, and Loops

## Topics to cover

-   Working with strings and lists
-   Indexing and slicing
-   Converting between strings and lists
-   Conditional statements
-   `for` loops
-   Counters and `.append()`
-   Combining operations in simple data-processing workflows

Write clear Python code and use informative `print()` statements so
someone running your code can understand the results.

## 1. Working with sequence information

Start with:

``` python
dna_info = "HOWR_017,Nevada,ATATCTCGCGGGGTTTATATATAttaatatatacgg"
```

This string contains three comma-delimited fields: sample name,
population, and DNA sequence.

#### A. Use `.split()` to turn `dna_info` into a list. Print the resulting list.

#### B. Using list indices, save the sample name, population, and DNA sequence as three separate variables. Print a sentence identifying the sample and population:

``` text
Sample HOWR_017 is from Nevada
```

#### C. Convert the DNA sequence to uppercase. Print the sequence and its length.

#### D. Count the number of `A`, `C`, `G`, and `T` bases. Calculate GC content:

``` text
GC content = (number of G bases + number of C bases) / total sequence length
```

Print GC content to **three** decimal places.

#### E. Use `if`/`else` to classify the sequence as `"GC-rich"` if GC content is greater than or equal to 0.50, and `"AT-rich"` otherwise. Print theclassification.

#### F. Use list slicing (e.g., list[:10]) to save the first 10 and last 10 bases as two new variables. Print both.

## 2. Filtering a list of measurements

Start with:

``` python
measurement_data = "12.4,8.7,15.1,4.3,19.8,10.2,6.6,14.5,21.3,9.8"
```

#### A. Use `.split()` to convert `measurement_data` into a list. Print the list and its length. Notice that its elements are still strings.

#### B. Create an empty list called `measurements`. Use a `for` loop to move through the list from A, convert each value to a `float`, and `.append()` it to `measurements`. Print the new list.

#### C. Create two empty lists:

``` python
large_values = []
small_values = []
```

Loop through `measurements`. If a value is greater than or equal to 10, append it to `large_values`. Otherwise append it to `small_values`. 

Print both lists and the number of elements in each.

#### D. Use a `for` loop to calculate the sum of all values in `measurements`.

Start with:

``` python
total = 0
```

During each trip through the loop, add the current measurement to `total`. After the loop, calculate the mean using `total` and `len(measurements)`. Print the total and mean.

**Do not use `sum()` for this problem.** The goal is to practice
accumulating (e.g., counter += 1) a value during a loop.

#### E. Use `if`/`elif`/`else` to classify the mean: - ≥ 15: `"high"` - ≥ 10 but
\< 15: `"moderate"` - \< 10: `"low"`

Print the classification.

## 3. Processing samples with loops and conditionals

Below is a list of simplified sample records. Each contains sample name,
population, and sequence separated by commas.

``` python
samples = [
    "HOWR_01,NV,ATGCGCGTAA",
    "HOWR_02,CA,ATATATTTAA",
    "HOWR_03,NV,GCGCGCCGTA",
    "HOWR_04,OR,AATTGGCCAA",
    "HOWR_05,NV,GGGCCCGCTA"
]
```

Use **one `for` loop** to process all five records.

#### A. Inside the loop, use `.split()` to separate each record into sample name, population, and DNA sequence. For each sample, print sample name, population, and sequence length:

``` text
HOWR_01, NV, sequence length = 10
```

#### B. Inside the same loop, calculate GC content for each sequence. Print sample name and GC content to two decimal places.

#### C. Still inside the loop, classify each sequence: - ≥ 0.60: `"high GC"` - ≥ 0.40 but \< 0.60: `"intermediate GC"` - \< 0.40: `"low GC"`

Print the classification for each sample.

#### D. Before the loop, create:

``` python
nv_samples = []
```

During the loop, if a sample is from `"NV"`, append its sample name to
`nv_samples`. After the loop, print the complete list and the number of
Nevada samples.

#### E. Add a counter that tracks the number of sequences classified as `"high GC"`. Initialize it before the loop and update it inside the loop. After the loop, print the number of high-GC samples.

## 4. Challenge: summarize samples by population

Use the same `samples` list from Problem 3.

#### A. Create three counters called `num_nv`, `num_ca`, and `num_or`, and initialize each to `0`. Write a `for` loop that processes each record, uses `.split()` to identify its population, and updates the appropriate population counter.

After the loop, print the number of samples from each population.

#### B. Create an empty list called `long_sample_names`. During the same loop (or in a new loop), append the sample name to this list if its name contains more than 6 characters.

After the loop, print `long_sample_names` and the number of sample names it contains.

#### C. Create an empty list called `gc_values`. Loop through the sample records, calculate the GC content of each DNA sequence, and append each GC-content value to `gc_values`.

After the loop, print the complete list of GC-content values.

#### D. Use another `for` loop and a counter to determine how many values in `gc_values` are greater than or equal to `0.50`. Print the final count.

#### E. In 1–2 sentences as a comment in your code, explain why it can be useful to first extract or calculate values into a list such as `gc_values`, rather than doing every analysis inside the original loop.



## What to turn in

Turn in completed code for **Problems 1,2, and 3**. Code should run
from beginning to end without errors and contain informative output.
