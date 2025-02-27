# Install prerequisites

Installing the prerequisites for RDMO differs on the different operating systems and is therefore covered in different sections. Here, you need to use the superuser.

## Linux

We recommend to install the prerequisites using the packaging system of your distribution. Use the following commands for Debian/Ubuntu or RHEL/CentOS.

```{eval-rst}
.. tabs::

   .. code-tab:: bash Debian/Ubuntu

      sudo apt install build-essential libxml2-dev libxslt-dev zlib1g-dev \
          python3-dev python3-pip python3-venv \
          git pandoc

      # optional, for pdf output
      sudo apt install texlive texlive-xetex lmodern librsvg2-bin

   .. code-tab:: bash RHEL/CentOS

      sudo yum install gcc gcc-c++ libxml2-devel libxslt-devel \
         python34-devel python34-pip python34-virtualenv \
         git pandoc

      # optional, for pdf output
      sudo yum install texlive texlive-xetex texlive-mathspec texlive-euenc \
         texlive-xetex-def texlive-xltxtra librsvg2-tools
```

On RHEL/CentOS SELinux is enabled by default. This can result in unexpected errors, depending on where you store the RDMO source code on the system. Some guidance on how to configure SELinux is given at [here](../advanced/index.md#selinux).

If the Python version on your system is no longer supported by RDMO, we strongly recommend that you upgrade your Linux distribution, as it is likely to be out of date. If you decide otherwise, it is relatively easy to install a different Python version using [uv](https://github.com/astral-sh/uv). Instructions can be found [here](../advanced/index.md#use-uv-to-install-a-custom-python-version).

## macOS

We recommend to install the prerequisites using [brew](http://brew.sh):

```bash
brew install python3
brew install git
brew install pandoc

# optional, for pdf export
brew install basictex
```


## Windows

On Windows, we **strongly** recommend to use the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) to run RDMO. Once WSL is activated you can install Debian or Ubuntu using the Windows App Store and use the corresponding commands given throughout this documentation.

Otherwise, and if you the adventurous type, the software prerequisites can be downloaded and installed from their particular web sites.

VS Code (we recommend this as editor and also to use the included terminal):
* download and install from https://code.visualstudio.com/

Python 3.12:
* download and install from <https://www.python.org/downloads/windows/>
* check **Add Python to environment variables** during setup

Node JS (only needed with the [development setup](../development/setup)):
* download and install from <https://node.js.org/en/download/package-manager>
* check https://github.com/rdmorganiser/rdmo/blob/main/.nvmrc for the major version used in RDMO (currently `18`)

Git:
* download and install from <https://gitforwindows.org>
* use the default options during installation, except:
   * use VS Code as default editor
   * use **Override default branch name for new repositories** and set it to "main"
   * use **Git from the command line and also from 3rd-party software**
   * use **Only ever fast-forward**

For Pandoc:
* download from <https://github.com/jgm/pandoc/releases>

For pdflatex (optional, for pdf export):
* download from <http://miktex.org/>

All further steps can then be performed in the Git-Bash shell either stand-alone or integrated into VS code, the windows shell `cmd.exe`, or the PowerShell. Since the commands differ slightly for the different options, please check the corresponding code examples labeled `bash` or `powershell`.
