def cube_number(num):
    return num*num*num

def add_surname(first, last):
    fullname = (first + " " + last)
    return fullname

result = cube_number(4)
print(result)

name = add_surname("Laurence", "Barin")
print(name)