# Linux primer 4

## topics to cover

- $PATH
- line endings
- advanced text processing tools (`sed`, `awk`)
- Shell scripts: loops
- From Haddock and Dunn: Chapters 6 and 16
- Bradnam and Korf primer through U45


## 1. $PATH      
This is an environment variable that lists the location of directories storing executables on `Unix` and `Linux` systems. See for yourself:
```bash
$ echo $PATH
```
The `/bin`, `/usr/bin`, and `/usr/local/bin` directories are normally part of the `$PATH` environment variable, but different users may have different directories listed in `$PATH` depending on system and user preferences. Executables that are in `$PATH` directories can be called from any location in your file system with out specifying their location.

In this class, you can store your scripts however you want. You can put them in a directory that you add to `$PATH`, and then you call them from anywhere without providing location information. 

**IF** you want to store executable scripts in a directory you add to `$PATH`, two steps are necessary. First, you must convert such scripts to executable.
```bash
$ chmod u+x mac2unix.sh
```
Second, you need to add the script to the directory you store such scripts in to `$PATH`. If you follow the suggestion of Haddock and Dunn (pg. 87), create a scripts directory (~/scripts/ for e.g.) within your home directory and add that to `$PATH` by adding the below line to `.bash_profile`, `.profile`, or `.zhsrc`:
```bash
$ export PATH="$PATH:$HOME/scripts"
```
Once you have done the above, you can call such scripts from the command line simply by typing them from the prompt:
```bash
$ mac2unix.sh filewithMAClineending.txt
```
For this course, we don't actually suggest doing this because you will be constantly altering scripts, and they may be more effectively stored in the directories where you are organizing your learning and course projects. In this case, you can simply call them with their absolute or relative paths (regardless of whether you want to change them to executable).

For e.g, if you wrote a script, `mac2unix.sh`, and stored it in `~/Documents/BIOL792/week4/`, you could call it directly if you were working in that directory:

```bash
$ zsh mac2unix.sh filewithMAClineending.txt 
```
Or simply call by completing its path to apply it in a different directory:

```bash
$ zsh ~/Documents/BIOL792/week4/mac2unix.sh filewithMAClineending.txt
```
## 2. Line endings revisited, text processing commands (`tr`)

As `Linux` commands, and many scripting languages, often entail processing one line at a time, line ending format really matters.  Because much of what you do in Linux, Perl, or Python will process text one line at a time, you will find that improper line endings will often cause problems. So how can we recognize when files have the wrong line endings?

As Unix commands, and many scripting languages, often process text **one line at a time**, line ending format really matters.  

- **Unix/Linux**: `\n` (newline)  
- **Mac**: `\r` (carriage return)  
- **Windows**: `\r\n` (carriage return + newline)  

For working in a Linux environment, files ideally need to use `\n` line endings. Improper line endings often cause problems in Linux, Python, and other bioinformatics tools written in the data science or genomics communities.

The quickest way to check what kind of line endings a file has is with the `file` command:

```bash
$ file grouse_barcodes.csv
```

### example: Mac line endings

Take a look at `grouse_barcodes.csv` in the github repository for this week . This file should contain three columns of information seperated by commas, but you'll notice that all of the information appears on a single line, and the highlighted symbol `^M` exists where line endings should. Here, the symbol `^M` represents every time a Mac carriage return (`\r`)exists in the file. There are multiple ways that you could easily change the line endings.

You could open the file in `bbEdit`, `VScode` or a similar editor to manually change line endings. Alternatively, and more efficiently, we can use `tr`, a transliterator function. You can think of `tr` as a find and replace command, where you specify a match to find (which can be specific, or a flexible regular expression) and 2) some replacement text. Check out the `man` page for `tr` before moving forward. 

Try changing the line endings of `grouse_barcodes.csv` using `tr`, and use `less` to confirm that it worked. In the command below, the first text in quotes designates the match to find, and the second represents the replacement text. In this case, we are finding Mac line endings (`\r`) and replacing them with Unix line endings (`\n`). We use `cat` to send the file contents to stdout, and then pipe that into the `tr` command.

```bash
$ cat grouse_barcodes.csv | tr '\r' '\n' > grouse_barcodes_unix.csv
```
Equivalently (using `>` and `<` instead of `cat` and `|`):
```bash
$ tr '\r' '\n' < grouse_barcodes.csv > grouse_barcodes_unix.csv
```
### Example: Windows line endings (\r\n)

