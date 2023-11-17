*Written By: Chris Anderson*<br>
*Last Updated: November 16, 2023*

# Capstone Project: *ACOM Transmitter FPGA Development*
<p>
This is a project collaboration between Dalhousie University and Ultra Maritime. The full project is to develop a transmitter chain to take user data to send across the underwater channel to the sister project, the ACOM Receiver. 
</p>
<p>
This project has had many hands on it over the years, most recently, as our capstone project. This repository is a collection of documentation and knowledge that we have gained over the duration of our time working on it. This README\.md file will detail the scope of the project as it stands, as well as, what each module (directory) entails. 
</p>

## Project Scope
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