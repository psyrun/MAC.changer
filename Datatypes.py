# type() to know the  datatype of the object.
a = 13 + 2j  #complex number with "j" representation
print(type(a)) 

# String
a = (str("Hello World !"))
print(a,type(a))


# Numerical 
## input integer
a = (int("100"))
print(a,type(a))

## input float
a = (float("99.9"))
print(a,type(a))

## input Complex
a = 12 + 0j 
print(a,type(a))

# Sequence

## list
a = ["web","rev","Crypto",1,2] #list are mutable
print(a[1],type(a))
print(a,type(a))

## tuple
print(a,type(a))
a = ("web","rev","Crypto",1,2) #list are mutable
print(a[0],type(a))
print(a,type(a))

## range
a = range(6)
print(a,type(a))

# Mapping 

## dict
a = {"name":"Hello","lastname":"World !!!"}
print(a,type(a))

# Boolean

##bool
a = True
print(a,type(a))

# Set

## set
a = {"name" ,"Hello","lastname", "World !!!"}
print(a,type(a))


## frozenset
a = frozenset({"name" ,"Hello","lastname", "World !!!"})
print(a,type(a))

#Binary

## bytes
a=b"Hello"
print(a,type(a))

## bytearray 
a = bytearray(5)
print(a,type(a))

## memoryview
a = memoryview(bytes(16))
print(a,type(a))
b = memoryview(bytes(16))
print(b,type(b))

# output

# <class 'complex'>
# Hello World ! <class 'str'>
# 100 <class 'int'>
# 99.9 <class 'float'>
# (12+0j) <class 'complex'>
# rev <class 'list'>
# ['web', 'rev', 'Crypto', 1, 2] <class 'list'>
# ['web', 'rev', 'Crypto', 1, 2] <class 'list'>
# web <class 'tuple'>
# ('web', 'rev', 'Crypto', 1, 2) <class 'tuple'>
# range(0, 6) <class 'range'>
# {'name': 'Hello', 'lastname': 'World !!!'} <class 'dict'>
# True <class 'bool'>
# {'lastname', 'World !!!', 'name', 'Hello'} <class 'set'>
# frozenset({'lastname', 'World !!!', 'name', 'Hello'}) <class 'frozenset'>
# b'Hello' <class 'bytes'>
# bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>
# <memory at 0x7f17f8aae340> <class 'memoryview'>
# <memory at 0x7f17f8aaea00> <class 'memoryview'>
