*Written by: Chris Anderson* <br>
*Last Updated: November 16, 2023*

# Setting up test Environment
To utilize any tools for this project, it is important to note that a *specific* environment is required. This being a **Linux** distribution.  Vivado and Vitis are available for Windows OS and certain Linux distributions. Petalinux is **ONLY** available for Linux distributions. Below is a list of OS's that can be used. 
<br

Vitis is available on:

- RHEL/CentOS 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2
- RHEL 8.3
- Ubuntu 16.04.5, 16.04.6, 18.04.1, 18.04.2, 18.04.3, 18.04.4, 20.04, 20.04.1 LTS
- Amazon Linux 2 AL2 LTS
- SUSE Enterprise Linux 12.4
- Windows 10 64-bit Professional and Enterprise versions 1809, 1903, 1909, and 2004
<br>

Petalinux is available on:

- Red Hat Enterprise Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8 (64-bit)
- CentOS Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8 (64-bit)
- Ubuntu Linux Workstation/Server 16.04.5, 16.04.6, 18.04.1, 18.04.2, 18.04.3, 18.04.4(64-bit)
<br>

With this being noted, the work for this project had been done on Ubuntu 22.4.3 LTS. This has not caused any issues with any operations of software, however, this is important to note as some errors could occur due to this. 
<br>

Moving on to actual requirements for the software. As per Xilinx, it is recommended to have a minimum of 16GB of RAM with 100GB of storage. *However*, in practice, we have found that you require more than 256GB to actually install Xilinx suite products. Therefore, if your system does not contain these, can a powerful CPU, it is recommended to use the lab computers. For this, please see the internal supervisor. 
<br>

---

###### IMPORTANT: All steps remain the same, until the last section of updating Ubuntu, may be different if not Debian distribution.

---

## Installing a Ubuntu Distribution
*Skip if you already have a Linux distribution*
Getting the initial info out of the way, we can move to actually setting up the test environment. This section will contain instructions on how to partition a storage drive, prepare a boot drive, and installing Ubuntu 22.4.3 LTS. This will be done in steps, this also assumes you have Windows installed as your OS.
<br>

### Partitioning
Partitioning is the process of creating partitions of a storage drive. If you do not have another drive to use, you must *dual-boot* your system. If looking to *dual-boot*, you must partition **PRIOR** to attempting the remainder sections. 
<br>

---

###### IMPORTANT: Another guide to setting up a dual-boot with Windows and Ubuntu can be found at [FreeCampCode](https://www.freecodecamp.org/news/how-to-dual-boot-any-linux-distribution-with-windows/)

---

