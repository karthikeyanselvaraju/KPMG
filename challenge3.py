import json
import re
import sys
from functools import reduce
def deep_get(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

def check_obj(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        sys.exit("Object is not expected format")

def check_key(k1):
    string_check= re.compile('[@_!#$%^&*()<>?\|}{~:]')
    if(string_check.search(k1) != None):
        sys.exit("Key is not in expected format.")

i1=input("Enter an Object : ")
check_obj(i1)
i1=json.loads(i1)

k1=input("Enter an Key : ")
check_key(k1)
k1=k1.replace("/",".")

print("Output:")
print(deep_get(i1, k1))    
