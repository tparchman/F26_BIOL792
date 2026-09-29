# Python Assignment 1: Scalars, Strings, and Basic Calculations

The goal of this assignment is to practice the Python concepts introduced this week: variables, strings, integers, floats, string methods, mathematical operations, `input()`, type conversion, and f-strings.

For each problem, write a Python script (`.py` file) that accomplishes the requested tasks. Include comments in your code describing the major steps.

---

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

## 2. Calculating a sampling summary

You are collecting data from a field study. At one sampling site, you counted the number of individuals of a species in a rectangular sampling plot.

Write a Python script that asks the user for:

- the **length of the plot in meters**
- the **width of the plot in meters**
- the **number of individuals counted**

Your program should then:

1. Calculate the area of the plot in square meters.
2. Calculate the density of individuals per square meter.
3. Estimate how many individuals would occur in an area of 100 square meters if the same density were maintained.
4. Print a clearly labeled summary of the results.
5. Report area, density, and the estimated number of individuals to two decimal places.

Remember that values obtained with `input()` are strings. Convert the measurements to the appropriate numeric type before performing calculations.

For example:

```py
length = float(input("Enter plot length in meters: "))
```

and:

```py
count = int(input("Enter number of individuals counted: "))
```

You can use f-strings to control the appearance of your output:

```py
print(f"Plot area: {area:.2f} square meters")
```

If a user entered a plot length of `8`, a width of `5`, and a count of `23`, your program should produce output similar to:

```text
Sampling summary
Plot area: 40.00 square meters
Individuals counted: 23
Density: 0.57 individuals per square meter
Estimated individuals per 100 square meters: 57.50
```

---

## 3. Expected genotype frequencies under Hardy-Weinberg equilibrium

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
AA = 0.122
Aa = 0.455
aa = 0.423

Check: genotype frequencies sum to 1.000
```

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