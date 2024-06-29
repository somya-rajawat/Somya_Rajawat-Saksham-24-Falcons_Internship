print (-(2))

a='A'
print(a)
print(type(a))
# ascii value
print(ord(a))
print(chr(97))


# string
str = "My name is Somya"
print(str) #print string
print(type(str)) #tell about the datatype
print(id(str)) #tells id
print(len(str)) #tells length of string it also counts space



# methods of the string
#capitilaize = POORNIMA UNIVERSITY
s='poornima university'
print(s.capitalize()) #Only capitalize first letter of first word 

# title
print(s.title())#capitalize both first letters

print(s.upper()) # this function do capital string 
print(s.lower())   # this function do lower string 
print(s.isupper())    #it's Output is boolean 
print(s.islower())   # it also have boolean output 
print(s.isalpha()) # it also have boolean out but value only have alphabets 

k='name'
print(k.isalpha())


var='1520063008'
print(var.isdigit())  # it only contains numbers
print(var.isdigit())




abc='vaid2006'
print(abc.isspace)
x='mahavir'
print(x.count('r'))


print(x)

print(s.find('ni'))

print(s.find("ni",8,len(s)))



# strip

a=" good person "
print(a.lstrip)

print(a.rstrip)

print(a.rstrip('son'))


print(a)

# replace
aa="__python_pro__"

ans=a.replace('__','nnn')

print(ans)
print(aa)
val=a.replace('__',"//")
print(val)



a='jaipur'
b='city'

ab=a.join(b)

print(ab)

print(a)
print(b)