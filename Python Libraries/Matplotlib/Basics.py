import matplotlib.pyplot as plt
#pyplot Matplotlib ka ek submodule hai jo graphs aur charts banane ke liye functions provide karta hai.
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.title("My First Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()