
# Linux primer 3

## topics to cover

- process control revisited
- more on removing directories and files
- copying directories, moving batches of files
- permissions, file modes
- pipes (`|`) and redirection (`>`,`>>`)
- Interacting with remote machines
- quickstart introduction to writing and executing shell scripts


<p>&nbsp;</p>

**Update on pulling course materials from github**

In the week 1 primer, I gave you a line of code to clone the full course directory from github. The code below will clone and pull the full directory tree and all of its contents.

```bash
git clone https://github.com/tparchman/F26_BIOL792
```
As we progress each week, I will add new material and update existing material. The best way to keep your local copy up to date is to use `git pull`. This will download new files and directories that I have added to GitHub and update course files that I have changed, while preserving new files that you have created locally.

First, move into the course directory:

```bash
cd path/to/course_directory
```
Then pull the latest version from GitHub:

```bash
git pull
```
You can check the status of your local repository at any time with:

```bash
git status
```

## 1. Process monitoring with `top`, `htop` and `ps`, running jobs in the background, killing jobs
`top` or `htop` will display information on processes running on the machine you are logged into.  Doesn't matter what directory you call it from.

```bash
$ top
```

`htop` will display information in a more readable and interactive format

```bash
$ htop
```

`ps aux` (-a -u -x) will show all active processes. 

```bash
$ ps aux
```

`ps aux | grep [search expression]` will pipe processes listed as above into `grep`, and can be used to locate PIDs for specific applications.

```bash
$ ps aux | grep firefox-bin
```

If you have mutliple processes running, and want to kill one, use `kill` followed by the process ID, which you can locate with `top` or `ps`, e.g.:

```bash
$ kill 9031
```

### Running jobs in the background

If you have a job running in the shell that is not doing what you want, you can kill from the terminal with "ctrl c". You can also temporarily kill with "ctrl z", and then restart it in the background with `bg` typed at the prompt with no additional arguments necessary. Try this out, it will be useful in the future.

If you are calling a command that is going to take some time, and you dont want it to occupy the shell you are working in, you can send it to the background with `&`. Once a job is running in the background, the job will continue once you close the terminal session or exit your connection to a remote server. The below command would take all files ending in fastq from within the current directory and concatenate them into one much larger file.

```bash
$ cat *fastq > allgenomefiles.fastq &
```

Especially useful if you are working on a remote server and want to disconnect, `nohup`, short for no hang up, is a more secure command that keeps processes running even after exiting the terminal. Nohup prevents the processes or jobs from receiving the SIGHUP (Signal Hang UP) signal, which is sent to a process upon closing or exiting the terminal. 

To use `nohup`:

```bash
$ nohup <command> <argument>
```

To use nohup with something that you want to put in the background:

```bash
$ nohup ping google.com &
```

Note, if you try the above, you machine will `ping` google.com repeatedly. To look the job up, and then kill, see below. Note that `pgrep` is an alternative way to look up some types of jobs that returns only the process number. Thus, it gives less information than `ps aux`, but is more streamlined and simple.  `ps aux` returns the full command line of each process, while `pgrep` only looks at the names of the executables.

```bash
$ pgrep -a ping
$ kill 20397
```
## Practice running a program, running it in the background, and killing it 

This is a repeat from last weeks assignment, but putting it here anyway, and adding some detail to play with `ps aux` and `pgrep`
`jot`  can generate strings of numbers, among other things (have a look at the `jot` `man` page). Try the following command which will print 100 random numbers:

```bash
$ jot -r 100
```

Now, increase the number of random numbers until you get to a number of replicates (think millions or more) that takes your computer an appreciable amount of time to complete. If you made the number large enough, you’ll notice that you can’t do anything else with your Terminal window while it’s busy. Use `ctl c` to stop it, and then execute the commands again with an “&” at the end:

```bash
$ jot -r 1000000000 > test.txt &
```

The ampersand (&) will cause the job to run in the background, you will have the normal prompt back in your terminal window, and closing it will not affect the job.  

You can use `top` or `ps` or `pgrep` to identify the process number of the `jot` job in oder to kill it. You could more efficiently pipe the output from `ps aux` into a grep search for `jot` to return the PID of the job running in the background:

