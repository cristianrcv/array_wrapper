#!/usr/bin/python

# -*- coding: utf-8 -*-

# For better print formatting
from __future__ import print_function

# Imports
import unittest


#
# UNIT TEST CASES
#

class TestArrayWrapper(unittest.TestCase):

    def test_basic_operations(self):
        from array_wrapper import ArrayWrapper
        size = 100
        a = ArrayWrapper(size)

        # Check basic setter and getter
        test_index = 10
        new_value = 1.0
        a.set_value_at_index(test_index, new_value)
        value_index = a.get_value_at_index(test_index)
        print("Value at " + str(test_index) + " should be " + str(new_value))
        print("Value at " + str(test_index) + " is " + str(value_index))
        assert (new_value == value_index)

        # Check address getter
        addr = a.get_address_of(test_index)
        value_addr = a.get_value_at_address(addr)
        print("Value should be " + str(new_value))
        print("Value at " + str(addr) + " is " + str(value_addr))
        assert (new_value == value_addr)

        # Check address setter
        new_value = 2.0
        a.set_value_at_address(addr, new_value)
        value_index = a.get_value_at_index(test_index)
        print("Value should be " + str(new_value))
        print("Value is " + str(value_index))
        assert (new_value == value_index)

        # Check resize
        size = 200
        a.resize(size)
        new_size = a.get_size()
        print("New size should be " + str(size))
        print("New size is " + str(new_size))
        assert (size == new_size)

    def test_memory_jumps(self):
        from array_wrapper import ArrayWrapper
        size = 100
        a = ArrayWrapper(size)

        # Compute addresses
        a_addrs = []
        for i in range(a.get_size()):
            a_addrs.append(a.get_address_of(i))

        # Compute jumps
        double_size = 8
        jumps = []
        i = 1
        while i < len(a_addrs):
            jump = a_addrs[i] - a_addrs[i - 1]
            print("JUMP FROM " + str(i - 1) + " TO " + str(i) + " IS: " + str(jump))
            assert (jump == double_size)
            i += 1

    def test_special_operations(self):
        from array_wrapper import ArrayWrapper
        size = 100
        a = ArrayWrapper(size)

        # Str
        print(a)
        print(str(a))

        # Length
        internal_size = len(a)
        print("Size should be " + str(size))
        print("Size is " + str(internal_size))
        assert (size == internal_size)

        # Get
        test_index = 50
        test_value = 1.0
        a.set_value_at_index(test_index, test_value)
        value_index = a.get_value_at_index(test_index)
        value_special = a[test_index]
        print("Value should be " + str(value_index))
        print("Value is " + str(value_special))
        assert (value_index == value_special)

        # Set
        test_value = 3.0
        a[test_index] = test_value
        value_index = a.get_value_at_index(test_index)
        print("Value should be " + str(test_value))
        print("Value is " + str(value_index))
        assert (test_value == value_index)

        # Contains
        if test_value in a:
            print("Value " + str(test_value) + " is contained")
        else:
            print("Value " + str(test_value) + " is missing!!")
            assert (False)

        # Iterator
        a_elements = []
        for elem in a:
            a_elements.append(elem)
        print("A should have " + str(size) + " elements")
        print("A has " + str(len(a_elements)) + " elements")
        assert (size == len(a_elements))


#
# MAIN FOR UNIT TEST
#

if __name__ == '__main__':
    unittest.main()
