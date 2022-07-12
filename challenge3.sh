#! /bin/bash
# Read the input from command line
getobject()
{
while [[ -z "$obj" ]]
 do
  echo "Enter the Object value:"
  read obj
  if jq -e . >/dev/null 2>&1 <<<"$obj"; then
        object_val=$obj
  else
        echo "Input is not an valid JSON"
        obj=""
  fi
 done
}

getkey()
{
  while [[ -z "$key" ]]
  do
    echo "Enter the Key value : "
    read key
    if [[ $key == *['!'@#$%^\&*()_+]* ]]
    then
     echo "Enter a valid Key"
     key=""
    else
     key_val=$key
    fi
  done
}

findjsonvalue()
{
  testkey=`echo $key_val | grep '/'`
  if [ -n "$testkey" ]; then 
     key=`echo $key_val | sed "s/\//./g"`
     echo $object_val | jq ".${key}"
  else
    echo $object_val | jq ".${key_val}"
  fi
}

getobject
getkey
findjsonvalue $object_val $key_val


