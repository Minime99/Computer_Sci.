# puts numbers from 0 to 5 not 0 to 6
for x in range(6):
    print(x)

total = 0
for x in range(2001):
    total = total+x
print(total)

for x in range(2, 6):
    print(x)

for x in range(1, 11):
    print(x, "ahoy!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)