*Written By: Chris Anderson* <br>
*Last Updated: November 16, 2023* <br>

# Installing Petalinux

This process will take a long time. This should be completed after the installation of Vitis and Vivado. <br>

**NOTE:** This is not required for Vitis and Vivado development. This is only for building an operating system. Theoretically, this only needs to be done once. 
<br>
<br>
This installation guide will show a step-by-step guide on installing Petalinux. As with Vitis and Vivado, Ubuntu 22.4.3 LTS is not an officially support OS for Petalinux. <br>
Throughout my time using Petalinux, there was not a specific issue that arose from using a more current version of Ubuntu, however, it will display many warnings. 

---

### What is Petalinux
Petalinux is a tool developed by Xilinx that works off of Yocto Linux distribution. What it does is create a custom Linux OS. While there is a great deal of configuration available with it, it creates an extremely bare bones and basic Linux OS. <br> <br>
This is essential for the project. The micro-controller used throughout this project thus far is the **Digilent Zybo Z7-20**. This is a powerful micro-controller, however, it is still a micro-controller. Therefore, we cannot run many complex distributions on it such as the Ubuntu distribution we have install on the system. <br> <br>
This is where Petalinux comes into play. Using Petalinux, we are able to integrate the Vivado FPGA firmware setup into our OS, creating many opportunities for expediting processing and essential operations that we would rather complete through "hardware" rather than software programs.

---

## How to install Petalinux
*This section will follow the steps required to install Petalinux on Ubuntu 22.4.3 LTS. The version of Petalinux that will be used is 2022.1, as it is the same as Vivado Vitis that has been installed.*

1. Installing pre-requisite libraries.
    + This is done rather easily since they are all part of Ubuntu's known library, therefore ```sudo apt-get install``` can be used to install them.
    + The libraries required to use Petalinux are: <br> 
```tofrodos```<br>
```iproute```<br>
```gawk```<br>
```gcc```<br>
```git-core```<br>
```make```<br>
```net-tools```<br>
```ncurses-dev```<br>
```libncurses5-dev```<br>
```tftpd```<br>
```zlib1g-dev```<br>
```flex```<br>
```bison```<br>
```lib32z1```<br>
```lib32curses5```<br>
```lib32bz2-1.0```<br>
```ia32gcc1```<br>
```ia32stdc++6```<br>
```libselinux1```<br>
    + It is important to remember that you may have many of these already installed, however, it is better to make sure by attempting to install it rather than guessing and not knowing why it does not work later.<br>

2. Downloading the Petalinux 2022.1 installer.
    + This requires a similar process to Vivado and Vitis.
    + You first need to go to the Xilinx download page [here](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools/2022-1.html)
    +
