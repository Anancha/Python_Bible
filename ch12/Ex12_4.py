my_file = open("bfile.bin", "wb+")
str = b"one two three"
num = b"[1, 2, 3]"
my_file.write(str)
my_file.write(num)
my_file.seek(0)
bdata = my_file.read()
print("Binary Data:", bdata)
my_file.close()