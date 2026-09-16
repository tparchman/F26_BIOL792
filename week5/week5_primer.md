# Why Python ?

One goal of this course is to introduce biologists without any, or much, prior programming experience to a language that can be useful for their needs. The choice of the first programming language to learn may not be as important as you think; once you have learned one, learning others will be much much easier, and you are nearly guaranteed to utilize additional languages at some point in your career. Nonetheless, the two scripting languages that have been most heavily used in bioinformatics and data science are **Perl** and **Python**. I had primarily used **Perl** for my needs, and have taught this course with Perl in the past. However, given a general shift in usage trends and training opportunities, beginning this semester, Ive decided to shift to Python both for teaching and for research purposes. There are a number of reasons for this:

- It is one of the most common languages used in biology and other fields of science. Thus, you will be able to find a lot of documentation, guidance, examples, and opinion on the web (see useful resources at the bottom of this page).
- It has excellent capabilities for manipulating text, suiting it well to bioinformatics and data science more generally.
- It uses consistent syntax, which makes learning specific code relatively easy.
- It has many built in libraries to facilitate common tasks
- Python is very widely used, across science, industry, and life in general 

<p>&nbsp;</p>

# Getting started with Python. 

## Topics to cover
- installing/updating python
- text editors, IDEs, `jupyter` notebooks and other media for writing python
- writing your first python script(s), `print` statements
- introduction to variable types in python
- Haddock and Dunn chapter 8, and first few pages of chapter 9

# 1. Installing/updating to python 3 current version
As we did with Unix, we are going to start slow and basic, ramping up as the weeks go on. First we are going to make sure everyone has the most recent version of Python installed. 

First check to see if you have python3 installed.  Open the shell and type

    $ python --version

If you get anyting that looks like version 2 not 3 or if you get an error that you dont have python, you will need to install version 3.


    $ brew install python3


### Python downloads, also potentially useful
Go to python.org and download the latest release

    https://www.python.org/downloads/mac-osx


## Ubuntu
It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python3 idle

# 2. Accessing, Testing, and Writing Python

There are multiple ways to run Python code. Each has different strengths and is suited for different tasks. Over the semester, you’ll learn to move between these environments depending on what you need — from quick tests to full research workflows.  In the end, I suggest that you mostly write code in either `jupyter notebooks` or in `.py` text files that you work on in a syntax-enabled code editor such as `VScode`, `sublime`, `bbedit`, or similar.

---

### 1. Python Interactive Mode in the Terminal

- Start by typing `python3` at the command line.  
- Opens the **Python interpreter**, where you type one python command at a time.  
- Good for testing lines of code, simple math, learning proper python syntax.  

Limitations:  
- Code is not saved.  
- Difficult to write multi-line (loops, conditionals) or structured programs.  
- Not useful for documenting work, terrible for debugging code that is more than just a few lines at a time.  

Think of this as a scratchpad or calculator for testing simple pieces of code.  

---

### 2. Jupyter QtConsole (via Anaconda Navigator)

- Works like interactive mode but with enhanced features.  
- Access it from Anaconda Navigator.  
- Advantages:  
  - Syntax highlighting.  
  - Inline plotting (you can see figures immediately).  
  - History of commands is preserved.  
  - Can also handle some Linux commands.  

This is much more usable than the bare interpreter and a good choice for quick but slightly more serious experimentation.  

---

### 3. Jupyter Notebooks

- Combines **code cells** with **Markdown text cells** (like these primers). If you are accustomed to `Rmarkdown`, this will feel familiar.  
- Excellent for keeping detailed descriptions of what, how and why you are doing things, along with alternating code blocks that can be executed on the fly from within the notebooks. Excellent for keeping accessible logs of python workflows for collaboration within a research group.  
- Ideal for:  
  - Teaching and learning step by step.  
  - Documenting your workflow.  
  - Creating reproducible reports.  
- Widely used in research and industry for data exploration, analysis, and communication.  

We will use Jupyter notebooks extensively in this course, as the weekly primers I provide will be written in Jupyter. This means when you download the notebooks and open then in `jupyter`, the code boxes will be active.  

---

### 4. Text Editors and IDEs (Integrated Development Environments)

- Python is most commonly written in stored as text in scripts with the `.py` extension as a custom. Scripts allow you to keep your code organized in one place, in executable format if desired, and allow you to organize code for different work as you deem useful. I will generally ask you to turn in your work for each week either in jupyter notebooks or in scripts (e.g., `Parchman_hashpractice.py` or `Parchman_haspractice.ipynb`).  

