# Python assignment 4 — Week 9

## Topics to cover
- Working with files: input and output.
- Using `for` loops to process files one line at a time.
- Using `.readline()` to read a second line within a loop.
- Using regular expressions to find exact sequence motifs and variable-length repeats.
- Using `re.search()`, `re.findall()`, and `sys.argv`.

## Summarizing DNA sequence motifs in biological sequence data

This week we will work with DNA sequence data from several different species: a bird (*Manacus vitellinus*; `Manacus_vitellinus.gene.cds.fa.gz`) and two pines (*Pinus contorta*; `contorta_454.fa.gz`, and *Pinus taeda*; `Pta.seq.uniq.gz`). Download the files from the course website and decompress them with `gunzip`. These are collections of coding or transcript-derived sequences, **not complete genome assemblies**.

**Start with one file.** Once your script works, test it on the others. You can submit a Python script (`.py`) or Jupyter notebook (`.ipynb`). Make sure your results are clearly labeled and that the code can be run again.

**Important assumption:** For this assignment, we will use FASTA files formatted with **one identifier line (`>`) followed by one complete sequence line**. The paired-line reading approach below works for this format, but not for general FASTA files where a sequence may span multiple lines.

## Task 1 — Count restriction enzyme recognition sites

Write a program that reads a FASTA file and counts the following exact DNA sequence motifs:

- **EcoRI:** `GAATTC`
- **MseI:** `TTAA`
- **HindIII:** `AAGCTT`

#### A. Count the sequences
Count the total number of FASTA records in the file. Remember that each identifier line beginning with `>` represents a sequence. Initialize your counter **before** the loop and increment it as you read the file.

#### B. Count restriction sites
Count the number of matches to each motif across all sequences in the file. You can use `len(re.findall(...))` to count matches within one sequence, then add those counts to running totals. For this assignment, count **nonoverlapping matches on the sequence as written**.

#### C. Summarize your results
Print a clearly labeled summary that includes the input filename, number of sequences, and total matches for each restriction site. You may also write the summary to a text file.

## Task 2 — Find microsatellite repeats

Microsatellites, or simple sequence repeats (SSRs), consist of short DNA motifs repeated consecutively. For example, `ATATATATAT` contains five consecutive `AT` repeats. Microsatellites are useful molecular markers because repeat number can vary among individuals.

#### A. Count AT repeats
Count the number of distinct regions containing **at least four consecutive `AT` repeats**.

#### B. Count ATC repeats
Count the number of distinct regions containing **at least four consecutive `ATC` repeats**.

#### C. Count GA repeats
Count the number of distinct regions containing **at least four consecutive `GA` repeats**.

**Hint:** Group the entire motif before applying a repetition quantifier, e.g., `(?:AT){4,}`. A noncapturing group `(?:...)` lets `re.findall()` return the entire repeated region. Count **repeat regions (loci)**, not the number of repeat units within those regions.

#### D. Export sequences containing SSRs
Create a new FASTA file containing **every sequence that has at least one of the three types of SSRs**. Write both the original identifier line and the complete sequence. Each sequence should be written **only once**, even if it contains multiple SSRs or multiple motif types. Print the number of sequences exported.

### Hint: reading a FASTA file two lines at a time

For files formatted with exactly two lines per record, you can read the identifier and sequence together:

```python
for Line in IN:
    Fasta = Line.strip("\n")
    Seq = IN.readline().strip("\n")
    # Work with Fasta and Seq here
```

For example, a record might look like:

```text
>seq2.prot.hox3 pos:1122424444
ATATATATCGGGCGTAAAATGGCGCTAGTTTGGGCCAATATTTTTTTAAAAAAAAAAAAAAAAAAAAA
```

You may use this approach for both tasks. Remember to initialize totals before entering the loop, and close files when you finish (or use `with open(...)`).

## Optional extension — Analyze multiple files

Modify your script so that you can provide **multiple FASTA filenames** as command-line arguments. For each file, produce a separate summary of the restriction-site counts and SSR counts, and write an SSR-containing FASTA output with a filename that identifies the source dataset. Use `sys.argv[1:]` to access all filenames supplied after the script name.

For example:

```bash
python cutsite_micro_multi_exportSSR.py Manacus_vitellinus.gene.cds.fa contorta_454.fa Pta.seq.uniq.fa
```

**Before submitting:** Check that your sequence counts are plausible, that all three motifs are counted separately, and that the exported FASTA file retains matching identifier/sequence pairs.
