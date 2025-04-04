def is_even(n):
    return (n & 1) == 0


assert is_even(0) == True
assert is_even(1) == False
assert is_even(2) == True
assert is_even(12345678) == True
assert is_even(12345679) == False
print("OK ✅")
