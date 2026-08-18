# In Left shift(<<)                  
# a<<n then 
# a<<n means a x(2**n)

# if a=5 and n=1 then
# 5<<1 means 5 x(2x1)

# if a=5 and n=2 then
# 5<<2 means 5 x(2x2)

# if a=5 and n=3 then
# 5<<3 means 5 x(2x2x2)

# In Right Shift(>>)
# a>>n then
# a>>n means  a/(2**n)

# if a=20 n=1 then
# 20>>1 means 20/(2x1)

# if a=20 n=2 then
# 20>>2 means 20/(2x2)

# if a=20 n=3 then
# 20>>3 means 20/(2x2x2)


a=5     #LEFT SHIFT OPERATOR
print(a<<1)
print(a<<2)
print(a<<3)
print(a<<4)


b=20  #RIGHT SHIFT OPERATOR
print(b>>1)
print(b>>2)
print(b>>3)
print(b>>4)