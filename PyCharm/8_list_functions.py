hs_friends = ["Red", "Lip", "Kat", "Dave", "Micah"]
college_friends = ["Hanz", "Paula", "Yuri", "Bianca", "Francis"]
print(hs_friends)
print(college_friends)

hs_friends.extend(college_friends)
print(hs_friends)

college_friends.append("James")
print(college_friends)

college_friends.insert(4, "Matthew")
print(college_friends)

hs_friends.remove("Dave")
print(hs_friends)

hs_friends.clear()
print(hs_friends)

college_friends.append("Hanz")
print(college_friends)

print(college_friends.count("Hanz"))

college_friends.sort()
print(college_friends)

college_friends.remove("Hanz")
print(college_friends)

college_friends.reverse()
print(college_friends)

college_friends2 = college_friends.copy()
print(college_friends2)