- The most important feature of a text editor for programming is that it recognizes the language you are using, and uses color to highlight syntax variation associated with functions, variables, control structures, and other aspects of programming languages. This helps you to write correct code, to debug code, to understand the code written by others, and to learn how to write code. Text editors and IDEs provide structured environments for this.  

Text Editors and IDEs which are well suited to python:  
- **Spyder**: comes bundled with Anaconda Navigator; looks and feels like `RStudio`; great for beginners.  
- **VS Code**: also comes bundled with Anaconda Navigator, popular and powerful editor with plugins for `Python`, `Git`, `Markdown`, `Linux` and more. 
Other commonly used editors:  
- **Sublime Text** Great basic text editor with customizable with plugins.  
- **BBEdit** (Mac only): simple, clean, and reliable with useful extensions and plugins. 

These tools are best when you need:  
- Larger projects that span multiple files.  
- Debugging tools.  
- Version control integration (Git/GitHub).  

You won’t need these immediately, but we’ll build toward them later in the semester.  

---

## To install Anaconda Navigator

There are numerous ways to install Anaconda, Jupyter, VScode, and other tools mentioned above. For consistency in this course, Im going to ask you to do something I normally don't: install a GUI package. In this case, by installing the Anaconda Navigator package, you will all install a suite of programs useful for data science, all at once. Doing this will insure that everyone in the room has access to this suite of tools, and can access them in a similar environment. 

Download the [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) suite of tools. From within this you can start the `Spyder`, `Jupyternotebooks', 'Jupyter QtConsole` and other tools from the launch menu> More importantly, you should also have access to these applications directly from the terminal.



# 3. Writing your first python program

We are going to do this first by writing some simple python in a file which we will call `first_python.py`. Go to a directory that you would like to work in for this exercise, then create this file, and open it in your text editor of choice:

```bash

touch first_python.py
open first_python.py
```
Hopefully you have configured your system to open all files ending with `.py` in a text editor such as `VScode`, `bbedit`, or `sublime`, or something similar. If not, now is the time to pause and get that fixed.

**We dont want to be using `nano` or other in terminal text editors to write and debug python code, unless its absolutely necessary. This is slow and clunky, and counterproductive to the learning process**


Similar to shell scripts from last week, the first line of python scripts should be the shebang followed by the location of python:

    #!/usr/local/bin/python3

or, depending on your system:

    #!/usr/bin/python3


If you are unsure where you installed python3, you can easily figure out where it is:

    $ which python3


You can also use the below text as your first line. This allows you to send script to `env` first, which should then locate python3, wherever it resides.

    #!/usr/bin/env python3

Either of the above will do, and are important **IF** or when you wish to convert your scripts to executable. If you want to do this, change the file mode: 

    $ chmod u+x first_python.py

And run as follows:

    $ ./first_python.py


## Your first simple program, using a `print` statement.

Sending information from your python scripts to stdout is accomplished with the `print` function. Our first script will simply illustrate how to print specified text, and will serve to convince you that this might not be as hard as you thought it was. Use `touch` to make a blank text file, but give it a `.py` extension as is customary for python scripts. This script needs only two simple parts. First, your customary first line that should go in all of your scripts, which should be:

    #!/usr/bin/env python3
Or the path to the specific location where python lives:

    #!/usr/local/bin/python3

To illustrate the use of `comment` text, marked with `#`, lets add a comment that is for you to read, not python. 

    #this is a comment: testing my first program with a simple print statement

Note the line above will not be part of the interpretted code. Instead, you can make use of `#` to leave annotations for yourself or others in your code to explain what you are doing.

Now lets add a print statement:

    print ("It is time to learn Python")

You can now run your program in two ways. Simply (which we strongly recommend for this class):

    $ python3 first_script.py 

Or, change to executable, then run:

    $ chmod u+x first_script.py
    $ ./first_script.py

If all is in order, "It is time to learn Python" should print to the screen, and you are ready for more.


<p>&nbsp;</p>


# 4. Quickstart tutorial for using jupyter notebooks

Now that youve written and run your first Python program as a `.py` script from the terminal, lets look at writing python code **Jupyter notebooks**. These notebooks are widely used in teaching, research, and data science because it lets you mix code, results, and notes all in one place.

