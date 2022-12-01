name = input("please enter your name ")
# deepak kumar singh

# deepak , len - 1 = 5
# name.count("d") , name.count(name[0]) = 1
# name.count("e") , name.count(name[1]) = 2
# name.count("e") , name.count(name[2]) = 2
# name.count("p") , name.count(name[3]) = 1
# name.count("a") , name.count(name[4]) = 1
# name.count("k") , name.count(name[5]) = 1

# output
# d : 1
# e : 2
# e : 2
# p : 1
# a : 1
# k : 1
temp_var = "d"

i = 0
while i < len(name):
    if name [i] not in temp_var:
        temp_var += name[i]
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1
