# Dictionary :  Key-value pairs , unorderd, Mutable

mydic =   {
    "name":"Om Prakash",
    "age":20,
    "College": "KIIT",
    "City":"Patna" 
}

print("Printing Dictionary")
print(mydic)
print(mydic['name'])


print("Adding email in dict ")
mydic["email"] =  "ompra.rox@gmail.com"

print(mydic)


try:
    print(mydic['subname'])
except :
    print("Error while getting subname")
    
    
print("** Traversing in Dictionary **")

for key in mydic.keys():
    print(key)
    