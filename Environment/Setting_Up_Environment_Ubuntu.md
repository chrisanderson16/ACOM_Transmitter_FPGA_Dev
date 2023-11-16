*Written by: Chris Anderson*

# Setting up test Environment
To utilize any tools for this project, it is important to note that a *specific* environment is required. This being a **Linux** distribution.  Vivado and Vitis are available for Windows OS and certain Linux distributions. Petalinux is **ONLY** available for Linux distributions. Below is a list of OS's that can be used. <br>

Vitis is available on:  <br>

- RHEL/CentOS 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2
- RHEL 8.3
- Ubuntu 16.04.5, 16.04.6, 18.04.1, 18.04.2, 18.04.3, 18.04.4, 20.04, 20.04.1 LTS
- Amazon Linux 2 AL2 LTS
- SUSE Enterprise Linux 12.4
- Windows 10 64-bit Professional and Enterprise versions 1809, 1903, 1909, and 2004


Petalinux is available on: <br>

- Red Hat Enterprise Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8 (64-bit)
- CentOS Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8 (64-bit)
- Ubuntu Linux Workstation/Server 16.04.5, 16.04.6, 18.04.1, 18.04.2, 18.04.3, 18.04.4(64-bit)

With this being noted, the work for this project had been done on Ubuntu 22.4.3 LTS. This has not caused any issues with any operations of software, however, this is important to note as some errors could occur due to this. <br>

Moving on to actual requirements for the software. As per Xilinx, it is recommended to have a minimum of 16GB of RAM with 100GB of storage. *However*, in practice, we have found that you require more than 256GB to actually install Xilinx suite products. Therefore, if your system does not contain these, can a powerful CPU, it is recommended to use the lab computers. For this, please see the internal supervisor. <br>

#### ALL STEPS REMAIN THE SAME, REGARDLESS OF DISTRIBUTION RELEASE

---

## Installing a Ubuntu Distribution
*Skip if you already have a Linux distribution*
Getting the initial info out of the way, we can move to actually setting up the test environment. This section will contain instructions on how to partition a storage drive, prepare a boot drive, and installing Ubuntu 22.4.3 LTS. This will be done in steps, this also assumes you have Windows installed as your OS.

### Partitioning
Partitioning is the process of creating partitions of a storage drive. If you do not have another drive to use, you must *dual-boot* your system. If looking to *dual-boot*, you must partition **PRIOR** to attempting the remainder sections. <br>


