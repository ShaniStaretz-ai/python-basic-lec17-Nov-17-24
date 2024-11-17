# python-basic-lec17-Nov-17-24
dictionary functions
## subjects learned:
* keys()- return a *dict_list* type of the dictionary's keys - 
  * better turn it to list(dict.keys())
  * can be run on it with foreach.
* items()-  returns a list of tuples (key,value)-read only:- 
  * better turn it to list(dict.items())
* values()- returns dict_values types of the dictionary's values
  * better turn it to list(dict.values())
* unpack value - term for separate a list for its values: x,*y
    ```
    l=[[1,2,3,4][1]]
    for x,*y in l:
    x=l[0]=1, y=[2,3,4]
    x=l[0]=1 y=[]
  for key,value in dict.items()
    ``` 
* copy(): duplicate a dictionary: assign to new parameter is only copy by reference.
* fromkeys([<keys>],value-initvalues)- will create a new dictionary with the giving keys list
  * with init value/None(DEFAULT, if not giving)
  ```
  new_d=dict.fromkeys([key1....])
  new_d=exist_dict_name(exit_dict_name.keys()
  ```
* pop(key_name)= remove to key from the dictionary and returns it's value
* len(dictionary)= returns the total count of keys
* str(dictionary)-JSON.stringify() in js- to convert dictionary to string.
* 
## extra subjects:
 * max function can receive a dictionary and a lambda function. 
 * the function enumerate() is a usage of the term unpacking , on list

