name = "Duygu"    #str
age = 21          #int
gpa = 3.2         #float  
is_student = True #bool

print(type(name))
print(type(age))

gpa = int(gpa)
print(gpa)

#age = float(age)
#print(age)

age = str(age)
#print(type(age))

#age += 1 #Exception has occurred: TypeError
         #can only concatenate str (not "int") to str

age += "1"   
print(age)  #211    

name = bool(name)
print(name)

