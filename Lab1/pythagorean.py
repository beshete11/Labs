import math

def main():

    input_1 = input("Add a number for one side of a triangle:")
    input_2 = input("Add a number for the second side of a triangle:")

    side_a = int(input_1)
    side_b = int(input_2)

    side_c = float("{:.2f}".format(math.sqrt(side_a**2 + side_b**2)))
    print("The hypotenuse is", side_c)

main()

