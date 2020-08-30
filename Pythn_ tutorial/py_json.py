import json

# Parse JSON - Convert from JSON to Python
print("-- Convert from JSON to Python --")
x = '{"name":"Harish","age":28,"city":"Patiala"}'
y = json.loads(x)
print("Name:", y["name"], ",city:", y["city"], ",age:", y["age"])

# Convert from Python to JSON
print("-- Convert from Python to JSON --")
person = {
    "name": "Maise",
    "age": 21,
    "profession": "actresss"
}
js = json.dumps(person)
print(js)

# convert Python Object into JSON Strings

# 1. dict 2. list 3. tuple 4. string 5. int 6. float 7. True 8. False 9. None
print("-- Convert Python object into JSON String --")
print(json.dumps({"name": "Sophie", "age": 30}))
print(json.dumps(['apple', 'banana']))
print(json.dumps(('mango', 'cherry')))
print(json.dumps("Python"))
print(json.dumps(786))
print(json.dumps(78.6))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert Python object contain all legal datatype

x = {
    "name": "John",
    "age": 30,
    "married": "True",
    "divorced": "False",
    "children": ("anne", "billy"),
    "pets": "None",
    "cars": [
        {"model": "BMW", "year": 1984},
        {"model": "Toyota", "year": 1995}
    ]
}

print("-- Convert Python object contain all legal datatype --")
print(json.dumps(x))

# Format the Result

print("-- Format the Result --")
print(" Exmple 1")
print(json.dumps(x, indent=4))
print(" Exmple 2")
print(json.dumps(x, indent=4, separators=("-", "=")))

# Order the Result
print("-- Order the Result --")
print(json.dumps(x, sort_keys=True))
