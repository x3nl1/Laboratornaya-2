import matplotlib.pyplot as plt
import numpy as np

def generate_plot_data(start, end):
    x = np.linspace(start, end, 100)
    y = x ** 2
    return x, y

def create_plot(x, y):
    plt.plot(x, y)
    plt.title("График y = x²")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
    
x, y = generate_plot_data(start, end)
create_plot(x, y)
