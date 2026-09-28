# Python Assignment 1: Scalars, Strings, and Basic Calculations

The goal of this assignment is to practice the Python concepts introduced this week: variables, strings, integers, floats, string methods, mathematical operations, `input()`, type conversion, and f-strings. For each problem, write a Python script (`.py` file) that accomplishes the requested tasks. Include comments in your code describing the major steps.

## 1. Summarizing a DNA sequence

Start with the following DNA sequence:

```py
seq = "  atgctagCGATCGGctaacggttATGC  \n"
```

Write a script that:

1. Removes whitespace from the beginning and end of the sequence.
2. Converts the entire sequence to uppercase.
3. Determines the length of the sequence.
4. Counts the number of `A`, `C`, `G`, and `T` bases.
5. Calculates GC content as the proportion of bases that are either G or C.
6. Creates an RNA version of the sequence by replacing `T` with `U`.
7. Prints a clearly labeled summary of your results. Report GC content to three decimal places.

Some Python tools that may be useful:

```py
seq.strip()
seq.upper()
len(seq)
seq.count("A")
seq.replace("T", "U")
```

Remember that an f-string can be used to produce clean output:

```py
print(f"Sequence length: {length} bases")
print(f"GC content: {gc_content:.3f}")
```

---

## 2. Expected genotype frequencies under Hardy-Weinberg equilibrium

Write a Python script that calculates expected genotype frequencies under Hardy-Weinberg equilibrium for a locus with two alleles, `A` and `a`.

Recall that:

**p + q = 1**

and expected genotype frequencies are:

**AA = p²**

**Aa = 2pq**

**aa = q²**

Your program should:

1. Use `input()` to ask the user for the frequency of allele A (`p`).
2. Convert the value entered by the user to a float.
3. Calculate the frequency of allele a (`q`).
4. Calculate the expected frequencies of `AA`, `Aa`, and `aa`.
5. Calculate the sum of the three genotype frequencies as a check.
6. Print all allele and genotype frequencies to three decimal places.

Remember that `input()` returns a string, so you will need to convert the input before doing calculations:

```py
p = float(input("Enter the frequency of allele A (p): "))
```

Your output should be clearly labeled and look something like:

```text
Allele frequencies:
p = 0.350
q = 0.650

Expected genotype frequencies:
AA = 0.123
Aa = 0.455
aa = 0.423

Check: genotype frequencies sum to 1.000
```

---

## 3. Calculating allele frequencies from observed genotype counts

Suppose you sampled a population and observed the following genotype counts:

```text
AA = 37
Aa = 46
aa = 17
```

Write a Python script that stores these values as variables and calculates:

1. The total number of individuals sampled.
2. The total number of copies of the gene sampled. Remember that each diploid individual carries two copies.
3. The total number of `A` alleles in the sample.
4. The total number of `a` alleles in the sample.
5. The frequency of allele `A` (`p`).
6. The frequency of allele `a` (`q`).
7. The observed heterozygosity: the proportion of sampled individuals that have genotype `Aa`.
8. A check showing that `p + q = 1`.

Begin by storing the genotype counts as integers:

```py
AA = 37
Aa = 46
aa = 17
```

Think carefully about how many copies of each allele are contributed by each genotype. For example, an `AA` individual contributes **two A alleles**, while an `Aa` individual contributes **one A and one a allele**.

Use f-strings to produce clearly labeled output, and report frequencies to three decimal places.

---

## 4. Find and fix the problem

Consider the following Python code:

```py
sequence = "ATGCGTA"
length = "7"

print(length + 3)
```

Copy this code into Python and run it.

1. What error does Python report?
2. Use `type()` to determine the type of the variable `length`.
3. Explain briefly why `length + 3` does not work.
4. Fix the code **without changing the original assignment `length = "7"`** so that Python correctly prints `10`.

The following may be useful:

```py
type(length)
int(length)
```

Include your corrected code and, as a comment in the script, briefly explain what caused the original error.