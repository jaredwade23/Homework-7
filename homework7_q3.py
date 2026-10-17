def main():
    height = float(input("Enter the initial height in meters: "))

    if height <= 0:
        print("Height must be greater than zero.")
        return

    bounces = 0

    while height >= 0.001:
        height = height * 0.60
        bounces = bounces + 1

    print("The ball bounced", bounces, "times.")  


main()