```bash
$ ps aux | grep jot
```

OR

```bash
$ pgrep -a jot
```

After you identify the job id (e.g., 77654), you can kill it:

```bash
$ kill 77564
```

<p>&nbsp;</p>

Keep in mind that if you are using `jot` and redirecting to a file, you may use significant disc space. So, be sure to delete the files you make.

If you dont want to generate output, you could alternatively experiment with running jobs in the background using `sleep`. `sleep` is a convenient way to experiment with processes because it simply tells the computer to wait for a specified amount of time. Below will activate sleep for 1 hour.

```bash
$ sleep 1h
```
Remember, you can kill an active terminal job using 

```bash
$ ctrl c
```

You can run in the background using `&` or `nohup`. Here we are going to start multiple sleep jobs so that you can find and destroy each:

```bash
$ nohup sleep 1h &
$ nohup sleep 2h &
$ nohup sleep 3h &
```
One way you could find PIDs is to use `htop` to look around. Once you are in `htop`, you can open search capability by typing `/` and then type `sleep`. The lines with your jobs will then be highlighted, and the PID will be on the left. To leave `htop`, hit `q`.

More efficiently, you can quickly list PIDs using `pgrep`

```bash 
$ pgrep -a sleep
```

Jobs can then be killed using `kill` and the PID, for example:

```bash
$ kill 94234
```
## 2. Removing directories and files revisited (and note of caution).

Once you changed your .bash_profile file to invoke the `-i` option, the shell should ask if you are sure you want to delete or overwrite files after using `rm`, `rmdir`, `cp`, or `mv`. *Please make certain that you have this working correctly so you dont inadvertently destroy things.* 

Things should look as below:

```bash
$ rm british_PCA.jpg 

remove british_PCA.jpg? 

```

If you are in a hurry, you can override the -i option, but be VERY careful before doing this regularly.

```bash
$ rm -f british_PCA.jpg
```

### Understanding the **danger** of `rm -rf`  

The `rm` command permanently **removes files and directories** from your system. Unlike moving something to the Trash/Recycle Bin, once you run `rm`, the files are gone immediately and cannot be restored with a simple undo. We updated your profile file with an alias that causes `rm` to be interpretted from the shell as `rm -i`, to protect you against accidentally making a mistake with `rm`. With several command line options, you can override this protection, and even make `rm` more dangerous.

- `rm` = remove  
- `-r` = recursive → go into directories and delete **everything inside them**  
- `-f` = force → do not ask for confirmation, even for write-protected files  

So, `rm -rf` means:  
**“Delete everything in this location, including all subfolders, without asking me first.”**

### Why this is dangerous  
- Running `rm -rf` in the wrong place (e.g., your home directory, or `/`) can wipe out your entire system in seconds.  
- There is **no warning** and no way to recover the files without backups.  
- A small typo in the path can destroy important data.  

### Safer practice  
- Use interactive mode (`rm -i`) so the system asks before deleting each file.  
- Double-check your current directory with `pwd` before running `rm`.  
- For students, it’s a good habit to replace `rm` with a safer alias. We have already done this, but just a reminder here to put this in context.  

```bash
alias rm="rm -i"
```
Be sure to understand that this alias behavior **will be overriden if you use `rm -rf`**

But often, using the dangerous version of `rm` will be necessary to do things efficiently. After all, being more efficient in life is why you are learning Linux. 

As an example, lets say you used poor code to write 600 .txt files to a directory, and you want to clean up those files before fixing your python code. To remove them all, without being prompted with "remove N.txt?" for each file consecutively, you can execute `rm` with the the additional arguments `-r` (removes file heirarchy recursively, meaning it will remove directories and all within) and `-f` (without prompting for confirmation). This is the most dangerous Linux command, with no second chances, so use with **extreme caution**. 

The below command will remove, instantly without second chances, forever, every file in the working directory that ends in txt. To repeat, **extreme caution**. Below a wildcard character is used to match anything that ends in txt, but you can specify any number of things, which makes `rm -rf` a dangerous thing.

```bash
$ rm -rf *txt
```


Because the above command is dangerous (you could accidentally delete more than you wish). Always test such wildcard (`*`) commands with `ls` first, eg:

