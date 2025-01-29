prompt = input("Enter a distance or weight amount followed by a unit of measurent:")
felicia = prompt.split()

if felicia[1] == "lbs" or felicia[1] == "lb":
    conversion = float(felicia[0])* 0.45359237
    print(prompt, "=", float("{:.3}".format(conversion)),"kg")

if felicia[1] == "kg":
    conversion = float(felicia[0]) / 0.45359237
    print(prompt, "=", float("{:.2}".format(conversion)), "lbs")

if felicia[1] == "in":
    conversion = float(felicia[0]) * 2.54
    print(prompt, "=", float("{:.3}".format(conversion)), "cm")

if felicia[1] == "cm":
    conversion = float(felicia[0]) / 2.54
    print(prompt, "=", float("{:.2}".format(conversion)), "in")

if felicia[1] == "yd" or felicia[1] == "yds":
    conversion = float(felicia[0]) * 0.9144
    print(prompt, "=", float("{:.2}".format(conversion)), "m")

if felicia[1] == "m":
    conversion = float(felicia[0]) / 0.9144
    print(prompt, "=", float("{:.2}".format(conversion)), "yd")

if felicia[1] == "oz":
    conversion = float(felicia[0]) * 28.349523125
    print(prompt, "=", float("{:.2}".format(conversion)), "g")

if felicia[1] == "g":
    conversion = float(felicia[0]) / 28.349523125
    print(prompt, "=", float("{:.2}".format(conversion)), "oz")
