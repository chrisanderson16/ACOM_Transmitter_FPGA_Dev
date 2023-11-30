*Written By: Chris Anderson*<br>
*Last Updated: November 20, 2023*

# PetaLinux
*This module document contains the simplified process for using Petalinux as a tool to create a Yocto-based operating system for the Zybo Z7-20 development board by Digilent. It is important to note that Petalinux builds depend on the board that you are using, and it must be taken into account which FPGA board you are using.*
<br>
<br>
There are many different ways to create a Petalinux OS, this includes this document, the given [tutorial provided by Dr. Bousquet](./Petalinux_Tutorial_Ehsan) and the [UG1144 Reference Guide for Petalinux 2022.1](./petalinux_Reference_Guide_2022-1.pdf). Many of them include different instructions on what to do, what configurations to change, etc. In this document is a collection of instructions that had worked for me. 

## What is PetaLinux
PetaLinux, or as I tend to write it petalinux, is a Yocto-based tool, created by Xilinx, to create operating systems for use on microprocessors, such as the Zybo Z7-20. In a simpler definition, it is a way to automate the extremely difficult process of creating embedded Linux OS for embedded systems. An example of embedded linux could be your internet router, which many run embedded linux to provide and run the services for your internet. 
<br>
<br>
While operating systems can slow down processes on FPGA boards, they can allow a system to become more interconnected, easier to use, and allow for more configuration. They also allow for better debugging from the transmitter chain. Petalinux has the advantage of being extremely "bare bones" and does not come with any "bloat-ware". 
<br>
<br>
That being said, there is a great deal that can be customized with petalinux. You are able to set the OS up in whatever way you like. There is a great deal to know about Petalinux, however, you are able to get away with using a surface level amount. I do recommend you read the [Reference Guide](/using_petalinux/petalinux_Reference_Guide_2022-1.pdf) as it can provide a great deal of insight and helpful tips, as well as being an essential tool for using Petalinux.
<br>

---
###### DISCLAIMER:Petalinux ***requires*** a Linux-based operating system.  I'm sure you noticed that the supported operating systems do not include Ubuntu 22.4.3 LTS (the one that was suggested to be installed). I have not personally experienced any issues with petalinux on this version (other than warnings that have not affected anything).

---

## What you need
There is some items that you will need to actually build the project. The first being the [Build Support Package (BSP) file](./Zybo-Z7-20-Petalinux-2022-1.bsp) in this module. You can think of this as the foundation of the Petalinux house we're building.
<br>
<br>
The next thing you need, which is optional for an initial build, but required for the project is the Xilinx Support Archive (XSA). This is what needs to be exported from Vivado to be appended to Petalinux, which when booted, will enact the hardware on the board.

---

## Building your first project