```bash
$ ls *txt
```
<p>&nbsp;</p>

## 3. Pipes (`|`) and redirection (>, >>, 2>)

**A. Pipes**, called with the `|`, are used to send stdout from a command directly as input into another. Lets say you have DNA sequence data from a large number of individuals, all in separate .fastq files, in a project directory. To be sure of your sample size, you want to count the number of files in that directory. `ls` normally sends directory content, one line at a time, to stdout. Here we are piping that output directly into `wc -l` which will count the number of lines, which will represent the number of files.

    $ ls | wc -l

Here are some examples from the files you played with last week under `GitHub/F23_BIOL792/week2_UnixII`:

Counting the number of records in yeast_genome.gff that are on chrI (chromosome 1):

    $ grep "chrI" yeast_genome.gff | wc -l

The below commands extract the third field (which describes genomic feature), then sorts the output, then prints to STDOUT the unique items in the sorted list.

    $ cut -f 3 yeast_genome.gff | sort | uniq

The below command is useful for counting the number of active processes a given user has on a Linux system.

    $ ps aux | grep parchman | wc -l

Pipes are obviously useful to send output from one Unix command to another, yet the above examples only use a single `|`. In fact, many bioinformatic "pipelines" are actually built from strings on unix commands piped into one another. The example below does something real and useful:

    $ samtools mpileup -P ILLUMINA --BCF --max-depth 100 --adjust-MQ 50 --min-BQ 18 --min-MQ 18 --skip-indels --output-tags DP,AD --fasta-ref buckwheat_ref.fasta aln*sorted.bam | bcftools call -m --variants-only --format-fields GQ --skip-variants indels | bcftools filter --set-GTs . -i 'QUAL > 19 && FMT/GQ >9' | bcftools view -m 2 -M 2 -v snps --apply-filter "PASS" --output-type v --output-file variants_rawfiltered_12JULY18.vcf  &

**B. Standard output, standard error, and redirecting output**

Most Linux commands produce one or both of two types of output:

**Standard output (`stdout`)** - the normal output produced by a command.

**Standard error (`stderr`)** - error messages and warnings.

By default, both are printed to your terminal. We can instead **redirect** them to files.

`>` redirects standard output to a file:

```bash
$ grep "gene" yeast_genome.gff > genes.txt
```

This writes the output from `grep` to `genes.txt` instead of printing it to the screen. **Be careful:** if `genes.txt` already exists, `>` will overwrite it.

`>>` also redirects standard output, but **appends** it to the end of an existing file rather than overwriting it:

```bash
$ grep "exon" yeast_genome.gff >> genes.txt
```

`2>` redirects **standard error** to a file:

```bash
$ some_command 2> errors.txt
```

This can be particularly useful when running long analyses, because normal output and error messages can be saved separately:

```bash
$ python analysis.py > output.txt 2> errors.txt
```

A quick way to remember these:

| Syntax | What it does |
|---|---|
| `>` | Redirect `stdout`; overwrite file |
| `>>` | Redirect `stdout`; append to file |
| `2>` | Redirect `stderr`; overwrite file |

These can also be combined with background jobs. For example:

```bash
$ nohup python analysis.py > output.txt 2> errors.txt &
```

This runs `analysis.py` in the background, keeps it running after you disconnect, and saves its normal output and error messages to separate files.

<p>&nbsp;</p>

## 4. Copying and mirroring directories within and among Linux systems: `rsync`

Use `man` to have a look at the capabilities of `rsync`, or better yet, ask chatGPT to summarize its most common and useful iterations. This is a versatile and frequently used command for moving, copying, or mirroring directories. You will find yourself using this command to copy directories around your computers file system as well as to storage drives, remote servers, and high performance computing systems. We will learn how this works here in a few simple contexts, but guarantee you will find yourself using this often.

The basic use of `rysnc` might look like what you see below:

```bash
$ rsync -av source_directory/ destination_directory/
```

I like to use the command line arguments `-a` and `-v`, which invokes archive mode and increases verbosity. This will print information to the screen as copying proceeds. For more information on `rsync` review the manual page, or do some internet searches.

