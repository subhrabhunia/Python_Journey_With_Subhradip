# In Bitwise operator all values first convert to binary
# | Operator | Name        | Example  | Description                              |
# | -------- | ----------- | -------- | ---------------------------------------- |
# | `&`      | Bitwise AND | `5 & 3`  | Sets bit to 1 if both bits are 1         |
# | `\|`     | Bitwise OR  | `5 \| 3` | Sets bit to 1 if at least one bit is 1   |
# | `^`      | Bitwise XOR | `5 ^ 3`  | Sets bit to 1 if bits are different      |
# | `~`      | Bitwise NOT | `~5`     | Inverts all bits                         |
# | `<<`     | Left Shift  | `5 << 1` | Shifts bits left by specified positions  |
# | `>>`     | Right Shift | `5 >> 1` | Shifts bits right by specified positions |

# | Expression | Binary Operation | Result |
# | ---------- | ---------------- | ------ |
# | `5 & 3`    | `0101 & 0011`    | `1`    |
# | `5 \| 3`   | `0101 \| 0011`   | `7`    |
# | `5 ^ 3`    | `0101 ^ 0011`    | `6`    |
# | `~5`       | Bitwise NOT      | `-6`   |
# | `5 << 1`   | `0101 → 1010`    | `10`   |
# | `5 >> 1`   | `0101 → 0010`    | `2`    |


a=10   #1010
b=6    #0110
print(bin(a))  #bin use to create binary number.
print(bin(b))

print(bin(a&b))  
print(a&b)

print(bin(a|b))  
print(a|b)

print(bin(a^b))  
print(a^b)

print(bin(~a))  #~x=-(x+1).In Bitwise Not operator we compare any one key.
print(~a)