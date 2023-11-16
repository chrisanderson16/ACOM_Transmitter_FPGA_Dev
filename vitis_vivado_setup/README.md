*Written By: Chris Anderson* <br>
*Last Updated: November 16, 2023*

# Installing Xilinx Suite Products
This process will take an extremely long time, regardless of internet access, computing power, etc. This should be done early on in development **AFTER** setting up the [dual-boot for linux](https://github.com/chrisanderson16/ACOM_Transmitter_FPGA_Dev/blob/main/environment_setup/README.md). <br>

This installation guide will give step-by-step instructions for installing Vitis and Vivado (and other Xilinx suite software) to the Ubuntu 22.4.3 LTS OS. Please note, this technically is *not* a supported distribution. However, throughout the time using this software on this version of Ubuntu, I have not encountered any errors. <br>

---

### What is Vitis and Vivado
This is an important starting point, even before installation. <br>
**Vivado** is professional FPGA firmware design software. This will be used to continue the development of the transmitter chain for the ACOM Transmitter FGPA. This software was introduced by Dr. J.F. Bousquet. It uses block diagrams and VHDL code to create logical representations of digital circuits on the FPGA. 
###### How to actually use this software will be detail in the *How to use Vivado*

**Vitis** is similar to many microcontroller/FPGA IDE's. This meaning, it is similar to using an arduino in the sense that you need to instruct the system on what it should do, given the firmware's definition of the digital circuits. You must import a bitstream, obtained from Vivado, to provide the Vitis on what it can use.<br>
For this specific project, this should be used as test software, to test the Vivado projects. This is due to the fact that scanning user with Vitis will not work with Petalinux. 

---

## How to install Xilinx Suite
