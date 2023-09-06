class SuperList():
    def __len__(self):
    return 1000
    
super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))

# access through index - special dunder method - modify it and have it return no matter what 1000