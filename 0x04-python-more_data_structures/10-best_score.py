#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key in enumerate(sorted(a_dictionary.keys())):
            return key[-1]
