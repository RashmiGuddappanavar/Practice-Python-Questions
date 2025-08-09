# Reverse a string without using slicing ([::-1]).

input_ = input("Enter a String: ")
result = ""
i = 0
while (i < len(input_)):
    result = input_[i]+result
    i += 1
print(result)
