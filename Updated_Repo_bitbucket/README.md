*Written By: Chris Anderson*<br>
*Last Updated: November 20, 2023*

# Capstone Project: *ACOM Transmitter FPGA Development*
This is a project collaboration between Dalhousie University and Ultra Maritime ( *Nova Scotia's division of Ultra Electronics*). The full project is to develop a transmitter chain to take user data to send across the underwater channel to the sister project, the ACOM Receiver. 
<br>
<br>
This project has had many hands on it over the years, most recently, as our capstone project. This repository is a collection of documentation and knowledge that we have gained over the duration of our time working on it. This README\.md file will detail the scope of the project as it stands, as well as, what each module (directory) entails. 
<br>

---

## Project Scope
The aim of this project, as briefly stated above, is to create an Acoustic Modem (ACOM) Transmitter. This will use the following components: FPGA board, filter circuit, amplifier circuit, and underwater transducer. This system will take input data, encode (error correction), modulate, filter (D/A converter), amplify, and transmit, all in accordance with JANUS standards. 
<br>
<br>
This document will gloss over many of the important aspects that are required to know when stepping into the project. Specifically, each aspect of the project that may be unknown or new to you.

---

## Background
*This section will provide you with the necessary information on the background of the device, how and why it works, what is needed, etc. This an important part of the project, as actually understanding what the system does and needs to do is important to continue the design work.*

### ACOM Transmission
An Acoustic Modem, or ACOM, is a transmitter that employs a method of data transmission that does exactly what the name tells. It communicates via acoustic waves, rather than radio or microwave. The image below shows this idea illustrated with how it *could* be used with an underwater Remote Operated Vehicle (ROV). While there is a wide range of uses, including an alternative to laying telecommunication lines, it is important to note that ACOM transmission is much slower than traditional methods of data transmission. While water has a greater speed of sound when compared to air, it's attenuation is much greater. This can (*and does*) cause a great deal of data loss and scattering of signals, making it difficult to, not only receive the data, but to ensure that it isn't being received multiple times at incorrect times.
<br>

![acom-transmitter](/img/ACOM_Diagram.png)

<br>
This is where Binary Frequency Shift Keying (BFSK) and Frequency Hopping (FH) come into play. Utilizing these two operations allow for data to not only ensure that it is being received properly, but also that it is not being obtained at improper times. 
<br>
<br>

#### Binary Frequency Shift Keying (BFSK)
This is a complex idea to really get a hold on, so I would suggest putting some of your own research into the topic. 
<br>
<br>
In it's simplest form, BFSK is a way to note 0's and 1's as varying frequencies. For example, if I have a center frequency of 1000Hz, my 0 may be represented by 900Hz and my 1 may be represented by 1100Hz. 
<br>
<br>

#### Frequency Hopping (FH)
FH is another somewhat complex idea, so, again, I would suggest putting some research to getting a good hold on the idea. 
<br>
<br>
FH is a almost exactly what it sounds like. Each bit is to be transmitted at one of thirteen different frequencies within the JANUS bandwidth. This works along with BFSK. 
<br>
<br>

#### When we use them together
For an idea of how this may work in practice, please see below in the code section. It is important to note that this has been done for us my previous developments, however, verification is always a good thing.
```python
info                    = 0b00111011
carrier_freq            = 11520     # Hz
BFSK_bound              = 80        # Hz

# In addition to these frequencies, there are 5 others that are unused
# #####################################################################
# bit 7 = 0 
center_freq_7           = 11840     # Hz
bit_7_transmission_freq = center_freq_7 - BFSK_bound
# bit 6 = 0 
center_freq_6           = 11520     # Hz
bit_7_transmission_freq = center_freq_7 - BFSK_bound
# bit 5 = 1 
center_freq_5           = 11200     # Hz
bit_7_transmission_freq = center_freq_7 + BFSK_bound
# bit 4 = 1 
center_freq_4           = 10880     # Hz
bit_7_transmission_freq = center_freq_7 + BFSK_bound
# bit 3 = 1 
center_freq_3           = 10560     # Hz
bit_7_transmission_freq = center_freq_7 + BFSK_bound
# bit 2 = 0 
center_freq_2           = 10240     # Hz
bit_7_transmission_freq = center_freq_7 - BFSK_bound
# bit 1 = 1 
center_freq_1           = 9920      # Hz
bit_7_transmission_freq = center_freq_7 + BFSK_bound
# bit 0 = 1 
center_freq_0           = 9600      # Hz
bit_7_transmission_freq = center_freq_7 + BFSK_bound
```


<br>

#### JANUS
*Understanding JANUS is a very important part of the project. Luckily, the hard part of JANUS is done for us, that being the actual wave modulation and encoding (hard for me at least).*
<br>

##### What is JANUS?
JANUS is a NATO standardized method of communicating in the underwater channel. In simpler terms, it defines how NATO countries should send data underwater. 
<br>
<br>
The JANUS protocol details the use of *wake-up tones*, *32-bit preamble*, and *header packet* (with optional appended *cargo data* or payload). The packet headers are almost the same idea as to how internet packets work. Each sequence of bits has a different meaning for a node or receiver to understand, for instance, whether a message is an emergency distress signal, or just a friendly acknowledgement. These packets can be used to communicate a given message, or transmit detailed information in the appended cargo data section.
<br>
<br>
These packets then go through the defined JANUS transmission sequence generation, then waveform generation. To get a better idea of how JANUS works, please see the [JANUS module](/JANUS/README.md).
<br>

---

## Project our Group Received
*This project, as stated above, is to develop a working transmitter chain.*
<br>

**Provided Components**:
+ Zybo Z7-20 SoC (FPGA we used)
+ Filter Board
+ Amplifier Board
+ Underwater Transducer 


**Thus far, the system includes**: 
+ *On the FPGA*
    + PN Binary Generator
    + Binary Data Buffer
    + Forward Error Correction (FEC) Convolutional Encoder
    + Binary Frequency Shift Keying (BFSK)
    + Frequency Hopping
    + Passband Upconversion
        + This is where the carrier signal is introduced
    + Pulse Density Modulator (PDM)
+ *External from the FPGA*
    + Filter Board
    + Signal Amplifier
    + Transducer 
<br> 

Below is an illustration of the actual system.
<br>

![transmitter-chain](/img/transmitter-chain.png)

---

## What We have Done during our Capstone Project
As the project stands, there has been little done with the current chain. This project is a very research heavy implementation. As it turned out for our case, our idea of what we had to do switched many times as the scope of the project was broad and we did not absorb an entirely clear picture as for what our task was. 
<br>
<br>
Because of this, a great deal of time during our capstone project was spent researching and documenting our findings for the next team that takes on this development project can have a better starting point. 
<br>
<br>
Therefore, in this GitHub repository, there are many modules for getting to the point that we are currently at in the project. Some go into more detail than others, some are meant as reference guides for setting up the environment to work in, installing software, using software, and understanding the current state of the transmitter chain.
<br>
<br>
There is an order to which I would advice working through these modules as to ensure that each step is being completed.

1. Reading through this README\.md
2. Reading through JANUS Module
3. Setting up the development environment Module
4. Understanding the transmitter chain Module
5. Installing Vitis/Vivado Module
6. Installing Petalinux Module (Not everyone has to do this)<br>
a. Using Petalinux Module (Only for those that install Petalinux)<br>
b. Going from Petalinux Output to FPGA boot<br>
7. Using Vitus/Vivado Module
8. Driver Development Module
<br>

It is essential that all those participating in this project complete steps 1-4 to understand what is happening with the project.
<br>
<br>
It is also advised that, depending on whether you are computer or electrical, the Petalinux/Driver side of the project would be better for computer to take on. Vivado/transmitter chain would be better for Electrical to take on. 

---

## Future Work
As the project stands, our current plan was to replace the PN Binary Generator and Binary Data Buffer and replace them with a Memory Controller. What this would do is take data from memory in blocks of 1024 bits, and send them down the chain. Simple, right? Wrong. This is a grandiose idea to complete, however, making sure to implement each aspect of the JANUS in the proper way will prove difficult.
<br>
<br>

#### What is this Project Entails?
*To achieve this deliverable, there are several additions that must be made in different aspects of the project.*

##### What it would look like
Between our group and our external and internal supervisor, we opted to create an operating system on the microprocessor. This would utilize a driver that would handle the data to be stored into a specified memory address to be used by the hardware via a memory controller. This would be controlled by a bash command as below:

```bash
echo "Hello world!" > driver
```

This would leave a great deal of room for configuration, which is something the project sponsor, Ultra, was interested in. This could also be developed further with custom bash commands. All-in-all, we believe that this would satisfy the usability and extensive configuration that Ultra had desired from the project. 
<br>
<br>
Without the OS, the memory controller system would still be required, and in Vitis, you would also be able to simply scan a user. However, this would only allow for data transfer of strings, whereas the OS would allow for strings, images, data, any files to be transmitted.

#### To Do Breakdown
##### Vivado
1. Remove PN Binary Generator
2. Remove Binary Data Buffer
3. Implement Memory Controller <br>
a. Memory mapping must be done
4. Verify each aspect of the "black box" works as intended

##### Driver/Petalinux
1. Use Petalinux to build OS for Zybo Z7-20 <br>
a. For this, you can use Petalinux Build Module
2. Correspond with Memory Controller development to pick specified memory location
3. Develop driver to write data to memory location ***DYNAMICALLY***
<br>
<br>

While this is the proposed plan, you are able to complete this project however is agreed upon within the group and the sponsor, Ultra. 
<br>

---

## References
NATO. (2017, March 24). ***ANEP-87*** *Digital underwater signalling standard for network node discovery & interoperability.* Retrieved from **saiglobal.com**
<br>
<br>
Wikipedia. (n.d.). *Cyclic Redundancy Check*. Retrieved from **https://en.wikipedia.org/wiki/Cyclic_redundancy_check**