A couple of minor details control the placement of directories and their contents. In the above example, there is a trailing forward slash `/` on the source directory. This means the **contents** of `source_directory` will be written into `destination_directory`. I don’t like doing that often, as it can make a mess. The below example, without the trailing `/` on the source directory, will copy the directory itself (as a container) into the destination:

```bash
$ rsync -av source_directory destination_directory/
```

**NOTE on trailing `/`**:     Spend some time testing to be sure you understand the difference between using the trailing `/` and not when specifying the source directory. The trailing slash often causes confusion even among experienced users.

### Updating and Mirroring 

`rsync` is extremely useful for mirroring directory contents between computers, or for managing backups. For example, it can be used to copy the entire contents of your laptop to an external drive or remote server, but then used daily or weekly (or however often you like) to update a backup. While the first action may take a bit, once a version of the `source_directory/` exists within `destination_directory/`, the command below will only update `destination_directory/` to reflect changes in `source_directory/` since the last iteration of `rsync`. New and modified files will be copied. The `--delete` allows files that were deleted from source directory to be deleted from the destination_directory. Be cautious with this until you are completely comfortable to avoid potentially major mistakes with deleting things you don't want deleted.

    $ rsync -av --delete source_directory/ destination_directory/

### Important: `rsync --delete` can be destructive. Good idea to test before you run, and the `dry-run` command line option exists for this purpose.

This is how it works. Try it out with some small test directories, and work to understand the output.

```bash
$ rsync -av --dry-run source/ destination/
```

and then

```bash
$ rsync -av --delete --dry-run source/ destination/
```

### Copying across networks

One of the most common uses of rsync is moving data between computers, such as copying files to or from a remote server. When working with high performance computing (HPC) clusters or lab servers, the pattern looks like this:

    rsync -av local_directory/ username@remote.server.edu:/path/to/destination/

Or, pulling data back from the remote server to your laptop:

    rsync -av username@remote.server.edu:/path/to/source/ local_directory/

As long as you have SSH access to the server, rsync will securely copy files over the network. You can add options like --progress to watch the transfer speed and -z to compress during transfer (helpful for slower connections).

### Quick reference of common flags

- `-a` archive mode (preserve permissions, symbolic links, modification times, etc.)

- `-v` verbose (print what’s happening)

- `-z` compress file data during transfer

- `--progress` show progress during transfer

- `--delete` delete files in destination that no longer exist in source

As `rsync` is the most commonly used command to transfer files and directories around machines, and between machines and remote servers, there are lots of helpful tutorials out there. Below are a few

- [tecmint rsync tutorial](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)

