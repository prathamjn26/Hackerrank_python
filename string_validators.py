str = input()
print (any(i.isalnum()  for i in str))
print (any(i.isalpha() for i in str))
print (any(i.isdigit() for i in str))
print (any(i.islower() for i in str))
print (any(i.isupper() for i in str))