from unittest import result
import requests
import json

#initial url of metadata(Dont include meta-data here as we need some arg to send initially)
base_url = 'http://169.254.169.254/latest/'


def check_json(jsonoutput):
    try:
        json.loads(jsonoutput)
    except ValueError:
        return False
    return True


def loop_each_data(url, key):
    output = {}  #initialize the dict
    for item in key:     #loop till all the data processed
    #    print[item]
        new_url = url + item
        result = requests.get(new_url)
        text = result.text
        if item[-1] == "/":
            list_of_values = result.text.splitlines()
            output[item[:-1]] = loop_each_data(new_url, list_of_values)
      #      print(output)
        elif check_json(text):
            output[item] = json.loads(text)
        else:
            output[item] = text
    return output

def get_full_metadata():
   # actual_metadata = get_all_metadata()
    initial = ["meta-data/"]
    actual_metadata = loop_each_data(base_url, initial)
    metadata_as_json = json.dumps(actual_metadata, indent=4) #pass the complete objects to convert it to JSON
    return metadata_as_json  #return the converted json string


#start the trigger here
if __name__ == '__main__':
    print(get_full_metadata())   #call the operation
  # get_full_metadata()

