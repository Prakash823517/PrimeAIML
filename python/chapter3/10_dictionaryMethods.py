info = {
    "name": "Shardha",
    "subject" : ["math", "science"],
    "cgpa": 9.2,
    3.14: "PI"
}

for val in info:
    print(val)

for key, value in info.items():
    print(key, ":",  value)
    
print(info.keys())

# to convert into list
dict_keys = list(info.keys())
print(dict_keys)
print(type(dict_keys))

print(info.values())

print(info.items())

print(info.get("cgpa"))
print(info.get("cgpa2"))

info.update({
    "city": "Delhi"
})
print(info)
