# Python Assignment 2 — Answer Key

There are often multiple correct ways to accomplish the same task in Python. This key gives one clear solution to each lettered subproblem.

# 1. Working with sequence information

Start with:

```python
dna_info = "HOWR_017,Nevada,ATATCTCGCGGGGTTTATATATATTATTTAAA"
```

#### A. Use `.split()` to turn `dna_info` into a list.

```python
data_list = dna_info.split(",")

print(data_list)
```

#### B. Use list indices to save the sample name, population, and DNA sequence as separate variables.

```python
sample = data_list[0]
population = data_list[1]
dna_seq = data_list[2]

print(f"Sample {sample} is from {population}")
```

#### C. Convert the DNA sequence to uppercase and print the sequence and its length.

```python
dna_seq = dna_seq.upper()

print(f"Sequence: {dna_seq}")
print(f"Sequence length: {len(dna_seq)}")
```

#### D. Count each base and calculate GC content.

```python
num_a = dna_seq.count("A")
num_c = dna_seq.count("C")
num_g = dna_seq.count("G")
num_t = dna_seq.count("T")

gc_content = (num_g + num_c) / len(dna_seq)

print(f"A: {num_a}")
print(f"C: {num_c}")
print(f"G: {num_g}")
print(f"T: {num_t}")
print(f"GC content: {gc_content:.3f}")
```

#### E. Classify the sequence as GC-rich or AT-rich.

```python
if gc_content >= 0.50:
    print("GC-rich")
else:
    print("AT-rich")
```

#### F. Use slicing to save the first and last 10 bases.

```python
first_ten = dna_seq[:10]
last_ten = dna_seq[-10:]

print(f"First 10 bases: {first_ten}")
print(f"Last 10 bases: {last_ten}")
```

# 2. Filtering a list of measurements

Start with:

```python
measurement_data = "12.4,8.7,15.1,4.3,19.8,10.2,6.6,14.5,21.3,9.8"
```

#### A. Use `.split()` to convert `measurement_data` into a list.

```python
measurement_strings = measurement_data.split(",")

print(measurement_strings)
print(f"Number of measurements: {len(measurement_strings)}")
```

#### B. Convert each measurement to a `float` and append it to a new list.

```python
measurements = []

for value in measurement_strings:
    measurements.append(float(value))

print(measurements)
```

#### C. Separate the measurements into `large_values` and `small_values`.

```python
large_values = []
small_values = []

for value in measurements:
    if value >= 10:
        large_values.append(value)
    else:
        small_values.append(value)

print(f"Large values: {large_values}")
print(f"Number of large values: {len(large_values)}")

print(f"Small values: {small_values}")
print(f"Number of small values: {len(small_values)}")
```

#### D. Calculate the total and mean using a `for` loop.

```python
total = 0

for value in measurements:
    total += value

mean = total / len(measurements)

print(f"Total: {total:.2f}")
print(f"Mean: {mean:.2f}")
```

#### E. Classify the mean as high, moderate, or low.

```python
if mean >= 15:
    classification = "high"
elif mean >= 10:
    classification = "moderate"
else:
    classification = "low"

print(f"Mean classification: {classification}")
```

# 3. Processing samples with loops and conditionals

Start with:

```python
samples = [
    "HOWR_01,NV,ATGCGCGTAA",
    "HOWR_02,CA,ATATATTTAA",
    "HOWR_03,NV,GCGCGCCGTA",
    "HOWR_04,OR,AATTGGCCAA",
    "HOWR_05,NV,GGGCCCGCTA"
]
```

The assignment asks students to use one loop for Parts A–E. The sections below show how each requested piece fits into that loop.

#### A. Split each record and print sample name, population, and sequence length.

```python
for record in samples:
    fields = record.split(",")

    sample = fields[0]
    population = fields[1]
    dna_seq = fields[2]

    print(f"{sample}, {population}, sequence length = {len(dna_seq)}")
```

#### B. Calculate and print GC content for each sequence.

This code belongs inside the same loop, after the variables in Part A have been created:

