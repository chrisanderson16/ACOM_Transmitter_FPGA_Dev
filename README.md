*Written By: Chris Anderson*<br>
*Last Updated: November 18, 2023*

# Capstone Project: *ACOM Transmitter FPGA Development*
This is a project collaboration between Dalhousie University and Ultra Maritime ( *Nova Scotia's division of Ultra Electronics* ). The full project is to develop a transmitter chain to take user data to send across the underwater channel to the sister project, the ACOM Receiver. 
<br>
<br>
This project has had many hands on it over the years, most recently, as our capstone project. This repository is a collection of documentation and knowledge that we have gained over the duration of our time working on it. This README\.md file will detail the scope of the project as it stands, as well as, what each module (directory) entails. 
<br>

---

## Project Scope
The aim of this project, as briefly stated above, is to create an Acoustic Modem (ACOM) Transmitter by means of an FPGA board. This system will take input data, encode it, and modulate the signal, all in accordance with JANUS standards. It will finally be sent through a transducer to be transmitted across an underwater channel to a receiver.
<br>
<br>

##### JANUS
Understanding JANUS is a very important part of the project. Luckily, the hard part of JANUS is done for us, for the most part. 
<br>
<br>
The general flow chart of what happens with JANUS is shown below.

![janus-flow-chat](./img/JANUS_Packet_Encoding.jpg)

This is an important part of JANUS. This needs to be understood. The implementation we started with began at the CRC generator. This means that to implement an *ACTUAL* JANUS protocol in the system, our input data must be altered to meet the criteria. This must be done, following the JANUS bit allocation table, shown below.

![janus-bit-allocation](./img/JANUS_bit_allocation.jpg)

***So what does this all mean?*** This means that whenever we want to send a transmission, the first part of that transmission, *or packet*, must have the first 64 bits defined by the bit allocation table. The follow "cargo" data can be of any length, and does not require any other such bit allocations.
<br>
<br>
It is important to note that the cargo can follow the same convolutional encoding and interleaving, however, they are separately encoded and interleaved. 
<br>
<br>
Another important note is that there must ***NOT*** be any delay from the JANUS baseline packet and the cargo packet.
<br>
<br>
An aspect of the power reduction of JANUS is how it interacts with receivers and nodes. These nodes will be *sleeping*, or in a low power usage state when not in use and must be *awoken* by certain, preset tones. There is then a period where the node or receiver is given time to *wake up*. There is then a 32-bit sequence that essentially initializes the frequency hopping.
<br>
The sequence is as follows:
<br>
&emsp;&emsp;***{1,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0}*** <br>
After this sequence, the JANUS packet (*according to the bit allocation table*) is sent, followed by the cargo data. This is the data flow of JANUS.  Below is the data packet makeup for JANUS, followed by the frequency vs. time plot.

![janus-structure-packet-and-freq-v-time](/img/JANUS_packet_and_time_freq_structure.jpg)

NOTE FOR WRITING THIS DOC:
+ JANUS operates at 9440-13600Hz

---

## Current Project Developments (As they were when we started)
<p>
This project, as stated above, is to develop a working transmitter chain. Thus far, the system we were given includes: 
</p>

+ On the FPGA
    + PN Binary Generator
    + Binary Data Buffer
    + Forward Error Correction (FEC) Convolutional Encoder
    + Binary Frequency Shift Keying (BFSK)
    + Frequency Hopping
    + Passband Upconversion
        + This is where the carrier signal is introduced
    + Pulse Density Modulator (PDM)
+ External from the FPGA
    + Filter Board
    + Signal Amplifier
    + Transducer <br> 
<p>
<img align="left" src="./img/transmitter-chain.png">
&nbsp;
</p>
<p>
As the project stands, our current plan was to replace the PN Binary Generator and Binary Data Buffer and replace them with a Memory Controller. What this would do is take data from memory in blocks of 1024 bits, and send them down the chain. 
</p>
<p>
What this would mean is that rather than developing code in Vitis, we would opt to use Petalinux to create an OS on the FPGA. This would allow us to write a driver to write to memory with a bash command like: <br> 
</p>

```echo "Hello world!" > driver``` <br>

<p>
This would leave a great deal of room for configuration, which is something the project sponsor, Ultra, was interested in.
</p>