my_dict ={"John":1, "Michael":2, "Shawn":3}
 
list_of_key = list(my_dict.keys())
list_of_value = list(my_dict.values())
 
position = list_of_value.index(1)
print(list_of_key[position])
 
position = list_of_value.index(2)
print(list_of_key[position])