Files created on Windows generally use both carriage return and newline characters. In Linux, these may show up as ^M characters at the end of every line.

To convert Windows-style line endings (\r\n) to Linux-style (\n), you can run:

```bash
$ tr '\r\n' '\n' < windows_file.txt > unix_file.txt
```
or (the `-d` option is for delete):

```bash
$ tr -d '\r' < windows_file.txt > unix_file.txt
```

There are also dedicated tools like `dos2unix` and `unix2dos` (installable with `apt` or `brew`) that automate these conversions. But `tr` works universally and is worth learning as it can be generally applied to many instances where you need to replace one character with another.

## 3. Substituting and editing with `sed`

`sed` (**S**tream **ED**itor) is a tool for making automated edits to text, one line at a time. It is extremely useful when you need to search, replace, or delete patterns across large files without opening them in an editor. `sed` reads input line by line, applies the edits you specify, and writes the results to STDOUT (or to a file if you redirect).


### Basic substitution

Let’s start with the simplest use of `sed` to replace one pattern with another, using the file `steinbeck.txt` that you can find in the `week4` directory:


We could replace instances of "he" with "John" using:

```bash
$ sed "s/he/John/" steinbeck.txt
```

Note: `sed` is literal unless told otherwise — so this command also turns `The` into `TJohn` and   `where` into `wJohnre`.

- `s` = substitute  
- `he` = pattern to match  
- `John` = replacement  
- no flags = replace **first match** on each line only  

To replace **all matches** on each line, add the `g` (global) flag:
```bash
$ sed "s/he/John/g" steinbeck.txt
```
A few things to notice here is that wherever "he" occurs, it will be replaced. So, "The" is altered to "TJohn", `where` is altered to wJohnre`, etc.

### Chaining commands

Let's explore this command some more with `grouse_bams.txt`, which contains a simple list of file names from a DNA sequencing project. You'll notice that information is separated by both underscores and periods. The important information in this file lies between the first underscore and the first period (e.g., `CO_HC_20`), as this code represents the individual's geographic region (e.g., `CO`), the individual's population (e.g., `HC`), and the individual's  id number (e.g., `20`). Let's first use `sed` to delete the extra text that we might not care about. Since we need to remove different parts (`aln_` and `.sorted.bam`), we can to use a `|` in our command. Also, since periods are special characters in this case, we will need to escape them using a `\` in our substitution statement.
```bash
$ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" > grouse_ids.txt
```
 Try adding another `sed` command to the command above that replaces underscores with commas:
```bash
$ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" | sed "s/_/,/" 
```
You'll notice that only one underscore was replaced. This is because `sed` only replaces the first instance of the match on each line unless you tell it otherwise. In order for you to find and replace all matches on a line, you will need to add the `g` global flag:
```bash

$ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" | sed "s/_/,/g" 
```

### Multiple edits in one command

Instead of piping many sed commands, you can use the -e option:
The above examples pipe full `sed` commands into each other. A quicker way to execute multiple `sed` commands is to use the `-e` option:

```bash
$ sed -e "s/aln_//" -e "s/\.sorted\.bam//" -e "s/_/,/g" grouse_bams.txt
```
### Beyond substitution: deleting and printing

- delete lines matching a pattern:
```bash
sed "/^#/d" file.txt
```

- print only lines that match a pattern:
```bash
sed -n "/HC/p" grouse_bams.txt
```
These examples show that `sed` isn’t just for replacing text — it’s a general stream editor for filtering and rewriting lines.

### Extra resources for learning sed

- [geeks for geeks sed tutorial](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)

- [grymoire sed tutorial](https://www.grymoire.com/Unix/Sed.html#uh-13)

## 4. `Awk`: a text engine with a ton of flexibility

`awk` isn’t just another `Unix` command — it’s essentially its own small programming language, designed for scanning and processing text line by line. It’s incredibly powerful for selecting, reformatting, and summarizing text data. Entire books are written about `awk`, but here we’ll introduce just a few essentials using the `grouse_ids.txt` file from above.



### Printing text

Most basically, you can print out the entire contents of a file:
```bash
$ awk {'print'} grouse_ids.txt
```
### Printing columns

`awk` splits each line into fields based on a delimiter (default is whitespace/tab). Fields are referenced as `$1`, `$2`, `$3`, etc.

Example: print only the 1st and 2nd fields, using underscore as the delimiter
```bash
$ awk -F "_" {'print $1,$2'} grouse_ids.txt
```
 `NOTE`: the default delimiter for `awk` is a tab, so you will have to specify an underscore as a delimitor below (using -F).

By default, the output field separator is a single space. You can change it with OFS:
```bash
$ awk -F "_" 'BEGIN {OFS = "_"} {print $1,$2}' grouse_ids.txt
```
### Reordering and formatting

You can rearrange fields, or add formatting. Example: print the individual ID followed by the geographic region, separated by a colon:
```bash
$ awk -F "_" 'BEGIN {OFS = ":"} {print $3,$1}' grouse_ids.txt
```
### Filtering with regular expressions

You can include only lines that match a pattern. For example, to list populations that include individuals with HC in their ID (using `//`):

