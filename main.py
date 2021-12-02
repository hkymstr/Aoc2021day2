

print("AoC2021 day2 part 1")

x = 0  #horizontal
y = 0  #vertical

file1 = open('inputday2.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
#    print("Line{}: {}".format(count, line.strip()))


    if "forward" in line:
    #    print("add horizontal")
        for c in line:
            if c.isdigit():
                x = x + int(c)
   #             print ("x =",x)

    if "up" in line:
  #      print("reduce depth")
        for c in line:
            if c.isdigit():
                y = y - int(c)
 #               print ("y =",x)

    if "down" in line:
#        print("add depth")
        for c in line:
            if c.isdigit():
                y = y + int(c)
 #               print("y =", x)



print("done.......")
print("x=",x)
print("y=",y)
print(x*y)



print("AoC2021 day2 part 2")

x = 0  #horizontal
y = 0  #vertical
aim = 0
depth = 0

file1 = open('inputday2.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
#    print("Line{}: {}".format(count, line.strip()))


    if "forward" in line:
    #    print("add horizontal")
        for c in line:
            if c.isdigit():
                x = x + int(c)
                depth = depth + (aim*int(c))
   #             print ("x =",x)

    if "up" in line:
  #      print("reduce depth")
        for c in line:
            if c.isdigit():
                y = y - int(c)
                aim = aim - int(c)
 #               print ("y =",x)

    if "down" in line:
#        print("add depth")
        for c in line:
            if c.isdigit():
                y = y + int(c)
                aim = aim + int(c)
 #               print("y =", x)



print("done.......")
print("depth=",depth)
print("horizontal=",x)
print(depth*x)