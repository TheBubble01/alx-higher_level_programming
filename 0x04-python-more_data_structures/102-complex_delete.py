#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        new_d = {}
        for k, v in a_dictionary.items():
            if a_dictionary[k] != value:
                new_d[k] = v
        return new_d