```python
num_g = dna_seq.count("G")
num_c = dna_seq.count("C")

gc_content = (num_g + num_c) / len(dna_seq)

print(f"{sample} GC content = {gc_content:.2f}")
```

#### C. Classify each sequence by GC content.

This also belongs inside the same loop:

```python
if gc_content >= 0.60:
    classification = "high GC"
elif gc_content >= 0.40:
    classification = "intermediate GC"
else:
    classification = "low GC"

print(f"{sample}: {classification}")
```

#### D. Save the names of Nevada samples.

Initialize the list **before** the loop:

```python
nv_samples = []
```

Then add this conditional **inside** the loop:

```python
if population == "NV":
    nv_samples.append(sample)
```

After the loop has finished:

```python
print(f"Nevada samples: {nv_samples}")
print(f"Number of Nevada samples: {len(nv_samples)}")
```

#### E. Count the number of high-GC samples.

Initialize the counter **before** the loop:

```python
high_gc_count = 0
```

Update it inside the high-GC condition:

```python
if gc_content >= 0.60:
    classification = "high GC"
    high_gc_count += 1
elif gc_content >= 0.40:
    classification = "intermediate GC"
else:
    classification = "low GC"
```

After the loop:

```python
print(f"Number of high-GC samples: {high_gc_count}")
```

### Complete solution for Problem 3

Because Parts A–E are intended to work together in a single loop, the complete solution is:

```python
nv_samples = []
high_gc_count = 0

for record in samples:
    fields = record.split(",")

    sample = fields[0]
    population = fields[1]
    dna_seq = fields[2]

    print(f"{sample}, {population}, sequence length = {len(dna_seq)}")

    num_g = dna_seq.count("G")
    num_c = dna_seq.count("C")
    gc_content = (num_g + num_c) / len(dna_seq)

    print(f"{sample} GC content = {gc_content:.2f}")

    if gc_content >= 0.60:
        classification = "high GC"
        high_gc_count += 1
    elif gc_content >= 0.40:
        classification = "intermediate GC"
    else:
        classification = "low GC"

    print(f"{sample}: {classification}")

    if population == "NV":
        nv_samples.append(sample)

print(f"Nevada samples: {nv_samples}")
print(f"Number of Nevada samples: {len(nv_samples)}")
print(f"Number of high-GC samples: {high_gc_count}")
```

# 4. Challenge: summarize samples by population

Use the same `samples` list from Problem 3.

#### A. Count samples from Nevada, California, and Oregon.

```python
num_nv = 0
num_ca = 0
num_or = 0

for record in samples:
    fields = record.split(",")
    population = fields[1]

    if population == "NV":
        num_nv += 1
    elif population == "CA":
        num_ca += 1
    elif population == "OR":
        num_or += 1

print(f"Nevada samples: {num_nv}")
print(f"California samples: {num_ca}")
print(f"Oregon samples: {num_or}")
```

#### B. Save sample names containing more than 6 characters.

```python
long_sample_names = []

for record in samples:
    fields = record.split(",")
    sample = fields[0]

    if len(sample) > 6:
        long_sample_names.append(sample)

print(f"Long sample names: {long_sample_names}")
print(f"Number of long sample names: {len(long_sample_names)}")
```

#### C. Create a list containing the GC content of every sample.

```python
gc_values = []

for record in samples:
    fields = record.split(",")
    dna_seq = fields[2]

    num_g = dna_seq.count("G")
    num_c = dna_seq.count("C")
    gc_content = (num_g + num_c) / len(dna_seq)

    gc_values.append(gc_content)

print(f"GC values: {gc_values}")
```

#### D. Count how many values in `gc_values` are greater than or equal to 0.50.

```python
high_gc = 0

for value in gc_values:
    if value >= 0.50:
        high_gc += 1

print(f"Number with GC content >= 0.50: {high_gc}")
```

#### E. Explain why saving calculated values in a list can be useful.

One appropriate answer would be:

```python
# Saving calculated values in a list lets us reuse those results for
# additional analyses without repeating the original parsing and calculations.
```
