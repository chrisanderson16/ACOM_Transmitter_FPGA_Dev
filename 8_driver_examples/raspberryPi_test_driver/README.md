*Written By: Chris Anderson* <br>
*Last updated: November 29, 2023*
<br>

# Contents of this module

This module is meant as an example to give you an idea on how drivers work. The easiest way to understand drivers is to think of them as portals. They are usable in user space (i.e., the space that any user can have access to) and they navigate through kernel space to adjust hardware. 
<br>
<br>
There are three aspects to see in this module, one is the [Makefile](./Makefile), the second is the C code for the actual driver, [mymodule.c](./mymodule.c), and the final is the build object files that can be used to mount the created driver.
<br>

---

###### IMPORTANT NOTE: This example was completed on a Raspberry Pi 4b, it may not (most definitely will not) work on other linux distributions.

---

<br>

This was an example I went through to see how driver creation worked. I followed [this guide](https://www.youtube.com/watch?v=lWzFFusYg6g&list=PLc7W4b0WHTAX4F1Byvs4Bp7c8yCDSiKa9&index=1) by **Low Level Learning** almost exactly to create my drivers. I recommend watching this as it gives you an idea into how create drivers works. However, again, it is important to note that this was done on a Raspberry Pi. Methods of creating drivers differs between distributions and almost entirely relies on the kernel that your linux system is using. 
<br>
<br>
Because this was entirely from the above linked video, I will provide you the code that was used, including the C file, Makefile and output that should be received. I will not be provided step-by-step instructions as it would more or less be the same (if not worse) that how it is explained in the video.