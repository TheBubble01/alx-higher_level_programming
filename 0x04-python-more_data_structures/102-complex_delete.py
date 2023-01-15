#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        new_d = {}
        for k, v in a_dictionary.items():
            if v != value:
                new_d[k] = v
        return new_d
