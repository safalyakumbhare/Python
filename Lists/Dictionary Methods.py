d = { "faculties" :{"BA": "Bhagyshree Ambulkar", "DS": "Dhiraj Shembekar", "RI": "Rekha Israni"},"SJ":"Sudhir Juare"}

print(
    "The Value of the key BA is : ", (d["faculties"]["BA"])
)  # Printing  the value by using key name i.e., BA, DS etc..
print(
    "The all keys are : ", d.keys()
)  # Printing  all keys present inside dictionary using Key() Method
print(
    "THe ALL Values are : ", list(d.values())
)  #  Printing all values present inside Dictionary using Values() Method
print(list(d.items()));
# Printing All items (Key-Value pairs) in a Dictionary using Items() method
print(d.get("LP"))   # If any  one provide key which is not available in the Dictionary it will return None otherwise It will print the corresponding Value for that particular Key.