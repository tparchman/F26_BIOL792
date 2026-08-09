# Windows Setup Guide for Learning Linux and Python

If you have a Windows PC, you can still work effectively with Linux commands and Python by setting up the right tools.  
You have two main options for running Linux:


## Option 1: Windows Subsystem for Linux (WSL)

WSL lets you run a Linux distribution inside Windows without a separate machine or virtual machine.

### Install WSL + Ubuntu:
1. Open **PowerShell** as Administrator.
2. Run:
```powershell
wsl --install -d Ubuntu
```
3. If `wsl` is not recognized, follow Microsoft’s [WSL Installation Guide](https://learn.microsoft.com/windows/wsl/install).

Once installed:
```bash
sudo apt update
sudo apt install wget git tree htop
```

> **Pros:** Easy to set up, integrates with Windows, no separate boot needed.  
> **Cons:** Slightly slower for heavy workloads, relies on Windows filesystem.


## Option 2: Standalone Ubuntu Installation

You can install Ubuntu as:
- **Dual boot** — choose Windows or Ubuntu at startup.
- **Full install** — replace Windows with Ubuntu (not reversible without reinstalling Windows).
- **USB boot** — run Ubuntu from a USB drive without changing your system.

### Steps:
1. Download Ubuntu ISO: [https://ubuntu.com/download](https://ubuntu.com/download)
2. Create a bootable USB drive with [Rufus](https://rufus.ie/).
3. Boot from the USB drive and follow the installation prompts.

> **Pros:** Full native Linux performance, best for long-term Linux use.  
> **Cons:** More complex setup, requires reboot to switch between OS.


## 1: Terminal & Shell Environment

- In WSL: Ubuntu terminal runs automatically when you open it.
- In standalone Ubuntu: Terminal is built in.
- **Windows Terminal** ([Microsoft Store](https://aka.ms/terminal)) can also open WSL sessions.


## 2: Package Management

In Ubuntu (WSL or standalone):
```bash
sudo apt update
sudo apt install wget git tree htop
```


## 3: SSH & Remote Server Tools

In Ubuntu (WSL or standalone):
```bash
ssh -V
```
If not installed:
```bash
sudo apt install openssh-client
```

Optional GUI client for Windows: [Termius](https://termius.com/)

## 4: Python Environment Management

In Ubuntu (WSL or standalone):

- **Miniconda (recommended)**:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

- Or install from apt:
```bash
sudo apt install python3 python3-pip
```

## 5: Code Editor / IDE

- **[VS Code](https://code.visualstudio.com/)** — works on Windows and Ubuntu.
  - For WSL: Install the **Remote - WSL** extension to edit Linux files.
- Alternatives: [Sublime Text](https://www.sublimetext.com/), [PyCharm](https://www.jetbrains.com/pycharm/).


## 6: Jupyter Notebooks

In Ubuntu (WSL or standalone):
```bash
conda install jupyterlab
```
Or:
```bash
pip install jupyterlab
```


## 7: Git & GitHub Setup

In Ubuntu (WSL or standalone):
```bash
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Optional GUI: [GitHub Desktop](https://desktop.github.com/) (Windows-native, not Linux-native).


## 8: AI Helpers (Optional for Later)

- **Chat-based:** ChatGPT, Claude, Perplexity.
- **In-editor:** GitHub Copilot, Cursor.
- **Command-line:** Warp (Linux version for standalone Ubuntu).


## 9: Useful Linux Tools

In Ubuntu (WSL or standalone):
```bash
sudo apt install htop tree nano rsync
```

## 10: Optional but Helpful

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) — integrates with WSL.
- [Oh My Zsh](https://ohmyz.sh/) — enhances Zsh shell with plugins.





## Test Your Setup

Open Ubuntu (WSL or standalone) and run:
```bash
pwd
ls -lh
mkdir test_directory
cd test_directory
echo "Hello Linux" > hello.txt
cat hello.txt
```
If these commands run successfully, you’re ready to start learning Linux and Python!
