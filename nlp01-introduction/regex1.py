import re

pattern1 = "abcdd"
# pattern1 = "9876 efg 98"
# pattern1 = "a"

print("occurences of any character: ",re.match(r".+",pattern1))
print("occurences of A_Za-z: ",re.search(r"[a-z]+",pattern1))
print("occurences of ab*: ",re.search(r"ab?",pattern1))

if re.match(r"[a-z]+",pattern1) != None:
    print("Match!")
else:
    print("No Match!")