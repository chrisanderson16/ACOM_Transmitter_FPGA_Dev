# Description
This is a repo for Team 7 to use .xsa files to build petalinux from. This repository will also share the instructions on how this is done below. <br/>

###IMPORTANT NOTE FOR FUTURE DEVELOPMENT
This is for use with a Zybo Z7-20 Development board, other boards may differ. <br/>

## Partition File Placement
**Partition 1: Smaller partition**<br/>
&emsp;&emsp;*BOOT.BIN*, *boot.src*, and *image.ub* must be copied here. <br/>

**Partition 2: Larger partition**<br/>
&emsp;&emsp;*rootfs.tar.gz* must be copied here and then extracted.  <br/>

# How to burn to microSD for boot
**1.** Once the folders are downloaded from GitHub, you must first extract the .zip file. <br/>
&emsp;a. This can be ignored if using git clone <br/>

**2.** Delete the existing files on both microSD card partitions. <br/>
&emsp; **For Boot partition**<br/>
&emsp;&emsp;```sudo rm BOOT.BIN``` <br/>
&emsp;&emsp;```sudo rm boot.src``` <br/>
&emsp;&emsp;```sudo rm image.ub``` <br/>
&emsp; **For File system partition**<br/>
&emsp;&emsp;```sudo rm -rf rootfs``` <br/>

**3.** Copy/Move the new boot files and file system <br/>
To use the following commands, find the path to the boot files on your system. Then from the boot partition of the microSD card: <br/>
&emsp;&emsp;```sudo cp /[PATH TO BOOT FILES]/BOOT.BIN .``` <br/>
&emsp;&emsp;```sudo cp /[PATH TO BOOT FILES]/boot.src .``` <br/>
&emsp;&emsp;```sudo cp /[PATH TO BOOT FILES]/image.ub .``` <br/>

Do the same with the file system partition: <br/>
&emsp;&emsp;```sudo cp /[PATH TO ROOTFS]/rootfs.tar.gz .``` <br/>

**4.** Extract/Untar the rootfs. This needs to be done inside the file system partition: <br/>
&emsp;&emsp;```sudo tar -xvf rootfs.tar.gz```<br/>
Then you need to delete the tar. <br/>
&emsp;&emsp;```sudo rm rootfs.tar.gz```<br/>

**5.** Final step is to ensure that everything is exactly where it should be. Verify the root filesystem can be opened and contains files. Ensure that the boot files are still there. Once this is complete, you can eject the microSD and place it into the Zybo Z7-20.

# Booting from Zybo Z7-20 Board
Just before we boot up the board and power it on, ensure the microSD card inserted into the Zybo board. Plug in the USB Type C cable to provide power to the board. <br/>
Next, open PuTTY or another equivalent tool to get the serial port prompt. This will probably be at /dev/ttyUSB1 or something equivalent. You can check with *sudo dmesg | grep tty* to find if a new device has been connected. <br/>
Set the baud rate to 115200. If using Linux, make sure the font is one that you have as to not cause errors. <br/>

With all this set up, we can flip the power switch on the board. This should then begin the boot process. If it does not, click the reset button on the board.

### Once the kernel boots and Petalinux is running
Typically the user and password are always the same (Will probably be prompt to change password): <br/>
&emsp;User: *petalinux* <br/>
&emsp;Pass: *petalinux* <br/>
Sometimes, it will prompt you to create your own password, just set this to whatever you wish. At the moment, the login is default.

## Confirm it has successfully booted
Type: <br/>
&emsp;&emsp;```echo "hello world!"``` <br/>

If this prints *hello world!*, it works. 