- [linuxize rsync tutorial](https://linuxize.com/post/how-to-use-rsync-for-local-and-remote-data-transfer-and-synchronization/)
<p>&nbsp;</p>

**NOTE** to get `curl` and `wget` to work on your system, you may need to use `brew`(Mac Unix) or `apt-get`

## 5. Permissions and file modes

As Unix systems are  multi-user, the control of permissions on directories and files is critical for security, privacy, and collaboration. Typing `ls -l` (or `ll` depending on how you modified your bash_profile) will show you the permissions associated with files in your current directory.

    $ ll -h

    -rw-rw-r--.  1 parchman parchman  51G Jul 25  2017 J1b.clean.fastq
    -rw-rw-r--.  1 parchman parchman  51G Jul 22  2017 J1.clean.fastq
    -rw-rw-r--.  1 parchman parchman  44G Jul 22  2017 J2a.clean.fastq
    -rw-rw-r--.  1 parchman parchman  44G Jul 22  2017 J2b.clean.fastq
  

 A glance at this output illustrates how permissions are displayed. 3 permissions are defined for each owner level (`user`, 'owner'; `g`, 'user group'; `o` 'other'), only the owner of a file or directory can change the permissions therein. The first position from the output above specifies file type, the following 3 have permissions for 'user', then three for 'group', then 3 for 'other'. Permission is indicated by the letters below, a lack of permission with a `-`.
- Read (`r`): Permission to open and read a file, for a directory allows the listing of content.

- Write (`w`) Permission to modify the contents of a file, or for a directory, to add, remove and rename files.

- Execute (`x`): Permission to run an executable program.


Here are some examples of symbolic notation:

- `-rwxr--r--`: 'User' has read/write/execute permission, 'group' and 'other' have only read permissions.
- `drw-rw-r--`: A directory where 'user' and 'group' have read and write permissions, while 'other' has only read.
- `-rwxr-xr-x`: A file, 'user' has read/write/execute, 'group' has read/execute, and 'other' has execute.

The `chmod` command is used to alter permissions. The command can be controlled by either numeric or symbolic codes, the latter are illustrated below. You can find useful guides to the numeric system [here](https://gist.github.com/juanarbol/c44e736be70279c1fd5d68aa24f9d8be).

| Operator | Action/level |
|----------|--------|
|  +        | Add     |
|  -       | Remove  |
|  =       | sets permission|
|  r        | read    |
|  w       | write  |
|  x       | execute|  

<p>&nbsp;</p>

  
| Abbreviation | User level |
|----------|--------|
| u      | User     |
| g       | Group  |
| o       | Other|
| a       | All|
<p>&nbsp;</p>

We are going to try to avoid messing with permissions too much in this course, but if you go on to use remote or cluster computing systems with other groups, understanding permissions in more detail is essential. There are, however, a few simple things we will do, and below are some examples. 

Convert the .sh shell script to an executable for all users.

    $ chmod a+x first_shell_script.sh

Convert the .sh shell script to write for all users.

    $ chmod a+w first_shell_script.sh

This script can then be executed from the currently directory:

    $ ./first_shell_script.sh
<p>&nbsp;</p>


## 6. Interacting with remote locations
<p>&nbsp;</p>

### Retrieving content from web addresses 
It is quite common to download files, or large batches of files, from web addresses or remote servers. 

### Example: Using `curl` to pull data from NCBI  

The `curl` command can be used to fetch biological data directly from online databases such as NCBI. For example, the command below retrieves the FASTA sequence of the human BRCA1 gene (accession **NM_007294.4**) from NCBI’s nucleotide database:

    curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_007294.4&rettype=fasta&retmode=text" -o BRCA1.fasta

What this does:

- `curl` fetches the data from the NCBI URL.

- The URL uses NCBI E-utilities (efetch) to query the nucleotide database (db=nuccore).

- id=NM_007294.4 specifies the sequence accession number.

- rettype=fasta and retmode=text tell NCBI to return the sequence in FASTA format.

- -o BRCA1.fasta saves the output into a file called BRCA1.fasta.

After running this command, you can inspect the file with:

    less BRCA1.fasta

`wget` is similarly useful, and similar to execute. The example below illustrates how you can pull files straight from the github repo to a current directory. To get the link right, click on a file on github, right click on `raw` and copy the link.

    $ wget "https://github.com/tparchman/F25_BIOL792/raw/refs/heads/main/week3_unixIII/yeast_genome.gff"


<p>&nbsp;</p>

### Connecting to remote servers and HPC (High Performance Computing) systems 

Two of the most common tools you will encounter when working with remote servers are **SSH** and **SFTP**.  

- **SSH (Secure Shell):** lets you log into another computer (like a lab server or HPC system) from your terminal, giving you a secure command-line session as if you were sitting at that machine. Once we start using `ssh` to connect to remote servers, you will want to revisit the section on **permissions** above.

```
ssh username@ponderosa.unr.biology
```

- **SFTP (Secure File Transfer Protocol):** uses the same secure connection but is designed for moving files back and forth between your computer and a remote system.  

Example (to start an SFTP session):
```
sftp username@server.university.edu
```
These tools are essential for working in research computing because they allow you to run code on powerful servers and transfer data safely. We will cover SSH and SFTP in much more detail later in the semester, when we start working with remote servers and high-performance computing systems. For now, it’s enough to know that they provide secure remote access and file transfer capabilities.  

<p>&nbsp;</p>

## 7. Writing shell scripts (we will build on this next week)

You’ve now learned how to run individual commands in the terminal. But what if you want to **save a sequence of commands** and run them all at once? This is where **shell scripting** comes in. 

Here we will Linux commands to learn to write your first simple programs. We will cover this quickly today, and come back for more next week.

We call scripts, or programs, that execute linux commands "shell" scripts because we are operating in the shell (bash or zsh) and using linux commands as the language. Simply put these are programs consisting of linux code and arguments that can be written to do simple or surprisingly complicated jobs.

- **When:** Use shell scripts when you need to repeat tasks, automate workflows, or keep a record of your commands so you can rerun them later.  
- **Where:** Shell scripts are just plain text files, usually saved with a `.sh` extension (e.g., `myscript.sh`). You can create them in any text editor.  
- **How:**  For this, our code will simply be written and stored in a text file. We will use the extension `.sh` rather than `.txt` to signify that this is a shell script. The first line of such a file (or program) is the `shebang` which tells the computer what interpreter to use.

    #!/bin/zsh

To warm up to this idea, lets just print something to screen here. Your bash script thus should have exactly what is below.


#!/bin/zsh 
    echo "Welcome the the Biggest Little City"

Save the file as something like first_shell.sh. Then, you can execute from the command line in one of two ways. One, you can simply type:

    $ zsh first_shell.sh

Two, you can change the file to executable, then run, as follows:

    $ chmod a+x first_shell.s
    $ ./firstbash.sh

I have added three simple shell scripts to the [week3](https://github.com/tparchman/F24_BIOL792/tree/main/week3_unixIII) directory on the course github page. Have a look at these, and play around with executing them ahead of next weeks meeting.


## Week 3 Command Cheat Sheet

| Command | Purpose | Example |
|---------|---------|---------|
| `top` | Monitor processes in real time | `top` |
| `htop` | Interactive, colorful process monitor (install separately) | `htop` |
| `ps aux` | List all running processes | `ps aux` |
| `ps aux \| grep <name>` | Search processes by keyword | `ps aux \| grep firefox` |
| `pgrep -a <name>` | Get process IDs (PIDs) by name | `pgrep -a ping` |
| `kill <PID>` | Kill a process by ID | `kill 9031` |
| `ctrl c` | Stop a running job in the foreground | *(keyboard shortcut)* |
| `ctrl z` + `bg` | Pause a job, then resume in the background | *(keyboard shortcut + command)* |
| `<command> &` | Run a job in the background | `cat *fastq > all.fastq &` |
| `nohup` | Keep jobs running after logout | `nohup ping google.com &` |
| `jot -r N` | Generate N random numbers (macOS/Unix) | `jot -r 100` |
| `rm` | Remove files (interactive if aliased) | `rm file.txt` |
| `rm -rf` | Dangerous: remove directories/files recursively & force | `rm -rf *txt` |
| `rmdir` | Remove an empty directory | `rmdir olddir` |
| `rsync -av` | Copy/sync directories with archive + verbose | `rsync -av src/ dest/` |
| `rsync -av --delete` | Sync directories exactly, removing extra files | `rsync -av --delete src/ dest/` |
| `rsync -av user@server:/src/ dest/` | Copy data to/from remote servers | `rsync -av data/ user@hpc.edu:/scratch/` |
| `ls -l` / `ll` | List files with permissions and details | `ls -l` |
| `chmod` | Change file permissions | `chmod a+x script.sh` |
| `grep` | Search text by pattern | `grep "chrI" yeast_genome.gff` |
| `cut -fN` | Extract a specific field (column) from tab-delimited file | `cut -f3 yeast_genome.gff` |
| `sort` | Sort text or numbers | `sort yeast_genome.gff` |
| `uniq` | Collapse duplicate lines | `cut -f3 yeast_genome.gff \| sort \| uniq` |
| `wc -l` | Count lines in a file or stream | `ls \| wc -l` |
| `curl` | Download from a web URL | `curl -O https://.../file.fasta` |
| `wget` | Alternative to curl for downloading files | `wget https://.../yeast_genome.gff` |
| `ssh user@server` | Securely log into a remote server | `ssh username@server.edu` |
| `sftp user@server` | Securely transfer files to/from remote server | `sftp username@server.edu` |
| `echo` | Print text to the screen | `echo "Hello world"` |
| `#!/bin/bash` / `#!/bin/zsh` | Shebang: first line of a shell script | *(placed at top of `.sh` file)* |
| `chmod a+x script.sh` | Make a script executable | `chmod a+x first_shell.sh` |
| `./script.sh` | Run an executable script | `./first_shell.sh` |

---

