# print(arg1, arg2, arg3, ,,, sep = " ", end="/n", file= "sys.stdout")

for i in range(5):
    print(i+1, end="")
print("")

# ord() convert character to ascii code
# chr() convert ascii code to character
print(ord('a'))

for i in range(29):
    n = i + 97
    print("ASCII code of character("+chr(n)+") is {}".format(n))

