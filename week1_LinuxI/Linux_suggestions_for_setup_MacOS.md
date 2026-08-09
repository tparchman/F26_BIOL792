# macOS Setup Guide for Learning Linux and Python

If you have a Mac running **macOS 15.3 (Sequoia)**, you already have a Unix-like operating system under the hood — perfect for practicing Linux commands and running Python.  
This guide will help you get set up before starting the course.

---

## 1. Terminal & Shell Environment

- **Built-in Terminal.app** — fine for starting out.
- **Optional alternatives:**
  - [iTerm2](https://iterm2.com/) — more features (search, split panes, profiles).

> **Why:** You’ll use the terminal to run Linux commands locally and connect to remote servers.

---

## 2. Install a Package Manager

### [Homebrew](https://brew.sh/)
Homebrew makes it easy to install and update command-line tools.

**Install from command line:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Example tools to install:**
```bash
brew install wget git tree htop
```

---

## 3. SSH & Remote Server Tools

- **Built-in OpenSSH** — already installed; check with:
  ```bash
  ssh -V
  ```
- **Optional GUI client:** [Termius](https://termius.com/) for managing multiple SSH connections.

> **Why:** Much of your Linux work will happen on remote servers or HPC clusters.

---

## 4. Python Environment Management

Choose one:
- **[Anaconda](https://www.anaconda.com/)** — larger install, includes many packages preinstalled. **Recommended**

- **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** — small installer, lets you manage Python environments and packages.
- **[pyenv](https://github.com/pyenv/pyenv)** — lightweight Python version manager.

---

## 5. Code Editor / IDE

- **[VS Code](https://code.visualstudio.com/)** — works well for Python, Markdown, and Git. **Recommended**
- Alternatives:
  - [Sublime Text](https://www.sublimetext.com/) — lightweight.
  - [PyCharm](https://www.jetbrains.com/pycharm/) — Python-focused.

---

## 6. Jupyter Notebooks

Install via Conda from command line:
```bash
conda install jupyterlab
```
Or via pip:
```bash
pip install jupyterlab
```

> **Why:** Lets you run Python interactively in a browser — python materials will be presented in jupyter notebooks on course github page.

---

## 7. Git & GitHub Setup
GitHub is an online platform that helps people store, share, and collaborate on code projects. It uses Git, a version control system, to keep track of every change made to your files so you can go back to earlier versions if needed. For beginners in Linux and Python, GitHub is especially useful because it makes it easy to share scripts, notebooks, and programs with others. It also lets you contribute to open-source projects or learn by exploring code written by more experienced developers. In short, GitHub is like a combination of cloud storage, teamwork hub, and history tracker for your programming projects.

Install Git (via Homebrew or check if preinstalled):
```bash
git --version
```

Configure Git:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Optional GUI: [GitHub Desktop](https://desktop.github.com/)

---

## 8. AI Helpers (Optional for Later)

- **Chat-based:** ChatGPT, Claude, Perplexity.
- **In-editor:** GitHub Copilot, Cursor.
- **Command-line:** Warp AI (part of Warp terminal).   - [Warp](https://www.warp.dev/) — modern terminal with AI-assisted command explanations.


---

## 9. Useful Linux-Like Tools on macOS

Install with Homebrew:
```bash
brew install htop tree
```

Already available on macOS:
- `nano` — simple text editor.
- `rsync` — file transfer tool.
- `grep`, `awk`, `sed` — text processing commands.

---

## 10. Optional but highly recommended

- [Oh My Zsh](https://ohmyz.sh/) — improves the Zsh shell with plugins and themes.

