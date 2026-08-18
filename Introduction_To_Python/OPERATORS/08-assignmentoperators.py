# | Operator | Example   | Equivalent   |
# | -------- | --------- | ------------ |
# | `=`      | `x = 5`   | Assign value |              
# | `+=`     | `x += 3`  | `x = x + 3`  |              
# | `-=`     | `x -= 3`  | `x = x - 3`  |              
# | `*=`     | `x *= 3`  | `x = x * 3`  |              
# | `/=`     | `x /= 3`  | `x = x / 3`  |              
# | `%=`     | `x %= 3`  | `x = x % 3`  |              
# | `//=`    | `x //= 3` | `x = x // 3` |              
# | `**=`    | `x **= 3` | `x = x ** 3` |              
# | `&=`     | `x &= 3`  | `x = x & 3`  |              
# | `|=`     | `x|=3`    | `x \|= 3`    |  
# | `^=`     | `x ^= 3`  | `x = x ^ 3`  |              
# | `>>=`    | `x >>= 3` | `x = x >> 3` |              
# | `<<=`    | `x <<= 3` | `x = x << 3` |        
 
      
x = 10

x = x + 5
print("x = x + 5  :", x)

x += 5
print("x += 5     :", x)

x -= 5
print("x -= 5     :", x)

x *= 5
print("x *= 5     :", x)

x /= 5
print("x /= 5     :", x)

x %= 5
print("x %= 5     :", x)

x //= 5
print("x //= 5    :", x)

x **= 5
print("x **= 5    :", x)

# Convert float to int before bitwise operations
x = int(x)

x &= 5
print("x &= 5     :", x)

x |= 5
print("x |= 5     :", x)

x ^= 5
print("x ^= 5     :", x)

x >>= 5
print("x >>= 5    :", x)

x <<= 5
print("x <<= 5    :", x)

print("\nFinal Value of x =", x)