```bash
$ awk -F "_" 'BEGIN {OFS = "_"} /HC/ {print $1,$2}' grouse_ids.txt
```
There are a ton of additional tasks that you can accomplish with `awk`, and we encourage you to explore those on your own. 

### More useful tricks

- Line numbering with NR (Number of Record):
```bash
$ awk '{print NR, $0}' grouse_ids.txt
```
- Summing a column of numbers (imagine the second column is numeric):
```bash
$ awk '{sum += $2} END {print sum}' some_data.txt
```

- Printing only lines where a column matches a condition:
```bash
awk -F "," '$3 > 100 {print $1, $3}' data.csv
```
- Counting how many times each value occurs (frequency table):

```bash
$ awk -F "_" '{counts[$2]++} END {for (val in counts) print val, counts[val]}' grouse_ids.txt

This builds a tally of how many individuals belong to each population code `($2)`.
```

## Extra resources for learning `awk`

[The Grymoire awk tutorial](https://www.grymoire.com/Unix/Awk.html)

[GNU awk user guide](https://www.gnu.org/software/gawk/manual/)

## 5. Turning useful `Linux` code into reusable shell scripts

At this point, you’ve learned that Unix commands can be chained together to do real work. But typing long commands over and over is inefficient. The real power of Unix comes from saving those commands into **shell scripts** — simple text files that the shell can execute like a program. Scripts let you automate tasks, enforce consistency, and scale up from one file to thousands with only a small change.

---

### Anatomy of a shell script

A shell script is just a text file with:

1. A **shebang** line (`#!/bin/zsh` or `#!/bin/bash`) that tells the system which shell to use.  
2. One or more Unix commands, just like you would type interactively.  
3. Optionally, placeholders (`$1`, `$2`, `$@`) that store arguments you pass on the command line.

---

### A simple example: converting line endings

Let’s write a script that replaces Mac-style `\r` line endings with Unix `\n` line endings. Save the following into a file called `mac2unix.sh`:

```bash
#!/bin/zsh
cat $1 | tr '\r' '\n' > u_$1
```

`$1` here stores a command line argument, which in this case should be a text file with mac line endings. This will pipe the contents of that file to `tr` to replace `\r` with `\n` (thus replace mac with unix line endings), and will redirect to a file which will be named "u" plus the argument stored in `$1`.
```bash
$ chmod u+x mac2unix.sh
$ ./mac2unix.sh grouse_barcodes.csv
```
Or, this could be executed more simply with:
```bash
$ zsh mac2unix.sh grouse_barcodes.csv
```
This will produce a file "u_grouse_barcodes.csv", which should have unix line endings.

## Scripts with multiple arguments and loops

The true payoff of scripting comes when you need to process many files. You don’t want to type a new command for each file. Instead, you can write a loop that applies the same logic to all inputs.

Let's say we wanted to write a script that would take any number of barcode files (as provided in week4 directory) and 1) create an ids file (e.g., `CO_HC_20`) and 2) create a pops file (e.g., `CO_HC`). We would use this to begin each sequencing project that we are working on and ensure that the format of the new files is the exact same each time. Start by creating a new script (`make_ids_and_pops.sh`) using `touch` and adding the header shebang line as above.

Before we begin adding commands to our script, we first need to think about the terminal command that we will eventually use to execute our script (don't type this now - you're script hasn't been made yet):

```bash
$ zsh make_ids_and_pops.sh *barcodes.csv
```
In this command, you are telling your computer to execute your script on every barcode file in the directory. `Unix` will then store the list of the different barcode file names as standard input (`STDIN`). The standard input will be stored in the `$@` special array, where you can easily access the file names. Let's start simple, and have the first line of code only print out the contents of `@`. Once you have added this line to a `make_ids_and_pops.sh` file that you created, run this as in the code box above.

```bash
    #!/bin/bash
    echo $@
```
You should see `colias_barcodes.csv grouse_barcodes.csv` printed to your screen. Each of the file names (called using `*barcodes.csv`) is  stored separately as a special object: the first file name is stored in `$1`, the second file name is stored in `$2`, and so on. We will not be directly using those objects in this script, but they can be very useful for other tasks. Update `make_ids_and_pops.sh` 
```bash
    #!/bin/bash
    echo $@
    echo $1
    echo $2
```
Because we want our script to be able to handle any number of input files, we need to include a simple loop that tells the script to do execute multiple commands for each input file. Loop syntax might seem abstract at first, but it will make more sense as you familiarize yourself and practice. Before specifying the commands to execute, we first need to specify which files we want the loop to work on. We will do this by typing `for bc in $@; do`. This means: for every filename that is listed in `$@`, do whatever I type next. You are probably wondering what `bc` stands for. It's simply a placeholder object that I created for the filenames that could have been named almost anything you wanted. I chose `bc` for barcode, but you could chose `file`, `barcode`, `input`, or anything else that makes sense to you. After this, we need to add the `Unix` commands that will create the new ids and pops files. Finally, you need to type `done` on the last line.

```bash
    #!/bin/bash
    echo $@
    echo $1
    echo $2
    for bc in $@; do
        cut -f 3 -d "," $bc | grep "_" &> $bc.ids.txt
        cut -f 3 -d "," $bc | grep "_" | cut -f 1,2 -d "_" &> $bc.pops.txt
    done
```

You'll see that instead of specifying a specific file for the first command in each `Linux` pipe, you are instead specifying `$bc`, which is the current file name that you are currently working on in the loop. Also, instead of being able to redirect the output using `>`, you instead must use `&>` to redirect the standard output to a new file. Finally, you might be wondering why `$bc` is listed as part of the output file names. Look at the names of your new files to see what this syntax is doing. What are the `grep` commands accomplishing?


### Running a loop directly from the command line

You don’t always need a saved script to use loops.  
Loops can be typed directly at the shell prompt and will execute immediately.  

For example, try this one-liner:

```bash
$ for i in 1 2 3 4 5; do echo "Iteration $i"; done
```
This prints:

```bash
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```
You can also loop over files in your directory. For instance, if you had several .txt files:

```bash
for f in *.txt; do echo "Working on $f"; head -n 1 $f; done
```
### More demonstrations and examples for scripting with loops and arguments

To get more comfortable with scripting, here are a few additional short examples you can try. These show how loops and arguments work in ways that are easy to see and understand.

### Looping with numbers

You don’t always need files, loops can just run a command multiple times.  

```bash
$ for i in {1..5}; do echo "Number $i"; done
```

This should print:

```
Number 1
Number 2
Number 3
Number 4
Number 5
```
### Looping with wildcards (files)

You can loop over filenames that match a pattern (e.g., *.csv or *.txt).

```bash
for f in *.csv; do echo "File: $f"; done
```
The shell expands `*.csv` into all `.csv` files in your directory, and the loop runs once for each file.

### Using arguments $1 and $2

Scripts can behave differently depending on the arguments you pass. Here’s a tiny calculator that adds two numbers:

```bash
#!/bin/zsh
echo "The sum is: $(($1 + $2))"
```
Save this as `sum.sh`, and run:

```bash
zsh sum.sh 4 7
```

output should be:

```bash
The sum is: 11
```

### Adding progress messages

You can use `echo` inside loops to keep track of what’s happening.
```bash

#!/bin/zsh
for f in *.fastq; do
    echo "Counting reads in $f..."
    grep -c "^@" $f
done
```

This prints both the file name and the read count, so you know what’s happening as the script runs.

## Additional potentially useful resources to get started on bash scripting

- [free code camp tutorial](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/)

- [hostinger](https://www.hostinger.com/tutorials/bash-scripting-tutorial)

- [geeks for geeks](https://www.geeksforgeeks.org/bash-scripting-introduction-to-bash-and-bash-scripting/)





