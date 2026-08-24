info = {
    "name": "Shardha",
    "subject" : ["math", "science"],
    "cgpa": 9.2,
    3.14: "PI"
}

print(info)
print(type(info))
print(info[3.14])
print(info["name"])

# dictionary is mutable
info["cgpa"] = 9.6
print(info["cgpa"])