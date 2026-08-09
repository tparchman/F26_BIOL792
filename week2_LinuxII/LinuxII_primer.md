# Linux primer 2

## Topics to cover

- `man` pages
- .zshrc, .bashrc, .bash_profile, etc.
- text viewing and in terminal text editors
- compression, decompression
- more Linux commands, redirection
- process monitoring
- package installation
- introduction to `grep`

- **Haddock and Dunn: last 5 pages of chapter 4; chapter 5.**
- **U10 through U27 in Bradnam and Korf primer (http://korflab.ucdavis.edu/Unix_and_Perl/current.html)**
<p>&nbsp;</p>

## 1. `man` pages and command line options
For any Linux command (there are many thousands) you can find the full information on that command by using  `man` (manual pages, essentially). We will get introduced to 15-25 commonly used Linux commands today, looking at `man` pages is one way to learn about the flexibility and various command line options.

For example:

    man pwd
will tell you what `pwd` does.

Try:

    man grep

Here you will see the information on grep displayed in a text viewer called `less`. You will use `less` frequently, so here are some keys to making it efficient:

* `spacebar` will scroll forward a page 
* `b` will scroll up a page
* `q` to exit less and regain the terminal prompt 
* `/` to search file for pattern. 
* when in pattern search mode, `n` skips to next match, `N` skips to previous match


Upon scrolling through the `grep` man page, you will see that `grep` has many command options and is a flexible, powerful, and commonly used text processing tool.


Most commands also have command line options, which are typed following a `-` after the command. Try `ls` below with the additional options h or l, which could be specified in either format shown below

    ls -l -h
    ls -lh

Notice that when you use `man`, all of the command line options will be clearly listed and efficiently described. Try the below for command line option explanations for `ls`. As a reminder, type `q` to exit the `less` viewer and to regain your terminal prompt.

    man ls

Online manual pages (e.g., [less man page](https://man7.org/linux/man-pages/man1/less.1.html)) and other sites are also plentiful to read up on Linux commands or if you are looking for guidance.

chatGPT and other chatbased AI platforms can be very valuable for summarizing the common uses, arguments, and command line options for any Linux command. While `man` pages are good for exploring all of the potential uses and options, AI assistance is your best bet for jumpstarting your understanding of the use of a specific command.


## 2. Terminal profile settings

You can can customize the way a command works from shell by creating an **alias**. For example, the below command will change things so that when you type `ls`, your terminal will call `ls -lh`

    alias ls = 'ls -lh'

When you do type a command such as above during a terminal session, it will only work from within that session. Once you get more comfortable in Linux, you will likely want to customize the behavior of your shell uniformly. This can easily be done by modifying a file, `.zshrc` (or depending on flavor ofLinux/Unix you are running: `.bashrc`, `.profile` or `.bash_profile`), that resides in your home directory. The `.` before the file names here renders them 'hidden'. Thus, to move to your home directory and look for these types of files use (note the -a option is shorthand for all, so it shows the hidden files as well):

    cd ~
    ls -a

If you are running a newer Mac OS, you are probably running the zsh terminal application. If so, `.zshrc` is the name of the profile file. If you are running an older Mac OS, or just prefer bash as a terminal application, the profile information will be stored in `.bash_profile` or `.bashrc`. If you are using a recent install of Ubuntu Linux you should also be using a zsh terminal. To change protections on your use of several dangerous Linux commands (`rm`, `mc`, and `cp` even), we are going to customize all of your profile files to include alias commands that add some protections. This will ensure that you do no overwrite important files or directories, and that you dont accidentally vaporize large amounts of stored data. If you already have a profile with alias control behavior that you like, great. Either way, we are going to add the alias commands below, or are going to have you replace your current `.zshrc` file with examples I have provided on the github page.

If you are not sure which shell you are running, the command below will tell you:

    echo $SHELL

For Mac Unix or PC Linux, you can change the default shell to `szh` as below:

    chsh -s $(which zsh)

The alias collection above has some useful features. `ll` and `ls`, when typed, will give you more complete, and/or more readable information. `rm`, `mv`, and `cp` have the `-i` option added, which is  HIGHLY recommended. This will change the behavior of `rm`, `mv`, or `cp` to always ask if you are sure you want to remove a file, or overwrite a file with the same name in terms of `cp` and `mv`.

### ### `oh my zsh`: an open source, community-driven framework for managing your zsh configuration.
Oh My Zsh makes the command line friendlier, safer, and more powerful. It adds features like syntax highlighting, auto-completion, and a customizable prompt that shows useful information (such as your current git branch). For students new to Linux/Unix, it reduces frustration by catching mistakes and making the shell more informative, while still teaching the fundamentals of command-line work.  

### Installing ohmyzsh

- Install `Ohmyzsh` **On Mac Unix**
```zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

- Install `Ohmyzsh` **On Ubuntu Linux**

```
#update apt
sudo apt update

#install zsh if it is not default terminal
sudo apt install zsh -y

#install ohmyzsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

#make zsh default
chsh -s $(which zsh)

```

### Useful Beginner Customizations  

- **Aliases for safety and convenience**:  
  ```zsh
  alias python='python3'
  alias ll='ls -laF'
  alias ls="ls -F"
  alias rm='rm -i'
  alias mv='mv -i'
  alias cp='cp -i'

- **Theme choice**: Start with `agnoster` (clear, informative) or `ys` (compact and clean). As you get more experience with ohmyzsh, you can change to any number of themes. Oh My Zsh comes with over 100 different themes, which control how your command prompt looks, from minimal styles that just show your directory, to colorful prompts that display git branches, timestamps, or system status. Exploring themes is a fun way to personalize your shell and make it easier to read. You can browse and preview all available themes here: [Oh My Zsh Theme Gallery](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes).  

- **Plugins**: Enable `git` (default), and optionally add `zsh-autosuggestions` and `zsh-syntax-highlighting` for real-time feedback.

- **Safer redirects**: Add `set -o noclobber` to prevent accidentally overwriting files with `>`.

If you are running Mac Unix, you are going to use `zshrc_eg_mac_ohmyzsh` that you can find on course github page under week2.

If you are running Ubuntu Linux, you are going to use `zshrc_eg_ubuntu` that you can find on course github page under week2.

Go to your home directory:

    cd ~

View hidden files:

    ls .*

Note the above option will show just files that begin with `.`. If you wanted to see all files, regardless of whether they start with `.` or not, you could use:

    ls -a

This will show you what hidden files you have, and you should be able to find profile files, which might look like `.zshrc` `.bashrc`, or `.bash_profile`.

Then copy the `zshrc_eg_mac_ohmyzsh` or `zshrc_eg_ubuntu` file to your home directory. E.g., from the week2 directory:

```zsh
cp zshrc_eg_mac_ohmyzsh ~
```

or 


```zsh
cp zshrc_eg_ubuntu ~
```
Change name of profile file on `Mac Unix`:

```zsh

mv zshrc_eg_mac_ohmyzsh .zshrc

```

Change name of profile file on `Ubuntu Linux`:

```zsh
mv zshrc_eg_ubuntu .zshrc
```

Load/run the new profile settings using `source`

```
source ~/.zshrc
```

Once you quit and restart your terminal app, your new alias settings should be working, but test this out to be sure. Make a test.txt file, and use `rm` to remove it. If things are correct, you should be prompted by the terminal with "remove test.txt?". Type Y to remove, N to leave alone. Note, these settings will protect you from terrible very bad accidents, and you will be able to easily override them when you are comfortable (to be covered later).



## 3. Text viewing *OR* text editing within the terminal

### Text viewers for quickly looking at small sections of files

We will make common use of text viewers such as `less`, `head`, `tail` or `more`; especially `less`. Why would we just want to "look" and not "open" large text files? Large amounts of data stored in text are often beyond the memory capacity of GUI programs, and most of what we will work with will be far too large to "look" at usefully anyway. `less` will allow you to have a peak at a file to understand its structure, which is ultimately what you will need to write code to manipulate and extract information. 

As `man` pages are by default viewed with `less` when you call them in the terminal, look at the `man` page for `less` for guidance on how to control this text viewer.

    man less

You will use `less` regularly, a few tips, as above:
- `q` quits and renews the active terminal prompt
- `spacebar` moves one page forward
- `b` moves one page back
- `/` allows search, `/123` will go to instances of "123".
- after first match is found, `n` will go to the next match.


Use `less` to have a look at the top of **sample_passerina.fastq** file I have added under week2 on the course page (note, this will initially have to be decompressed as detailed below). You will see that DNA sequence data from an Illumina machine is stored in a structured and simple format with 4 lines of data per sequence (ID line, DNA sequence, Quality ID, quality score).

### In terminal text editors

To access and edit text *within* the terminal, there are many editors (`vim`, `emacs`, etc.) you can use. For this course, I suggest `nano`, which will be available on your system. Why would you want to use a keyboard controlled only in-terminal text editor instead of something like VScode or BBedit? Once you start working on remote servers, the time and place for such usage will become more clear. For now, just know it exists as an option, but do not make your life harder by trying to write your first bash or python programs in `nano`.

To open a file for editing within the terminal with `nano`:

```
$ nano myfile.txt
```

Yall dont need to worry about in terminal editors for now. Introducing them here so that you get the idea; when and why they are important will become apparent later when we learn to work on remote servers.

## 4. Compression and decompression using `gzip` and `gunzip`

Compression and de-compression are regular activities associated with large text data files, so get comfortable with it. `gzip` is a command for compressing and decompressing files. **Compression is critical for preserving disc space and for moving large data between computers or servers over remote connection.** While you may need data in its uncompressed form, there is never a reason to NOT store data in compressed form.

Compressed .gz files can be easily decompressed.

    gunzip sample_passerina.fastq.gz

And compression is similarly easy. The below command will create the compressed file "sample_passerina.fastq".

    gzip sample_passerina.fastq

All .txt files in a directory can be compressed (or decompressed) using a wildcard, `*` with this command. Note the below command would compress, one by one, all files ending in .txt. `*` will make your life easier.

    gzip *.txt 

`tar` is a Linux command with more flexibility that is commonly used for compressing directories (`gzip` and `gunzip` work with files NOT directories). We will learn more about `tar` later.

`*` will make your life easier, and you will learn to use it in many contexts. `*` is short for wildcard, meaning it matches everything. So, `ls *.txt` would list all files that start with anything and end with `*txt` in the directory this command was executed from. Here is another simple example for now, which would copy all of the files starting with BS_1287 and ending in fastq.gz to a specified directory

    cp BS_1287*fastq.gz data_for_BS1287/

## 5. stdout, redirection (`>`)

**stdout** (standard out) is the text that is printed to screen when Linux commands are executed. The `cat` command is used to concatenate files and print file contents to standard output. Using it as below will print the entire contents of passerina.fastq to screen (this file is located in the `week2_LinuxII` directory). Try it.

    cat passerina.fastq

That doesn't seem very useful in most cases. Instead, we can redirect the standard output of any Linux command to a file simply by using redirection with `>`. Here are some simple examples.

The below command would concatenate the data from all files in a directory ending in data.txt into one file. Note that `*` is a wildcard character that means "anything", so its use below with ***data.txt** will match all files in the directory that have any text followed by **data.txt**.

    cat *data.txt > all_data_in_directory.txt

The use of `>>` below will write the contents of **newdata.txt** to the end of **all_data_in_directory.txt**.

    cat newdata.txt >> all_data_in_directory.txt

Redirection of `ls -lh` below simply sends all that information on files in the directory to a text file.

    ls -lh > directory_contents.txt

`grep` is a powerful regular expression matching command, and later in the course we will learn extensively about using it to match and extract data matching characteristics that we can specify. The use of `grep` below will send all lines containing a match to "BS_1287" to a new file.

    grep "BS_1287" data_all_inds.txt > data_for_ind_BS1287.txt

## 6. Basic process monitoring 

On linux systems, it is often important or necessary to have a look at what the system is doing - to get an idea of how many jobs or processes are running and who is running them. It is also a useful way to recognize jobs you have started from the terminal that need to be stopped or **killed**.

*This is a simple start, we will revisit next week*

`top` will display information on processes running on the machine you are logged into. Try it, read the output. Doesn't matter what directory you call it from. As with `less`, type `q` to exit the system view.

    top

`top` doesnt have the prettiest or most obviously searchable output. `htop` is an upgrade that you may or may not have on your system. If you downloaded `oh my zsh`, you should have it. In the coming weeks, we will learn how to efficiently install whatever you want from the command line. In the meantime, if you dont have `htop`, you can downloand and install it using `brew`, following basic guide to package installation below.

`ps` will show your active process ids. Below I am using `ps aux`, piping (with `|` ) the output into `grep` and using my username as the match for `grep`. Try it with your username.

    ps aux | grep thomasparchman

If you have mutliple processes running, and want to kill one, use `kill` followed by the process ID, which you can locate with `top`, `htop` or `ps`

    kill 9031


## 7. Package installation

This is a bit extra for what we are doing this week, but I thought I would add it here as a guide for those interested. For installing on your personal mac computers, `brew` will be your most convenient option. I would stress here that this type of package installer/manager makes accomplishing these tasks in the Linux OS incredibly easy.


### Package Management with Homebrew on macOS  

**Homebrew** (`brew`) is a package manager for macOS that makes it simple to install and manage software from the command line. It fills in the gap left by macOS, which does not have a built-in package manager like Ubuntu. Homebrew installs software into a central location (`/usr/local` on Intel Macs or `/opt/homebrew` on Apple Silicon) and handles updates and dependencies automatically. This allows you to quickly add tools needed for programming, science, and everyday command-line work.  

### Basic Tutorial  

1. Install Homebrew (if not already installed):  

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Update Homebrew package list (always do this before installing new software): 

```bash
brew update
```
3. Update installed packages to their latest versions: 

```bash
brew upgrade
```

4. Install a new package (for example, wget):

```bash
brew install wget
```

5. Remove a package you no longer need:

```bash
brew uninstall wget
```

6. Search for installable packages by keyword

```bash
brew search python
```


**Note**: Unlike `apt`, you generally don’t need `sudo` with Homebrew, because it installs everything under your user account.

A more detailed, yet basic, tutorial can be found below. As with the above, carefully review before using.

- https://wpbeaches.com/installing-homebrew-on-macos-big-sur-11-2-package-manager-for-linux-apps/

### Ubuntu Linux distributions: Package Management with `apt`

Ubuntu uses the **Advanced Package Tool (APT)** to manage software. APT makes it easy to install, update, and remove programs from the system using the command line, while automatically handling dependencies (other packages that a program needs to run). This is one of the most important tools for keeping your system up to date and for adding new software in a safe, consistent way.  

### Basic Tutorial  

1. Update your package list (always do this before installing new software):  

```bash
   sudo apt update
```

2.  Upgrade installed packages to their latest versions:

```bash
sudo apt upgrade
```

3. Install a new package (for example, curl):

```bash
sudo apt install curl
```
4. Remove a package you no longer need:

```bash
sudo apt remove curl
```

5. Search for packages by keyword:

```bash
apt search python
```

6. Get information about a package:

```bash
apt show curl
```
You can find additional tutorials on `apt` and `apt-get` below. I suggest reviewing information, and familiarizing yourself with `sudo` carefully before using.

- https://phoenixnap.com/kb/how-to-use-apt-get-commands
- https://itsfoss.com/apt-get-linux-guide/
- https://www.control-escape.com/linux/lx-swinstall.html


## 8. Regular expressions and text extraction with `grep`

`grep` is a powerful regular expression engine, among the most commonly used commands for data science. You can explore the examples below using `sample_passerina.fastq.gz`, available under week2 on the [course github page](https://github.com/tparchman/F25_BIOL792). This is an increbily versatile command, so we better learn more. In it simplest invocation, `grep` will output every line in a file that matches a specified pattern.

Since fastq files have a standard four line format (ID starting with @, DNA sequence, quality id starting with +, and quality score), we know that every sequence has a line starting with @ associated with it. 

You will first need to decompress `sample_passerina.fastq.gz`, as detailed above with `gzip` and `gunzip`:

     gunzip sample_passerina.fastq.gz

Use `less` to have a look inside this file to get an idea of how its contents are structured. Important keystrokes shortcuts for `less` include `q` to exit, `spacebar` to 
skip down a page, and `b` to skip up a page.

    less sample_passerina.fastq
    
We could write all of teh ID lines to a separate file:

    grep "^@" -c sample_passerina.fastq > idlines.txt

We can cound the number of sequences:

    grep "^@" -c sample_passerina.fastq

We can print the line with a match, plus any number of lines following it:

    grep "^@" -A 1 sample_passerina.fastq

SDN_AM_43432 is the ID of a specific bird represented in this data set. How many DNA sequences do we have for this bird?

    grep "SDN_AM_43432" -c sample_passerina.fastq


