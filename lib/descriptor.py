from pkg_resources import resource_string
from collections import namedtuple
import json

def Descriptor(package, json_filename):
    json_str = resource_string(package, json_filename)
    json_dic = json.loads(json_str)
    return namedtuple("Descriptor", json_dic.keys())(**json_dic)
