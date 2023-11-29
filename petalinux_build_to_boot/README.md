# Description
This is a repo for Team 7 to use .xsa files to build petalinux from. This repository will also share the instructions on how this is done below. <br/>

### IMPORTANT NOTE FOR FUTURE DEVELOPMENT
This is for use with a Zybo Z7-20 Development board, other boards may differ. <br/>

---

## Partitioning MicroSD card
Before we can begin moving the boot files to the SD card, we must first partition the SD card, similarly to how we did with partitioning for a dual boot. In fact, it is the exact same way! However, given you have dual booted, and are most likely on Ubuntu already, therefore, this explanation will show how to do this on a Linux distribution (Ubuntu). It is important to note that the process I will explain is the easiest I could find and it follows the UG1144 PetaLinux reference guide from Xilinx provides the full instructions, so if you face issues with the following instructions, refer to it [here](https://docs.xilinx.com/r/en-US/ug1144-petalinux-tools-reference-guide/Partitioning-and-Formatting-an-SD-Card).
<br>
The most important thing to remember when creating partitions for the Petalinux boot files is that the boot filesystem needs to be Fat32, whereas the root filesystem must be Fat Ext 4.
<br>

#### This will follow the process through the terminal, you opt to use the Ubuntu Disk Manager Application, or another equivalent application if you wish.

**1.** Insert the microSD card into your device. <br>
&emsp;+ MicroSD card may require adapter.
&emsp;+ Ensure it is **NOT** on Read-Only mode. This is typically a slider on the side.

**2.** Unmount the SD card with the following command in the terminal. <br>
```bash
sudo umount /dev/sdc
```

**3.** Enter the following command into the linux terminal and press *enter*.<br>
```bash
sudo fdisk -l
```
&emsp;+ This will display all the storage disks that you have on your device. Make note of the one that is your SD card. This can be done by matching the storage sizes.

**4.** Enter the following command and press enter (for this demonstration, I will be called the SD card *sdc1*):
```bash
sudo fdisk /dev/sdc
```
###### NOTE: THIS MAY BE DIFFERENT THAN YOUR SYSTEM. ***THIS WILL DELETE ALL DATA ON THE SD CARD***

**5.** Enter *n*. <br>

**6.** Enter *p* <br>

**7.** Leave *Partition number* and *First sector* blank by pressing enter. <br>

**8.** Enter in the size of storage you would like to have for the boot partition. UG1144 recommends ~10GB, This option is in bits, rather than bytes. Therefore, enter *21111220* and press *enter*. <br>

**9.** Select *y* <br>

**10.** Select *n* <br>

**11.** Enter *p* <br>

**12.** Enter *w* <br>
&emsp;+ This will create the final partition which will take up the remainder of the storage on the SD card.

**13.** Now we can format each partition. The boot will be formatted as Fat32 with the following command: <br>
```bash
sudo mkfs.vfat /dev/sdc1
```
&emsp;+ NOTE: This may have change the SD card's disk name, make sure to use the correct one!
&emsp;+ NOTE 2: You can simply look for the partition sizes you just made.

**14.** Finally, we format the file system partition with:
```bash
sudo mkfs.ext4 /dev/sdc2
```

<br>
Congrats! You partitioned the SD card, now you can continue into the next section of this document.

---

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
