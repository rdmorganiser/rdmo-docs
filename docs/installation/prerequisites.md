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

On RHEL/CentOS SELinux is enabled by default. This can result in unexpected errors, depending on where you store the RDMO source code on the system. Some guidance on how to configure SELinux is given at [here](../advanced/index.html#selinux).

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

On Windows, we recommend to use the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) to run RDMO. Once WSL is activated you can install Debian or Ubuntu using the Windows App Store and use the corresponding commands.

Otherwise, the software prerequisites need to be downloaded and installed from their particular web sites.

For Python:
* download from <https://www.python.org/downloads/windows/>
* don't forget to check 'Add Python to environment variables' during setup

For git:
* download from <https://gitforwindows.org>

For Pandoc:
* download from <https://github.com/jgm/pandoc/releases>

For pdflatex (optional, for pdf export):
* download from <http://miktex.org/>

All further steps need to be performed using the windows shell `cmd.exe`. You can open it from the Start-Menu.
