#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lk = []
    lv = []
    new_a = {}
    for k in a_dictionary:
        lk.append(k)
        lv.append(a_dictionary[k])
    if value in lv:
        for elem, mem in zip(lk, lv):
            if mem != value:
                new_a[elem] = mem
        return new_a
    return a_dictionary
