#strings are immutable in python
word1 = "I love"
word2 =  "python"

print(len(word2))

#concatenate
# print(word1 + " " + word2)
sentence = word1 + " " + word2
print(sentence)

# print(word2[1])
# print(word1[0])

# for ch in word2:
#     print(ch)


word = "python"
# word[0] = "j"  # strings can not be changed bcz strings are immutable
# print(word)
word = "java"
print(word)
print(word.upper(), word.lower())

chai = "   Masala Chai  "
print(chai.strip())

chai_two = "Lemon, Gingetr, Masala"
print(chai_two.replace("Lemon", "ginger"))
print(chai_two)

# it will convert chai_two into list
print(chai_two.split(",")) 

chai_two = "Masala Chai"
# it will provide index of first occurence of chai 
print(chai_two.find("Chai"))

chai = "Masala chai chai chai"
print(chai.count("chai"))

chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))