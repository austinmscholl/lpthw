i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)



def ex33(n, p):
    i2 = 0
    numbers2 = []

    while i2 < n:
        print(f"At the top i2 is {i2}")
        numbers2.append(i2)

        i2 = i2 + p
        print("Numbers2 now: ", numbers2)
        print(f"At the bottom i2 is {i2}")

    print("The numbers: ")

    for num in numbers2:
        print(num)

ex33(50, 5)

def ex33_2(m, q):
    x = m
    y = q
    i3 = 0
    numbers3 = []

    for i3 in range(m, q):
        print(f"Adding {i3} to numbers3")
        numbers3.append(i3)

    for num in numbers3:
        print(num)

ex33_2(5, 10)
