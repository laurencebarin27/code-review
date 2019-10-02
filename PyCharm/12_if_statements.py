is_male = True
if is_male:
    print("You are male")
else:
    print("You are not male")

is_male = False
if is_male:
    print("You are male")
else:
    print("You are not male")

is_male = True
is_tall = False

if is_male or is_tall:
    print("You are either male or tall or both")
else:
    print("You are neither male nor tall")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are either not male or tall or both")


is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not is_tall:
    print("You are male but not tall")
elif not is_male and is_tall:
    print("You are not male but you are tall")
else:
    print("You are neither")

