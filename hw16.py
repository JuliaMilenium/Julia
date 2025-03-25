def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# Тестуємо функцію
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'

print('ОК')






def say_hi2(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"
print(say_hi2("Alex", 32))  # Виведе: Hi. My name is Alex and I'm 32 years old
print(say_hi2("Frank", 68))  # Виведе: Hi. My name is Frank and I'm 68 years old
