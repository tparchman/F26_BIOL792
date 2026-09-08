# Unix assignment 3

## Concepts/Tools: 
- `split`, `cat`
- pipes, redirection
- interacting with remote locations (`curl`, `wget`)
- moving large batches of files (understanding `rsync`)


## Files needed from course website:
- sample_passerina.fastq.gz (as last week)
- yeast_genome.gff

<p>&nbsp;</p>

## 1. Some additional quick file manipulations tricks

Lets go back to the `sample_passerina.fastq` file you were working with last week (Remember when you download from the Github repository, it will be compressed, and will need decompressing with `gunzip`).

**1.A** Lets say we need to split the big file into many smaller files to run parallel jobs on an HPC cluster. Use `split` to “split” `sample_passerina.fastq` into smaller files that each have 1000 lines. How would you accomplish the opposite problem, that is how would you put these files back together? Notice how `split` names files by default if not specified. Have a look at the `man` pages for `split` and `cat` to figure this out (the first command will use `split`, the second will use `cat`).

Try:

    split -l 1000 sample_passerina.fastq chunk_

Notice how split names files by default if not specified (chunk_aa, chunk_ab, etc.).

How would you accomplish the opposite problem, that is how would you put these files back together?

Try:

    cat chunk_* > recombined.fastq

**1.B** Instead, we might want to just extract the first 4000 lines of sample_passerina.fastq. Look at the `man` page for `head` (or ask chatGPT), and figure out how to do this as well as what you may be able to use `head` for more generally.


Try:
```zsh
head -n 4000 sample_passerina.fastq > first4000.fastq
```

<p>&nbsp;</p>

## 2. Pipes ("|"): moving **stdout** from one command into another.

