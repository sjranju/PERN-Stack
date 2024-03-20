a = open('demo.txt')
# a.write("\nI am appending this line to Demo file")
print(a.read())
a.close()

with open('Demo3.txt', "a") as myfile:
    num = 1
    while(num < 4):
        contents = myfile.write(F"\n New line {num}")
        num += 1

with open('demo3.txt') as myfile:
    contents = myfile.read()
    print(contents)