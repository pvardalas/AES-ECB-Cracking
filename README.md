# AES-ECB Hash Cracking


### Author

- **Panagiotis Vardalas**

## Overview

The program takes input and then encrypts as shown below:
```
agent [input] wants to see [flag]
```
The target is to retrieve the flag.

## How the exploit works:

I exploited the fact that in ECB mode there is no randomness for each block, due to the lack of an IV. So I gave enough padding to separate the blocks and expose one byte of the flag at a time and brute-force it.
To understand it better, here is a representation bellow:

### This is the layout:
### Beginning:
```
agent cccccccccc 
c wants to see x <-- The block I am comparing where x is the byte I am brute-forcing
cccccccccccccccc
cccccccccccccccc end_padding (Leaving space for the whole flag to reveal
cccccccccccccccc
cccccccccccccccc
c wants to see x <-- The block I am comparing
```
### Close to the end:
```
agent c3c2dffdec
5a1107bca11e26_E
cccccccccccccccc
cccccccccccccccc
 wants to see d7
2ab5a083c2dffdec
5a1107bca11e26_E
```
