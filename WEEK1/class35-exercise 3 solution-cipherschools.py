name, char = input("enter comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}") # case sensitive
# Deepak - deepak
# D - d
