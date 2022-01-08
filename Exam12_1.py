print(" *** Wind classification ***")
n = float(input("Enter wind speed (km/h) : "))
if n < 0:
    print("!!!Wrong value can't classify.")
    quit()
print("Wind classification is ", end="")
if n <= 51.99:
    print("Breeze.")
elif n <= 55.99:
    print("Depression.")
elif n <= 101.99:
    print("Tropical Storm.")
elif n <= 208.99:
    print("Typhoon.")
else:
    print("Super Typhoon.")
