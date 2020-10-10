# Media Access control (MAC)

## Definition
* MAC (Media Address Control) address is a unique address which is provided by the manufacture in ethernet card, wireless card or any other which provides access to the network. It helps to protect the device integrity by not having same address with respect to other devices which is used all around the globe. Either you plug in the same network device to another computer it will have the same address. 

## Why we need this ?

* To protect our computing device from being recognized on a network. 
* This provide a greater level of anonymity over the internet.
* This gives information about network cards and MAC addresses of the interface.

## Change your MAC maually
 ```bash
    anon@localhost$ ifconfig
    anon@localhost$ ifconfig eth0 down 
    anon@localhost$ ifconfig eth0 hw ether 00:00:44:55:22:00
    anon@localhost$ ifconfig eth0 up
 ```

## 

