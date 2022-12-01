# name = "     Deep       ak     "
# dots = "..............."
# lstrip() method
# print(name + dots)
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip() + dots)
# print(name.replace(" ", "") + dots)

name, char = input("enter comma separated name and character : 3").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}") # case senitve
# Deepak - deepak
# D - d
# " Deepak " -----> "Deepak" -------> "deepak"
# "  D " ------>"D" --------> "d"
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()