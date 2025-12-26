# oh-my-alias v0.1

Oh My Alias was meant to be a script that adds a bunch of aliases, so you wont have to suffer anymore

## TOC(Table of contents)
- [Installation](#installation)
    - [#1 Option](#1-install-automatically)
    - [#2 Option](#2-install-manually)
- [How to use](#how-to-use)
    - [mkcd](#mkcd)
    - [rmcd](#rmcd)

## Installation
As they say:
> "options always have a main parent"

And in this case , this is true , so let's get started doing the parent , then we are gonna go through 2 paths

Firstly, if you are on windows , i highly recomend just using this in WSL and follow the steps

1. Clone this repo

Seriously, clone the repo by using this command:
```bash
git clone https://github.com/mintybrackettemp-hub/oh-my-alias/
```

Make sure the Oh my alias directory is specifically at `~/oh-my-alias`, do not delete it, or the installation will fail

This is where we have 2 options:

### #1 Install automatically
Make sure you use the following distros , otherwise , go to the second option:

- Ubuntu
- Debian
- Linux Mint
- Pop_OS!
- Or anything related to Ubuntu/Debian(Example: ZorinOS)
- Arch
- Manjaro
- EndevaourOS
- Or anything related to Arch(Example: Artix)
- Fedora
- CentOS
- Rhel
- Or anything related to Fedora(Example: Nobara)

using the repo , type EXACTLY this(or copy the command):

```bash
cd ~/oh-my-alias
python3 INSTALL.py
```

*(Make sure you git cloned first)*

It should automatically install Oh My Aliases, and yes , there will be options, just go through it and boom, you have it

*NOTE: Oh My Alias only supports zsh becouse it's still in development, and will make you switch to zsh unless you say so to not to , you can switch manually*

To uninstall , just run this:
```bash
cd ~/oh-my-alias
python3 UNINSTALL.py
```

### #2 Install manually

*(Make sure you git cloned the repo) at `~/oh-my-alias`*

It's actually pretty simple , just run this:

```bash
echo "source ~/oh-my-alias/shell/main.zsh" >> ~/.zshrc

source ~/.zshrc # this one is optional
```

To uninstall , just delete that line using `nano` or `vim` or whatever editor you use

## How to use

As i said, this is work in progress, so expect it to have a minimal amount of commands to learn:

### mkcd

mkcd has one purpose , make a new folder and cd into that folder , shortening `mkdir my-cool-folder && cd my-cool-folder`

ew , who needs that long, using the script , you can just run `mkcd my-cool-folder`

arguments:

Name of argument | Usage | Examples
-|-|-
`-p/--parent`| When you use the parent directory, such as `my-cool-folder/my-cooler-folder` | `mkcd -p folder1/folder2`
`-e/--expand` | Expand `~`, `.` or `..`| `mkcd -e -p ../folder1.5`
`-s/--silent` | Completly silent | `mkcd -s 'silent :D'`
`-v/--verbose` | Logs everything | `mkcd -v 'Crazy :/'`
`--configure-silence [option]` | `err` only logs errors(enabled by default), and `cre` only logs the creation of files| `mkcd --configure-silence err ''`
`-h/--help` | Builtin help | `mkcd -h`

### rmcd

rmcd does the same , but it first cd's into the parent and then deleted the specified folder

so instead of doing `cd .. && rm -rf my-removed-folder`

just do `rmcd`

It deletes your current folder and cd's into the parent

The following arguments:

- `-p/--parent`
- `-s/--silent`
- `-v/--verbose`

have the same functionality as the `mkcd` command

New arguments:
- `-f/--force` - forcefully delete empty folder, examples: `rmcd my-deleted-folder -f`
