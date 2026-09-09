import math
import matplotlib.pyplot as plt
#imports

def plot_function(fun_str, domain, ns):
    xmin = domain[0]
    xmax = domain[1]

    # x list
    xs = []

    step = (xmax - xmin) / (ns - 1)

    for i in range(ns):
        x = xmin + i * step
        xs.append(x)

    # y list
    ys = []

    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    # table
    print()
    print("{:<15} {:<15}".format("x", "y"))
    print("-" * 30)

    for i in range(ns):
        print("{:<15.4f} {:<15.4f}".format(xs[i], ys[i]))

    # graph
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.grid()
    plt.show()
    #can i use pandas in the future? i took a bunch of ai classes before but idk if you want me using that... ¯\_(ツ)_/¯
    #got very used to jupyter notebooks because of it, so its refreshing to be back in vscode

# user input
fun_str = input("Enter function with variable x: ")

xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

ns = int(input("Enter number of samples: "))

domain = (xmin, xmax)

# function
plot_function(fun_str, domain, ns)