#!/usr/bin/python3
"""Contains function class_to_json"""
import json


def class_to_json(obj):
    """Returns a dictionary description of a class object"""
    jsonObj = json.dumps(obj.__dict__)
    return jsonObj
