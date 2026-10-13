# Python assignment 3

## Topics to cover

-   Working with files: input/output
-   More with lists
-   `sys.argv`, `re.search`
-   `for` loops and processing files one line at a time

<br>

### This week you will work more with lists, and more importantly, get comfortable reading IN and writing OUT. We are not literally reading the contents of entire files into memory at once. Instead, we are making connections (file objects or handles) between our program and these files, and using `for` loops to process data one line at a time. The `python_3_primer.ipynb` and slides from class should help get you started.

<br>

## 1. Reading a file and building a list

The file **genenames.txt** has two columns. The second column contains
gene names. Write a script that reads the file one line at a time and
stores the gene names in a list.

<br>

#### A. Open `genenames.txt` for reading.

You can hardcode the file name, especially if you are working in
Jupyter.

<br>

#### B. Use a `for` loop to process the file one line at a time. For each line, remove the line ending and split the line into a list.

<br>

#### C. Extract the gene name from the second column and append it to a new list.

Initialize an empty list before entering the `for` loop, then add one
gene name to that list each time through the loop.

<br>

#### D. After the loop is finished, print the list of gene names to check that your script worked.

<br>

## 2. Reading, filtering, and writing output

Now write a similar script to read the data in **flies.txt**. This file
has three columns: fly number, day or night, and seconds of flying time
recorded. You want to keep the flying times only for observations
recorded at night (`N`).

#### A. Open `flies.txt` for reading and create an empty list that will hold the night-time flying values.

You can hardcode the input file name or use `sys.argv` to provide it
from the command line.

<br>

#### B. Process the file one line at a time. Remove the line ending and split each line into a list.

<br>

#### C. Use an `if` statement to identify lines for which the day/night column is `N`. For those lines only, append the flying time to your list.

<br>

#### D. Open an output file for writing and write the night-time flying values to the file, one value per line.

Remember that `.write()` writes strings and does not automatically add a
line ending.

<br>

## 3. Processing DNA sequence data

Here we are going to process a FASTA file,
**no60_intron_IME_data.fasta**, containing DNA sequence data for 59,260
intron sequences. You will calculate summary information for each
sequence and write that information to an output file.

For this file, each sequence is represented by an ID line beginning with
`>` followed by a line containing the DNA sequence. Use a `for` loop to
process the file one line at a time. You will need to recognize whether
each line is an ID line or a sequence line and do something different
for each.

You can hardcode the input file name, especially if you are using
Jupyter, or use `sys.argv` to provide the file name from the command
line.

<br>

#### A. Open the FASTA file for reading and open a new output file for writing.

<br>

#### B. Process the FASTA file one line at a time and remove the line ending from each line.

Use `re.search()` to recognize ID lines that begin with `>`.

``` python
if re.search("^>", Line):
```

When you encounter an ID line, save that ID so that you can use it when
you process the sequence line that follows.

<br>

#### C. For each DNA sequence, calculate its sequence length.

Remember that each sequence line is a string, so `len()` can be used to
determine its length.

<br>

#### D. For each DNA sequence, calculate its GC content.

GC content is the proportion of bases in a DNA sequence that are either
G or C. Remember that `str.count('G')` and `str.count('C')` can be used
to count bases in a sequence string.

<br>

#### E. Write one line to your output file for each sequence containing the sequence ID, sequence length, and GC content.

Your output should look something like:

``` text
>AT1G68260.1_i1_204_CDS, Sequence length: 152, GC content: 0.355263
>AT1G68260.1_i2_457_CDS, Sequence length: 719, GC content: 0.350487
>AT1G68260.1_i3_1286_CDS, Sequence length: 82, GC content: 0.365854
```

And the output file should have the same number of lines as the input file

<br>

#### F. Keep track of the total number of DNA sequences as the file is processed.

Initialize a counter before the loop and update it each time you process
a DNA sequence.

<br>

#### G. Keep running totals that will allow you to calculate GC content across all sequences in the file.

Think about which values need to accumulate each time you process a
sequence.

<br>

#### H. After the `for` loop is finished, print to the screen:

1.  the total number of DNA sequences
2.  the overall GC content across all sequences in the file

The calculation for the entire collection of sequences should be done
**after** the loop, using the running totals that were accumulated while
the file was being processed.

<br>

### What to turn in

Turn in your script for **Problem 3**.
