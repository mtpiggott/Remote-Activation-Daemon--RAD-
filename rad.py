#! /usr/bin/python
'''
    File:        rad.py
    Description: Main file of the Remote Activation Daemon
    Author:      Michael Piggott
    Date:        10/31/2011
'''
import messageInterface

def main():
    while 1 == 1:
        #do stuff
        message = messageInterface.recieveMessage()

if __name__ == '__main__':
    main()
