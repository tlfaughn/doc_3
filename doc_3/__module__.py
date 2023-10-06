def circ_area():

    print("-_-_-_-_-_-_OPTIONS_-_-_-_-_-_- \n \n 1. Calculate square footage \n 2. Calculate circumference \n 3. Quit")

    option = int(input("Enter an option: "))

    while option != 3:
        if option == 1:
            side1 = int(input("Enter a length in feet: "))
            side2 = int(input("Enterh a width in feet: "))
            area = side1*side2
            print(f"The square footage is {area}")
            break
            
        elif option == 2:
            result = float(input("Enter the diameter: "))
            Circum = result * 3.14
            print(f' The circumference is {Circum}.')  
            break

        elif option != 3:
            print("Please enter a valid option.")

        
        option = int(input("Enter an options number: "))
        
    else: 
        print("Thank you. ")

circ_area()