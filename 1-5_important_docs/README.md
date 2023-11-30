*Written By: Chris Anderson and Michelle Yee* <br/>
*Last Updated: November 29, 2023*<br/>



### What this Module Contains
The following will be a brief overview of what is contained within this directory.

##### What is VHDL Code?
VHDL stands for *VHSIC Hardware Description Language*. <br/>
VHSIC stands for *Very High Speed Integrated Circuits Program* <br/>


### vivado_system_all_proj.zip
Moving on, this module/directory contains a variety of research, skills and understanding we have collected over our time with this project. The most important item of note is the file [vivado_system_all_proj.zip](./vivado_system_all_proj.zip). This zip file contains all of the Vivado projects for the current transmitter chain that was provided for us by Dr. Bousquet. The first item of the zip is another zip file labelled *BFSK_Transmitter_DCA.xpr.zip*. This file is the actual transmission chain. The other ".xpr" files are components held within the actual transmission chain. It would be a good idea, and good practice to take a look at these, however, they are somewhat intimidating. 
<br/>
<br/>

The other items contained in the *vivado_system* zip is other work completed by other groups on this project. We did not reference many of them, as they were not as important for our research. 

<br/>

### Import_time.m & time1.csv
These files are output from the board itself running the transmission chain and how we can observe and verify the output. It can be interesting to look at to see what the output of the board, in hold, looks like. Specifically, [Import_time.m](./Import_time.m) is used to analyze [time1.csv](./time1.csv).


### CodeComments_Cleanedup.pdf
[This pdf](./CodeComments_Cleanedup.pdf) is one of the largest contributions that we could make, and took most of our final semester to create. This contains many of the configurable parameters, functions, values, etc. that may be required to alter the output of the transmission system. This was important as the client wishes to have the system to be JANUS compatible, whereas the transducer we have at our disposal is not. Therefore, we must be able to create a way that our client can take our findings, and implement them accordingly without having to spend too long on understanding the current code. 
<br/>
<br/>
This document outlines the different files that make up the Transmitter_TL project. Each component includes its position in the hierarchy, a brief description of its functionality and what sections can be modified when meeting different specifications. General notes are added to further understanding.
<br/>
Most of the information in this table has been obtained from the [Acoustic B-FSK Link Design report](./Acoustic_B-FSK_Link_design_report.pdf) and online resources. Please make reference to that document for a more detailed explanation of all VHDL files.

### CustomAmplifierBoardPres.pdf
This document explains and shows how the amplifier board works that will be used to modulate the signal of the completed JANUS packet + Cargo packet. This is necessary for the transducer as the signal from the FPGA output is not nearly strong enough as it must be. 
<br>
It also shows the filter board. It does a little explanation of the both of them as to what they are doing with the FPGA output. It is the ADC so that the transmission chain can output an acoustic wave via the transducer.




