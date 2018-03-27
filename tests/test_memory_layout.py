#!/usr/bin/python

# -*- coding: utf-8 -*-

# For better print formatting
from __future__ import print_function

import numpy as np
import gc
import weakref


def print_info(name, iden, hex, inthex):
    print("-------------------------------")
    print("NAME: " + str(name))
    print("ID:   " + str(iden))
    print("HEX:  " + str(hex))
    print("INT:  " + str(inthex))
    print("-------------------------------")


def inspect_structure(l, n, more_info=False):
    # Show content
    if more_info:
        print(l)
        print("")

    # Check memory storage
    id_l = id(l)
    hex_l = hex(id_l)
    int_hex_l = int(hex_l, 16)
    if more_info:
        print_info("l", id_l, hex_l, int_hex_l)

    l_ids = []
    for i in range(n):
        elem = l[i]
        name_elem = "l[" + str(i) + "]"
        id_elem = id(elem)
        hex_elem = hex(id_elem)
        int_hex_elem = int(hex_elem, 16)

        l_ids.append(id_elem)

        if more_info:
            print_info(name_elem, id_elem, hex_elem, int_hex_elem)

    # Check ids
    if more_info:
        print("")
        print("-------------------------------")
        for i in range(n):
            print("ID( l[" + str(i) + "] ): " + str(l_ids[i]))

    # Check offsets
    if more_info:
        print("")
        print("-------------------------------")
    l_offsets = []
    for i in range(n):
        elem = l[i]
        id_elem = id(elem)
        offset = id_elem - id_l
        l_offsets.append(offset)

        if more_info:
            print("OFFSET from " + str(i) + " to base: " + str(offset))

    # Check jumps
    if more_info:
        print("")
        print("-------------------------------")
    l_jumps = []
    for i in range(1, n):
        jump = l_offsets[i] - l_offsets[i - 1]
        l_jumps.append(jump)

        if more_info:
            print("JUMP FROM " + str(i - 1) + " to " + str(i) + ": " + str(jump))

    # Check non-constant jumps
    set_l_jumps = set(l_jumps)
    num_diff = len(set_l_jumps)
    print("NON CNST JUMPS: " + str(num_diff))
    print("JUMP VALUES: " + str(set_l_jumps))


def inspect_array(mat):
    ids = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            ids.append(id(mat[i][j]))
            # print("mat [" + str(i) + ", " + str(j) + "] = " + str(id(mat[i][j])))

    i = 1
    jumps = []
    while i < len(ids):
        jump = ids[i] - ids[i - 1]
        jumps.append(jump)
        # print("JUMP " + str(jump))
        i += 1

    print(set(jumps))


#
# FUNCTIONS TO RETRIEVE OBJECTS FROM IDs
#


def objects_by_id(id_):
    # Retrieves an object by ID
    # It goes through all the Garbage Collector listed objects (performance?)
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj
    raise Exception("No found")


_id2obj_dict = weakref.WeakValueDictionary()


def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid


def id2obj(oid):
    return _id2obj_dict[oid]


#
# LAUNCH INSPECT TESTS
#

def launch_inspect_tests():
    # Parameters
    n = 100
    tries = 5

    # Test1
    import copy

    for t in range(tries):
        generator1 = (copy.copy(np.array(np.random.random((2, 2)), dtype=np.double, copy=False)) for _ in range(n))
        l1 = list(generator1)

        print("# TEST 1 # TRY " + str(t))
        inspect_structure(l1, n, more_info=False)
        print("################################")

        del generator1
        del l1

    # Test2
    print("")
    for t in range(tries):
        l2 = []
        for _ in range(n):
            a = np.array(np.random.random((2, 2)), dtype=np.double, copy=False)
            l2.append(a)

        print("# TEST 2 # TRY " + str(t))
        inspect_structure(l2, n, more_info=False)
        print("################################")

        del l2

    # Test3
    print("")
    for t in range(tries):
        l3 = [np.zeros((2, 2))] * n
        for i in range(n):
            a = np.array(np.random.random((2, 2)), dtype=np.double, copy=False)
            l3[i] = a

        print("# TEST 3 # TRY " + str(t))
        inspect_structure(l3, n, more_info=False)
        print("################################")

        del l3

    # Test4
    print("")
    import array
    import random

    for t in range(tries):
        generator4 = (random.random() for _ in range(n))
        l4 = array.array('f', generator4)

        print("# TEST 4 # TRY " + str(t))
        inspect_structure(l4, n, more_info=False)
        print(l4.buffer_info())
        print("################################")

        del generator4
        del l4

    # Test5
    print("")
    for t in range(tries):
        l5 = [np.array(np.random.random((2, 2)), dtype=np.double, copy=False) for _ in range(n)]

        print("# TEST 5 # TRY " + str(t))
        inspect_structure(l5, n, more_info=False)
        print("################################")

        del l5

    # Test6
    print("")
    for t in range(tries):
        l6 = np.random.random((n, n))

        print("# TEST 6 # TRY " + str(t))
        inspect_array(l6)
        print("################################")

        del l6


if __name__ == "__main__":
    launch_inspect_tests()