Below is a quick tutorial. For a more detailed primer on getting started go to the [`jupyter_start`](https://github.com/tparchman/F25_BIOL792/tree/main/jupyter_start) directory at the top leve of the course github page.

### Opening Jupyter from the terminal

1. Make sure you have Anaconda installed (`Jupyter` comes with it).  
2. From your terminal, navigate to the directory where you want your notebooks to live. E.g.:

```bash
   cd ~/Documents/BIOL792/week5_pythonI/
```

Launch Jupyter Notebook with:

```bash
jupyter notebook
```
This will open a browser window showing the contents of the current directory. (If it doesn't open automatically, copy the URL shown in the terminal into your browser.)

Creating a notebook:

- In the Jupyter browser window, click New, then Python 3 Notebook.

- A new tab will open with an untitled notebook.

- Click into the first empty cell and type:

```py
print("Hello from Jupyter!")s
```

- Run the cell with Shift + Enter, or hitting the `play` button at the top of the window. You'll see the output appear directly beneath the cell.


### Markdown vs. Code Cells

- Code cells: run Python code and display the output immediately below.

- Markdown cells: let you write formatted text (like headings, bullet points, or math formulas) using markdown language (.md).

Try this:

- Change a cell to Markdown (from the dropdown at the top).

The type into the cell:

```md
# My First Notebook
This notebook combines **Python code** and *notes* in one place.
```
- Run the cell with Shift + Enter to see the formatted text.

### A simple plot demo

Notebooks really shine when you mix code, text, and visualizations. Try this in a new cell:


```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.title("Simple Plot")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
```
### notebooks vs. scripts

- **Scripts (`.py`):**  
  - Best for saving complete programs and running them from the command line.  
  - Suited for long-term projects and reusable code.  
  - No built-in way to mix code with notes or results.  

- **Notebooks (`.ipynb`):**  
  - Mix **code cells** with **Markdown text** for explanations.  
  - Run code in small, testable chunks.  
  - Excellent for teaching, learning, and documenting scientific workflows.  
  - Can easily include plots, images, and formatted notes.  

Both are important tools. In this course, you’ll practice with each so you learn when to use one or the other.

# 5. Variable types in python

Four types of ariables are used to store information in python:

- Scalars: These can be of type integer, Float, String, or Boolean. Scalar variables store one 'thing'
- Lists: are one dimensional arrays of scalars
- Tuples: immutable lists
- Dictionaries: associative arrays, or unordered sets of key:value pairs

Variables can be named almost anyway you like. However, they can not start with a digit (e.g., 1dog) or with `$` or `#` (e.g., $stop, #pound), and they can not be among the 33 python3 keywords (see https://docs.python.org/3/library/keyword.html). Keywords are reserved for specific functionality in python, examples include `False`, `if`, `else`, `elif`, `import`, `for`, and `True`.

## Scalars

Scalars are the first type of variable we will work with in python. They include:

- **Integers**: whole numbers 
    - 1
    - 5
    - 999999
- **Floats**: : any number, with decimal, also referred to as“floating point”. 
    - 11.23 
    - 0.0222 
    - 3 x 10-10 
    - 3e12

- **Strings**: sequence of text characters
    - “ACGGGTTAACCCTTT”
    - “Western Conference Finals”
    - “3.14159 approximates Pi”

- **Boolean**: True or False

Assigning variables in python is easy. You can name variables that store information any way you like. You may want to use a format that will allow you to recognize different types of variables, but the rules are flexible. Below, I am assigning a float to the variable Pi, an integer to the variable Place, and a string to the variable Team. 

```python
Pi = 3.14159
Iteration = 5
Team = "Bengals"
DNAseq = "AAATCGTTGTCTGTGTG"
```

The `print` function, use first above, can be used anytime you would like to print a variable to screen (e.g., the terminal window)

We will do more of this next week, but we can do math operations on integers and floats and the variables which they are assigned to. Note the code below will print 21.

```python
x = 7
y = 3
z = x * y
print(z)
```

We can use the `.type` function to check the type of variable>

```python
type(x) ## will return int
type(DNAseq) ## will return string
```

## Lists

Lists store multiple scalars, of the same, or of different types. Lists are heavily used in python, as they are in other programming languages, and offer a variable type that can be iterated through with loops. 

One dimensional lists can be hard coded as below. Note that print here is used to print the entire list.

```python
ColorList = ('blue', 'red', 'green', 'violet', 'orange')
NumList = ('9', '83', '85', '11','52')
print(NumList)
```
Individual list elements by the name of the list and the list index enclosed in brackets. The index of the first element is `0`.

```python
ColorList = ('blue', 'red', 'green', 'violet', 'orange')
print(ColorList[1]) # will return red
```

In the upcoming weeks you will get comfortable writing loops to execute the same code on every element of a list. When we do that you will start to learn that indents have strict rules in python code. Below is an example of a for loop that simply executes a print statement for each element in a list.

```python
ColorList = ('blue', 'red', 'green', 'violet', 'orange')
for color in ColorList:
    print(color) # note the indent. If the first line under for was not indented, and error message would come and this would not work.
```

## Dictionaries
These are unordered associative arrays that consist of key value pairs. Because they are unordered, the offer a much faster way to store and retrieve information that comes in pairs of variables. We will learn much more about how to build and loop through dictionaries later this semester. They may feel weird at first, but dont let that stress you out. Eventually you will come to appreciate or even love them.

Dictionaries are normally built on the fly with data read from files, but they can be hard coded for demonstration purposes as illustrated below.

```python
NameNumber = {
'Jerry' : '784.4495',
'Lee' : '784.1658',
'Angie' : '784.4496',
'Suzie' : '784.1555'
}
for key in NameNumber:
...     print(key, ":", NameNumber[key]) 
```

# 6. Writing/thinking in Pseudocode

Before writing any actual code, it is often helpful to first outline your plan in **pseudocode**. This is an informal way of writing out  *logic* of a program in English in order to organize your thoughts.

### What is pseudocode?
- A step-by-step outline of what your code should do.  
- Written in human-readable form, without worrying about Python syntax.  
- A blueprint for your actual script.  

### Why use pseudocode?
- **Clarity:** Forces you to think about logic before getting stuck on Python details.  
- **Planning:** Break down problems into smaller pieces.  
 

### When to use pseudocode
- When approaching a problem for the first time.  
- When writing functions or loops that involve multiple steps.  
- When designing workflows that combine data processing, analysis, and visualization.  

### Example
Suppose we want to count how many lines in a FASTQ file start with `@`.  
First write it as pseudocode:

**Open the FASTQ file\
Set a counter to zero\
For each line in the file:\
If the line starts with "@":\
Add one to the counter\
Print the counter**

This would translate into python as:

```python
counter = 0
with open("sample.fastq") as infile:
    for line in infile:
        if line.startswith("@"):
            counter += 1
print(counter)
```



# 7. Additional resources to help with learning Python


## Python documentation and other useful resources. 

I strongly recommend you explore several of the below resources and tutorials. They will all facilitate your progress greatly.

[Python documentation](https://www.python.org/doc/)

[Python for Biologists](https://pythonforbiologists.com/tutorial.html)
- Excellent tutorials and primers for introductory python. Follows similar topics to what cover in this class, with lots of variation on themes.

[Learn Python Interactive](https://www.learnpython.org/)
 - This has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.

[Python guru ](https://thepythonguru.com/)
 - This also has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.


## AI tools to accelerate learning

AI platforms (such as ChatGPT, GitHub or VScode Copilots) can be powerful tools for learning Python more quickly. They are not a replacement for understanding the language yourself, but they can help in several useful ways:

- **Debugging help:** If you paste in an error message or a block of code, AI tools can be extremely useful for debugging and explaining why errors are happening.  
- **Code explanation:** AI can do a very good job of explaining, line by line, functioning code written by others. I have found it quite useful for describing how specific lines, blocks, or entire programs work. This might be its most obvious use for learning.  
- **Boilerplate code generation:** AI can write repetitive or template-style code (e.g., loops, plotting setup) so you can focus on the logic of your program.  
- **Learning by iteration:** You can experiment by asking AI to write a simple function, then refine it step by step to see how changes affect the output.  
- **Exploring new tools and libraries:** AI can suggest packages or commands you might not know about yet, which can broaden your toolbox faster.  

**Note:** AI should be used as a guide and accelerator, not as a crutch. Always read, test, and understand the code yourself to make sure it does exactly what you intend. **In scientific coding, transparency and reproducibility depend on your ability to explain your work clearly**. There is no escaping this responsibility.


## Note on Python 3 syntax updates and Haddock and Dunn.

 If you are using Haddock and Dunn text, be aware that it is based on python2, and there are some important differences between python2 and python3 (syntax changes that will require slight modification of book examples)


1. print statements in python3 should use (). 
2. `raw_input()` has become just `input()`

