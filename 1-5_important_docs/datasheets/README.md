*Written by: Chris Anderson*<br>
*Last updated: December 1, 2023*
<br>

# Datasheets
The datasheets in this directory are required to get an understanding of the hardware components used for the project. As the main component is an FPGA, we had used a Zybo Z7-20 SoC development board. However, this is not the only option, just the one we had used. That being said, it is powerful enough to complete all the tasks we want it to. 

## BII-5020
This datasheet is for the filter board. Please take a read through this to get a better understanding of the filter board and how it functions.

## BII-7522
This datasheet is for the transducer that has been provided by Dr. Bousquet. This is one of the major hardware constraints preventing the project from using a "full" JANUS implementation, rather opting for a JANUS-like implementation. The main difference being the operational frequency.

## TR-ORCA
The best way to think about this item is that it is an aquatic microphone and captures all acoustic levels within the UW channel. This is important as it can be used to test whether the final transmitter is producing an acoustic signal, and one that we want.