def hammingWeight(self, n: int) -> int:
    res = 0
    while n:
        res += 1 if n & 1 else 0
        n >>= 1
    return res

#count the number of 1 bit in 1000110001
#logic
#we started doding and operation so it will then shift right all the bit