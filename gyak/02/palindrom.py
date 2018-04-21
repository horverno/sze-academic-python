palindrom1 = "Indul a görög aludni"
palindrom2 = "Rád rohan a hordár"
palindrom3 = "Ez nem az is palindrom..."

teszt1 = palindrom2[::-1].lower().replace(" ", "")
teszt2 = palindrom2.lower().replace(" ", "")

print(teszt1)
print(teszt2)

if teszt1 == teszt2:
    print("Ez palindrom :)")
else:
    print("Hát ez nem palindrom :(")