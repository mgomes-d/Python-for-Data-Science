ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

del ft_tuple
ft_tuple = ("Hello", "Belgium!")

ft_set.remove("tutu!")
ft_set.add("Brussels") 

ft_dict["Hello"] = "19"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)