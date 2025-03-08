file = open("sample.txt", "r")

#data = file.read()  # for 1 file we can use read function only one time.

data = file.read(2)

print(data)

data = file.readline()

print(data)

data = file.readline()

print(data)

file.close()