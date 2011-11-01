#! /usr/bin/python

'''
    File: radTest.py
    Description: Tests rad.py
'''

# imports
import unittest
import rad

class testRecieveMessage(unittest.TestCase):

    def setUp(self):
        pass

    #Test Casses for RecieveMessage
    def testPioneers(self):
        testMessage = "pioneers start"

        message = rad.recieveMessage()

        self.assertEqual(message, testMessage)


if __name__ == '__main__':
    unittest.main()