Decompress (using `gunzip`) sample_passerina.fastq.gz and try each of the commands below, striving to understand what each is doing. The sections in Haddock and Dunn, or the regular expression cheat sheat under [unix resources](https://github.com/tparchman/F22_BIOL792_coursepage/tree/main/unix_resources) on the github page, will help you understand what `^` and `[ ]` mean for regular expressions. In addition, you will want to learn what the `tr` command does.

    grep ^@ sample_passerina.fastq | wc -l   

    grep ^@ sample_passerina.fastq | grep “NVP_CY_48147” > NVP_CY.txt

    grep ^[ATCG] sample_passerina.fastq | wc -l

    grep ^[ATCG] sample_passerina.fastq | tr ‘T’ ‘U’ | less

    grep ^[ATCG] sample_passerina.fastq | tr ‘T’ ‘U’ | head –n 20 > first20seqs_transliterated.txt

    grep ^@ sample_passerina.fastq | sort | uniq -c

<p>&nbsp;</p>

**2.A**. use `wget` (or similar) to download **yeast_genome.gff** from the [github site](https://github.com/tparchman/F25_BIOL792/blob/main/week3_unixIII/yeast_genome.gff) directly to your current working directory. 

Note, fastest way to do this would be right click on `raw` and copy link to raw data. Try:

    wget "https://github.com/tparchman/F25_BIOL792/raw/refs/heads/main/week3_unixIII/yeast_genome.gff"

    
GFF file format is used extensively in bioinformatics to store information on genomic features. This file has information on transcripts from a yeast genome. The third field in each row of this file has a description of the ‘feature’ of DNA sequence to which a region belongs. Example categories would be centromere, gene, intron, and tRNA.
<p>&nbsp;</p>

### Complete each task below, using linux commands and pipes where ideal.

**2.B** Use pipes to connect commands in order  to 1. grab the information for transcripts on chrIII, 2. Grab only the first 100 of these, 3. grab the “feature” field, and 4. Write to a file. (try a combination of `grep`, `head`, `cut`, and `>`)

    grep "chrIII" yeast_genome.gff | head -n 100 | cut -f3 > chrIII_features.txt

**2.C** Come up with a command to output the information for sequences on chromosome III that represent CDS. (try `grep`, with or without `|`)

    $

**2.D** Write out a file that lists in sorted order, all of the unique feature categories in yeast_genome.gff. Details on the commands sort and uniq can be found in the book or in man pages. (try `cut`, `sort`, `uniq`)

    $


<p>&nbsp;</p>

## 3. Moving and syncing files and directories: backing up your work (or your entire system)


`rsync` is a tool that can be used to sync directories, copy directories, update directories, etc. Read up on `rsync`, and pay careful attention to the command line options. In the simplest sense it works like copying and pasting a directory using the finder or windows explorer, but many times faster and with many options for specifications. Anytime you move large files or directories while working on computing clusters you will make heavy use of `rsync`.

With more detailed command line options, rsync can be used to sync two directories exactly.
	
**3.A.** Make a directory called `rsync_test` in your BIOL792 directory (or another directory of your choice). In that directory make two directories (for convenience, name them `dirsource` and `dirdestination`). Start by putting some files in the `dirsource` directory (maybe just 3 files), or just using `touch` to create some empty files.

**3.B.** Copy the dirsource directory from one location to another, rename the copied directory. Note that whether or not you follow the directory name with a `/` will have a big effect on how this works. Specifically, if you run:
 
    $ rsync –av dirsource/ ~/Desktop

The files within dirsource will be put into the desktop directory (not inside of a dirsource directory though).

If you run:

    $ rsync –av dirsource ~/Desktop

The dirsource directory will be copied to the Deskop directory.


**3.C.** Go into the dirsource directory and delete one of the files. Use `rsync` so that dirdestination mirrors dirsource. That is, so the file deleted in dirsource is now deleted in dirdestination. This will require you understanding how the `–-delete` command works.
	
    $

## 4. Writing useful shell scripts.

Here you will write a bash script for rapidly syncing your working files from a certain directory (or perhaps your entire home directory) to a flash or backup drive. This will require you to understand how to write a shell script, and how to use `rsync` (pay special attention to the delete option). The end point of this assignment should be a script that you can run from the terminal that accomplishes this job merely by typing the name of the shell and the program. You will only need two lines within the script. One will be `#!/bin/zsh` and one will be your `rsync` command. Your script should be runnable from the command line by either specifying `zsh` as the interpreter: 

	e.g., $ zsh sync_laptop.sh

or by turning the script into an executable

    $ chmod a+x sync_laptop.sh
    $ ./sync_laptop.sh


For now, lets specifically write a program that syncs your BIOL792 directory (or some other directory you would like to usefully backup) with the same directory that you have created on either a flash drive, or an external hard drive at home. This program should result in the directory on your drive being updated to look exactly like the BIOL792 directory on your laptop. That is **new files should be added to the destination directory and files you deleted from your laptop should be removed from the drive as well**. When the program is done, it should print to the screen “Your work is now backed up” or something like this. You can look at slides from class to get more hints on how to do this.

Once you have tested this and are absolutely sure it is working the way you want, you could use the basic structure of the script to back up your entire home directory (or your entire computer) to a drive. 


---

# Assignment 3 command summary 

| Command | Purpose | Example |
|---------|----------|---------|
| `split` | Split a large file into smaller parts | `split -l 1000 bigfile.txt chunk_` |
| `cat` | Concatenate files together | `cat chunk_* > combined.txt` |
| `head` | View the first *n* lines of a file | `head -n 4000 sample.fastq` |
| `tail` | View the last *n* lines of a file | `tail -n 100 sample.fastq` |
| `grep` | Search for matching text patterns | `grep "chrIII" yeast_genome.gff` |
| `tr` | Translate or replace characters | `tr 'T' 'U' < seqs.txt` |
| `sort` | Sort lines alphabetically or numerically | `sort yeast_genome.gff` |
| `uniq` | Filter out duplicate lines (usually after `sort`) | `sort features.txt \| uniq` |
| `cut` | Extract specific columns from text (tab-delimited) | `cut -f3 yeast_genome.gff` |
| `wc` | Count lines, words, or characters | `grep ^@ sample.fastq \| wc -l` |
| `rsync` | Copy or sync directories efficiently | `rsync -av source/ dest/` |
| `rsync --delete` | Sync directories and delete files removed from source | `rsync -av --delete source/ dest/` |
| `curl` | Download data from a URL | `curl -O http://.../file.fasta` |
| `wget` | Alternative tool for downloading files | `wget http://.../file.fasta` |

---

**Tip:** Use `man <command>` or `<command> --help` to read the manual and see more options for any of these tools. OR, ask chatGPT to demonstrate the functionality you desire from a specific command, or combination of commands.