*There are many online resources with people detailing the absolute way to build a project. I found [Digilent](https://digilent.com/reference/programmable-logic/zybo-z7/demos/petalinux) (Creators of the Zybo Z7-20 Development Board) have a good instruction set that I based my instructions off of that I used to get my first successful build.*

Petalinux works via the command line. As stated in the previous module for installing petalinux, you must first source the commands. If you have implemented the suggested *.bashrc* file edits, great! If not, you must type in the following command:
```bash
source /home/chris/petalinux/settings.sh # As given in the previous module
```
You can now use petalinux tools. The next setup stage is downloading the corresponding BSP file. This can be downloaded from [Digilent's GitHub repository](https://github.com/Digilent/Zybo-Z7/releases/tag/20/Petalinux/2022.1-1/Zybo-Z7-20-Petalinux-2022-1.bsp). Simply download the .bsp asset.
<br>
<br>
Now, you can create your own project. The following will be step-by-step instructions to building your own petalinux project. 
<br>


1. Make a project directory, go into that directory.
```bash
mkdir z720-petalinux-build-v1 # In the event a build fails, I note the number
cd z720-petalinux-build-v1
```
2. Create the project, go into the project's directory (os/).
```bash
petalinux-create -t project -s /home/chris/petalinux-builds/BSP-files/Zybo-Z7-20-Petalinux-2022.1-1.bsp
cd os
```
+ The *-t* flag denotes what is being created.<br>
+ The *-s* flag denotes the source, BSP, we will build the project for/from.

3. Configure the project.
```bash
petalinux-config
```
+ This will open a menu, to where you can select different options to configure the final build.
    + For now we just open, then save and exit.

4. Build the project.
```bash
petalinux-build
```
+ It is important to note that this process will take quite some time. It will depend entirely on the computer you are using, however, from my experience, this can take upwards of 30-45 minutes.

5. We create the boot files to be placed onto the SD card to boot from. This step can be found in the [petalinux_build_to_boot](/petalinux_build_to_boot/README.md) module.
```bash
petalinux-package --boot --force --fsbl images/linux/zynq_fsbl.elf --fpga images/linux/system.bit --u-boot
```

6. Assuming the build did not fail (which it might!), congrats! You made your first bare bones Petalinux project!
<br>

---

## Building a Petalinux Project with an XSA file
*This process is almost identical to the previous build, however, there is one additional step that requires an XSA file. This XSA will be exported from Vivado as the hardware description.*

1. Make a project directory, go into that directory.
```bash
mkdir z720-petalinux-build-v2 # Different build, different number
cd z720-petalinux-build-v2
```
2. Create the project, go into the project's directory (os/).
```bash
petalinux-create --type project --template zynq --name z720-petalinux-build-v2
cd z720-petalinux-build-v2
```
3. Configure the project with the given hardware description (.xsa file).
```bash
petalinux-config --get-hw-description /home/chris/petalinux-builds/xsa-files/[EXPORTED VIVADO HW DESCRIPTION].xsa
```
+ This will open a menu, to where you can select different options to configure the final build.
    + For now we just open, then save and exit.

4. Build the project.
```bash
petalinux-build
```
+ It is important to note that this process will take quite some time. It will depend entirely on the computer you are using, however, from my experience, this can take upwards of 30-45 minutes.

5. We create the boot files to be placed onto the SD card to boot from. This step can be found in the [petalinux_build_to_boot](/petalinux_build_to_boot/README.md) module.
```bash
petalinux-package --boot --force --fsbl images/linux/zynq_fsbl.elf --fpga images/linux/system.bit --u-boot
```

6. Assuming the build did not fail (which it might!), congrats! You made your first bare bones Petalinux project!
<br>

---

## Now what?
Once you have successfully built Petalinux, the complex part is out of the way. Now you must obtain the necessary files to actually boot on the Zybo Z7-20.
<br>
<br>
To get these files, starting in the project directories:
```bash
cd os/images/linux
```

This is where the necessary files to boot the board reside. These files being:
+ *BOOT.BIN*
+ *boot.scr*
+ *image.ub* 

<br>

Another necessary piece to the puzzle is the ***Root File System*** or ***rootfs***. This is required, but it is also found in the same directory. Copy these files to somewhere accessible, then move to [petalinux_build_to_boot](../petalinux_build_to_boot/README.md) for instructions on how to get them to the Zybo board and to boot.

---

## Troubleshooting Petalinux Build Errors
When using Petalinux, there is an extremely long rabbit hole that you can go down, leading to a large amount of potential errors and build fails. So if you are trying to build, and run into an error, don't sweat it! It will happen.
<br>
<br> 
From my time experimenting and learning how to build with petalinux, there is a great deal that can go wrong. This tool is also somewhat obscure, i.e. it is not an easy Google away. I found what was best to do was the build a project, change one or two parameters or configurations in *petalinux-config* to see what had changed between each build. However, the [Xilinx Support forums](https://support.xilinx.com/s/question/0D52E00006iHp9DSAS/embedded-linux-useful-resources?language=en_US) for petalinux are usually a good help when trying to diagnose a reoccurring issue.