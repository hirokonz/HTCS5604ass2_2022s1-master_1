import unittest
import functions


class Test_functions(unittest.TestCase):  # Task 1: Unit Test - test 5 functions in "functions.py".

    def test_isAInt(self):  # UT1: verify the parameter is a number.

        number = functions.isAInt(1)  # positive number
        self.assertTrue(number)

        number = functions.isAInt(-1)  #negative number
        self.assertTrue(number)

        number = functions.isAInt(1.5)  #positive decimal number
        self.assertTrue(number)

        number = functions.isAInt(-1.5)  #negative decimal number
        self.assertTrue(number)

        number = functions.isAInt(0)  # 0
        self.assertTrue(number)

        number = functions.isAInt("1")  # String number
        self.assertTrue(number)

        number = functions.isAInt("Alphabet")  #string
        self.assertFalse(number)

        number = functions.isAInt("&&")  #special character
        self.assertFalse(number)

        number = functions.isAInt("")  #Null
        self.assertFalse(number)

    def test_isValidChoice(self):  # UT2: verify the parameter is selected from choices ["1", "2", "3", "4", "5", "6"]

        choice = functions.isValidChoice("1")
        self.assertTrue(choice)

        choice = functions.isValidChoice("2")
        self.assertTrue(choice)

        choice = functions.isValidChoice("3")
        self.assertTrue(choice)

        choice = functions.isValidChoice("4")
        self.assertTrue(choice)

        choice = functions.isValidChoice("5")
        self.assertTrue(choice)

        choice = functions.isValidChoice("6")
        self.assertTrue(choice)

        choice = functions.isValidChoice("7")  #parameter outside of list
        self.assertFalse(choice)

        choice = functions.isValidChoice("0")  # parameter is 0
        self.assertFalse(choice)

        choice = functions.isValidChoice(1)  #parameter is within 1-6 but an integer 1
        self.assertFalse(choice)

        choice = functions.isValidChoice(3)  #parameter is withing 1-6 but an integer 3
        self.assertFalse(choice)

        choice = functions.isValidChoice(8)  #parameter is outside of list and integer 8
        self.assertFalse(choice)

        choice = functions.isValidChoice("Alphabet")  #parameter is alphabet string
        self.assertFalse(choice)

    def test_isValidName(self):  # UT3: verify that the length of parameter is greater than 0 and less than or equal 30

        name = functions.isValidName("Hiroko Hodge")  # Length 13
        self.assertTrue(name)

        name = functions.isValidName("a")  #length 1
        self.assertTrue(name)

        name = functions.isValidName("Hiroko Hiroko Hiroko Hiroko 12")  # length 30
        self.assertTrue(name)

        name = functions.isValidName(" ")  #length blank 1
        self.assertTrue(name)

        name = functions.isValidName("")  #length 0
        self.assertFalse(name)

        name = functions.isValidName("isValidName isValidName isValidName isValidName ")  #length over 30
        self.assertFalse(name)

    def test_isValidPosition(self):  # UT4: verify the parameter is one of "Guard", "Forward" or "Centre"
        position = functions.isValidPosition("Guard")  #option one
        self.assertTrue(position)

        position = functions.isValidPosition("Forward")  #option two
        self.assertTrue(position)

        position = functions.isValidPosition("Centre")  #option three
        self.assertTrue(position)

        position = functions.isValidPosition("Catcher")  #parameter is not one of three options
        self.assertFalse(position)

        position = functions.isValidPosition("guard")  #parameter is guard but small case
        self.assertFalse(position)

        position = functions.isValidPosition(" ")  #blank parameter
        self.assertFalse(position)

        position = functions.isValidPosition("1")  #parameter is number
        self.assertFalse(position)

    def test_isValidInputNumber(self):  # UT5: verify the number is between minNum & MaxNum or equal to minN & maxN.
        valid_number = functions.isValidInputNumber(50, 10, 100)  # number is mid-range within the boundary
        self.assertTrue(valid_number)

        valid_number = functions.isValidInputNumber(10, 10, 100)  #number = minNum
        self.assertTrue(valid_number)

        valid_number = functions.isValidInputNumber(100, 10, 100)   #number = maxNum
        self.assertTrue(valid_number)

        valid_number = functions.isValidInputNumber(9, 10, 100)  #number is lower side of out of boundary range
        self.assertFalse(valid_number)

        valid_number = functions.isValidInputNumber(101, 10, 100)  #number is higher side of out of boundary range
        self.assertFalse(valid_number)


if __name__ == '__main__':
    unittest.main()
