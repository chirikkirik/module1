my_dict = {"Alesya":2006, "Kirill":2005, "Denis":2018}
print(my_dict)
print(my_dict["Alesya"], my_dict.get("Alex"))
my_dict["Max"] = 2003
my_dict["Mike"] = 2012
print(my_dict.pop("Max"))
print(my_dict)

my_set = {1, 0, 0, 1, "Kirill", "Kirill",}
print((my_set))
my_set.add(2)
my_set.add(3)
print(my_set)
my_set.discard(3)
print(my_set)