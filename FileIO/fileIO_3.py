import struct

# Packing values to bytes
# The first parameter is the format string. Here it specifies the data is structured
# with a single four-byte integer followed by two characters.
# The rest of the parameters are the values for each item in order
binary_data = struct.pack("i5s15s", 8499000, b'Hello', b'My name is Joon')
print(binary_data)

# When unpacking, you receive a tuple of all data in the same order
tuple_of_data = struct.unpack("i5s15s", binary_data)
text = str(tuple_of_data[1])
print(text)
print(tuple_of_data[1].decode('utf-8'))

# For more information on format strings and endiannes, refer to
# https://docs.python.org/3.5/library/struct.html

print(b'hello')

text = b'thithere'
print(text)

