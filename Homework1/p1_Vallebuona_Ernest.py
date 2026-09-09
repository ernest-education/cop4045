import matplotlib.pyplot as plt
import math

#your karmic debt grows every time you require a pdf conversion instead of just grading the .py file


while(True):
        print("Enter quadratic components for a, b, and c in order. enter nothing for a to quit.")

        a_in = input("Enter a: ")
        if(a_in == ""):
            print("Quitting")
            break
            #if nothing is entered before ENTER, break out and terminate

        a = float(a_in)
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
            #take the other values now that proceeding is confirmed, no checks as this is assumed valid
    
        D = b**2 - (4*a*c)
        #discriminant 

        if(D < 0):
            print("no real solutions")

            #for graphing
            xopt = -b / (2*a)

            xmin = xopt - 5
            xmax = xopt + 5

        elif(D == 0):
            x_one = -b  / (2*a)

            print(f"One Solution: {x_one:.5f}")

            #for graphing
            xmin = x_one - 5
            xmax = x_one + 5

        else:
            x_one = (-b - math.sqrt(D))/ (2*a)
            x_two = (-b + math.sqrt(D))/ (2*a)

            print(f"Two solutions: {x_one:.5f} and {x_two:.5f}")

            #for graphing
            xmin = min(x_one, x_two) - 2
            xmax = max(x_one, x_two) + 2


        #make 150 values
        x_values = [
            xmin + i * (xmax - xmin) / 149
            for i in range(150)
        ]

        y_values = [
             a * x**2 + b * x + c
             for x in x_values
        ]

        # Plot the quadratic function
        plt.figure()
        plt.plot(x_values, y_values)
        plt.axhline(0)
        plt.axvline(0)

        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"f(x) = {a}x² + {b}x + {c}")
        plt.grid(True)

        plt.show()