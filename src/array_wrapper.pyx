#!/usr/bin/python

# -*- coding: utf-8 -*-

# For better print formatting
from __future__ import print_function

# Imports
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free


cdef class ArrayWrapperIterator:
    cdef ArrayWrapper arrayWrapper
    cdef unsigned int current_index
    cdef unsigned int end_index

    # Constructor
    def __cinit__(self, arrayWrapper):
        self.arrayWrapper = arrayWrapper
        self.current_index = 0
        self.end_index = arrayWrapper.get_size()

    # Iterator
    def __next__(self):
        if self.current_index < 0 or self.current_index >= self.end_index:
            raise StopIteration

        value = self.arrayWrapper.get_value_at_index(self.current_index)
        self.current_index = self.current_index + 1
        return value


cdef class ArrayWrapper:

    # Internal class attributes
    cdef double* data

    cdef size_t num_elements
    cdef size_t array_size

    cdef unsigned int base_addr
    cdef unsigned int max_addr

    # Constructor
    def __cinit__(self, size_t num_elements):
        '''
        Allocate num_elements * sizeof(double) bytes without initialization

        Arguments:
            - :param num_elements: New number of double elements of the array
        Return:
            - :return None
        Raise
            - MemoryError : If the array cannot be allocated
        '''

        # Allocate memory
        array_size = num_elements * sizeof(double)
        mem = <double*> PyMem_Malloc(array_size)
        if not mem:
            raise MemoryError()

        # Store information in internal structures
        self.data = mem

        self.num_elements = num_elements
        self.array_size = array_size

        self.base_addr = <unsigned int> &self.data[0]
        self.max_addr = self.base_addr + self.array_size

    # Destructor
    def __dealloc__(self):
        '''
        Free the memory used by the internal structure

        Arguments:
            - :param self:
        Return:
            - :return None
        Raise:
        '''

        # Free internal array. The rest of the structures are plain, no need to free
        PyMem_Free(self.data)

    # Resizer
    def resize(self, size_t num_elements):
        '''
        Allocate num_elements * sizeof(double) bytes, preserving the current content
        and making a best-effort to re-use the original data location

        Arguments:
            - :param num_elements: New number of double elements of the array
        Return:
            - :return None
        Raise
            - MemoryError : If the array cannot be re-allocated
        '''

        # Allocate memory
        new_array_size = num_elements * sizeof(double)
        mem = <double*> PyMem_Realloc(self.data, new_array_size)
        if not mem:
            raise MemoryError()

        # Store information in internal structures
        self.data = mem

        self.num_elements = num_elements
        self.array_size = new_array_size

        self.base_addr = <unsigned int> & self.data[0]
        self.max_addr = self.base_addr + self.array_size

    # Getters
    def get_size(self):
        '''
        Returns the size of the internal array

        Arguments:
        Return:
            - :return Size of the internal array
        Raise
        '''

        return self.num_elements

    def get_value_at_index(self, size_t index):
        '''
        Returns the value stored at the specified index of the internal array

        Arguments:
            - :param index: Array index between 0 and num_elements
        Return:
            - :return The value stored at the specified index of the array
        Raise
            - Exception : If the index is out of the array bounds
        '''

        if index < 0 or index >= self.num_elements:
            raise Exception("ERROR: Array access index out of bounds")

        return self.data[index]

    def get_value_at_address(self, unsigned int addr):
        '''
        Returns the value stored at the specified memory address

        Arguments:
            - :param addr: Memory address between the start and the end of the internal array
        Return:
            - :return The value stored at the specified memory address of the array
        Raise
            - Exception : If the memory address is out of the array bounds
        '''

        if addr < self.base_addr or addr >= self.max_addr:
            raise Exception("ERROR: Array access memory address out of bounds")

        index = (addr - self.base_addr) / sizeof(double)
        return self.data[index]

    def get_address_of(self, size_t index):
        '''
        Returns the memory address of the specified index element in the internal array

        Arguments:
            - :param index: Array index between 0 and num_elements
        Return:
            - :return The memory address of the specified index element in the internal array
        Raise
            - Exception : If the index is out of the array bounds
        '''

        if index < 0 or index >= self.num_elements:
            raise Exception("ERROR: Array access index out of bounds")

        return <unsigned int> &self.data[index]

    # Setter
    def set_value_at_index(self, size_t index, double value):
        '''
        Sets a new value for the specified index of the internal array

        Arguments:
            - :param index: Array index between 0 and num_elements
            - :param value: New value
        Return:
            - :return None
        Raise
            - Exception : If the index is out of the array bounds
        '''

        if index < 0 or index >= self.num_elements:
            raise Exception("ERROR: Array access index out of bounds")

        self.data[index] = value

    def set_value_at_address(self, unsigned int addr, double value):
        '''
        Sets a new value for the specified memory address of the internal array

        Arguments:
            - :param addr: Memory address between the start and the end of the internal array
            - :param value: New value
        Return:
            - :return None
        Raise
            - Exception : If the memory address is out of the array bounds
        '''

        if addr < self.base_addr or addr >= self.max_addr:
            raise Exception("ERROR: Array access memory address out of bounds")

        index = (addr - self.base_addr) / sizeof(double)
        self.data[index] = value

    # Special methods
    def __str__(self):
        '''
        Returns the string representation of the object

        Arguments:
        Return:
             - :return String representation of ArrayWrapper
        Raise
        '''

        s = "ArrayWrapper[" \
            + "size=" + str(self.num_elements) \
            + ", base_addr=" + str(self.base_addr) \
            + ", max_addr=" + str(self.max_addr) \
            + "]"
        return s

    def __iter__(self):
        '''
        Returns an iterator for the object

        Arguments:
        Return:
             - :return An iterator for the object
        Raise
        '''

        return ArrayWrapperIterator(self)

    def __len__(self):
        '''
        Returns the number of elements of the object

        Arguments:
        Return:
             - :return The number of elements of the object
        Raise
        '''

        return self.get_size()

    def __getitem__(self, index):
        '''
        Returns the element stored in the given index

        Arguments:
            - :param index: Array index between 0 and num_elements
        Return:
             - :return The element stored in the given index
        Raise
        '''

        return self.get_value_at_index(index)

    def __setitem__(self, index, value):
        '''
        Sets a new value for the element stored in the given index

        Arguments:
            - :param index: Array index between 0 and num_elements
            - :param value: New value
        Return:
        Raise
        '''

        self.set_value_at_index(index, value)

    def __contains__(self, value):
        '''
        Returns if the object contains the given value or not

        Arguments:
            - :param value: Value to look for
        Return:
             - :return True if the object contains the given value. False otherwise
        Raise
        '''

        for index in range(0, self.num_elements):
            if self.data[index] == value:
                return True
        return False
