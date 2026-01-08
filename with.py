# With_HW.py

with open("example.txt", "r") as file:
    contents = file.read()

print(contents)


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


with open("example.txt", "r") as file:
    lines = file.readlines()

with open("output.txt", "w") as output:
    for line in lines:
        output.write(line.upper())