#### What you need
+ Computer/laptop you wish to dual-boot or change OS
+ USB drive or equivalent storage device of 8-16GB
+ Download the image file (For Ubuntu, you can use this **[link](https://ubuntu.com/download/desktop)**)

## Installing dual-boot Ubuntu
#### Set up Partitions

**1.** Open *Create and format hard drive partitions*.
<br>

**2.** Shrink a pre-existing volume.
+ Assuming you do not have another new drive to install Ubuntu on.
+ Please keep in mind, shrinking a partition may result in data loss. Make sure to backup any important files and/or documents. 
+ Ensure to retain at least 20GB from current storage state on main OS partition as to not unintentionally lose data.

---

###### EXAMPLE: If I have a 500GB SSD with a total of 300GB being used by my C: drive, do not shrink more than 150GB. 
 - Keep in mind this may not be enough to install software later down the setup process.

---

**3.** Ensure your drive looks like this:

![Disk-Management-image](../img/disk-management-after-shrink.jpg)

**4.** You have now partitioned your storage drive to be used for a dual-boot. Congrats!



---

#### Setting up a boot drive
Now that you have a partition for Ubuntu to install to, you need a drive to install from. That can be any external storage device, but must be at least 8-16GB. 
<br>

**1.** Install an image burning software, we have used **[Rufus](https://rufus.ie/en/)**.
<br>

**2.** Insert the storage drive into your computer, then start **[Rufus](https://rufus.ie/en/)**.
<br>

**3.** In **[Rufus](https://rufus.ie/en/)**, select the image file (Something like *ubuntu-22.4.3-desktop-amd64.iso*) we want to use. This is the one we downloaded from Ubuntu above. 
<br>

**4.** Select the drive you want to "burn" the image to. Make sure to select the external storage device (Something like *USB (F:)*). 
<br>

**5.** Press **Start**, you now have a boot drive that can be used to install Ubuntu. Congrats!
<br>

---

#### Installing Ubuntu
After completed the previous sections, you now have the means to install Ubuntu onto your device. Follow the next few steps on how to install Ubuntu. 
<br>

**1.** Shutdown device.
<br>

**2.** Insert boot drive.
<br>

**3.** Turn on device.
<br>

---

###### **IMPORTANT:** Some computer's BiOS will recognize the boot drive immediately, some will not. If it does not prompt you to *Try Ubuntu* or *Install Ubuntu* and just starts up Windows as normal, determine how to open BiOS on your device, this could be done by pressing F12 or F10 or DEL repeatedly while booting.

---

**4.** Select *install Ubuntu*.
<br>

**5.** Follow all the steps that are required, such as, creating an account, setting timezone, setting partitions.
+ If prompt with setting partitions for boot and filesystems, set boot for 24GB and the rest for the filesystem, however, this should not occur.
<br>

**6.** Once you reach the end of these options, you will be given a loading screen where Ubuntu will *actually* install. Wait for this to complete.
<br>

**7.** Congrats, when it's done installing, you have successfully dual-booted Windows OS and UBuntu 22.4.3 LTS.
<br>


**Congrats**, you have not completed the dual-boot setup and installation process.

---

### Accessing Ubuntu and Windows
With dual-booting, your BiOS must now manage 2 different boot drives. In practice, when you install from scratch, whenever you turn on your device, it should prompt an option of booting Windows OS or Ubuntu OS. <br> <br>
If this is **NOT** the case, you will need to open your BiOS each time you wish to boot Ubuntu and select the boot partition for Ubuntu.

---

### Alternative Install: Replacing OS with Ubuntu
Another alternative from dual-booting is to switch from Windows OS to Ubuntu or another Linux distribution. Keep in mind, this would be completed wiping the Windows OS install and replacing it with another. This is reversible to a degree, however, it is never easy. 
<br>

***ONLY DO THIS IS YOU WANT TO LEARN LINUX AND DO NOT CARE TO USE WINDOWS OS ON DEVICE.***
<br>

If you choose to do this, make sure to backup all data you wish to keep. Then confirm the data is backed up. Then make sure it's backed up again. Once you choose this option, the ***data will be lost forever***.
<br>

In the above section for completing a Ubuntu dual-boot, you can ignore the partitioning step. Make sure to follow up on research prior, as once you start, you will be unable to use the device until Ubuntu has completed.
<br>

**1.** Back up any and all important data you do not wish to lose.
+ Also, make sure to capture any and all serial numbers for your device, Windows OS key, etc. 
    + This is so that in the event you wish to reinstall Windows OS, you are able to without purchasing another license.
<br>

**2.** Skip the ***Set up Partitions*** section.
+ Since we are not creating another boot drive, we do not need to divide a drive into partitions to install.
+ Again, ***DO NOT DO THIS IF YOU DO NOT WISH TO LOSE WINDOWS OS***
<br>

**3.** Complete the ***Setting up a boot drive*** section as normal. 
<br>

**4.** Complete the ***Installing Ubuntu*** step, however, this time select the drive that contains the Windows OS and Windows data.
+ ***This will erase any and all data on the respective drive, DO NOT DO THIS IF YOU WISH TO LOSE THIS DATA.***
<br>

**5.** Congrats! You have now installed Ubuntu Linux. 
+ This is what I have done, and it is a good way to *force* yourself into learning Linux. It also makes it easier to interact with the Linux environment and get more comfortable with Linux in general.

---

## Setting up Ubuntu
Now that you have a Linux distribution install and runs, we can now begin to prepare the system for actual use. This is primarily done by installing required libraries. 
<br>
The last step in this process is updating Ubuntu itself. 
<br>

&emsp;```sudo apt update``` 
<br>

&emsp;```sudo apt upgrade``` 
<br>

These commands should be run every few weeks as to keep Ubuntu's system up-to-date.
<br>

Make will be required for using Vitis down the road, and any other makefiles you wish to create on the Ubuntu system. For this, enter the following command: 
<br>

&emsp;```sudo apt install make```
<br>

There are many other dependencies and libraries that may be required. A simple error log may be telling of potential issues that may arise down the road. The *sudo apt install* bash line works well for most distribution recognized libraries and dependencies.
<br>
<br>

