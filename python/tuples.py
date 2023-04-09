# Tuple  :  ordered , immutable , allows duplicate 

mytuple ={"MAx", 28, "Dost"}

print(mytuple)

for i  in  mytuple:
    print(i )
    
if 20 in mytuple:
    print("Yessss ")
else :
    print("Noooooo")
    



print("Now converting tuple to list ")
myList =  list(mytuple)

print(type(myList))

name , age , city =  mytuple

print(name)
print(age)
print(city)