## Switchign from `bash` to `zsh` shells

These instructions are for Ubuntu linux and/or WSL/Ubuntu linux users.

1. Check current shell

```bash
echo $SHELL
```
You will likely see:

```bash
/bin/bash
```

2. Install `zsh`, and check that it installed correctly
```bash
sudo apt update
sudo apt install zsh
zsh --version
```
If so, you should see something like below:

```bash
zsh 5.9
```

3. Switch default shell to `zsh`

Locate where zsh is installed:

```bash
which zsh
```
Above will return somethign like:

```bash
/usr/bin/zsh
```
To actually change default shell

```bash
chsh -s $(which zsh)
```
You will probably be prompted for linux password. Once you have done that, close the WSL Ubuntu terminal completely and restart it.

Then check that `zsh` is set to default shell, by checking the `$SHELL` environment variation. The `echo` command should print the path to screen (e.g., `/usr/bin/zsh`)

```bash
echo $SHELL
```

4. Install `ohmyzsh`

Make sure curl and git are installed:

```bash
sudo apt install curl git
```
Then install Oh My Zsh using its standard installer:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
When installation finishes, your prompt should change.

Oh My Zsh keeps most of your shell configuration in:

```bash
~/.zshrc
```
And you can have a look at it with:


```bash
less ~/.zshrc
```

You can find information on `ohmyzsh`, including full documentation, information on themes to choose from, and more [here](https://ohmyz.sh/?utm_source=chatgpt.com#install)
