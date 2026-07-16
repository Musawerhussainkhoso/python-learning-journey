import matplotlib.pyplot as plt 
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y) #plot() function graph mein x aur y points ko draw karti hai.
plt.show()

#markers Marker graph ke har individual point ka symbol hota hai.
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y , marker = 'o') #plot() function graph mein x aur y points ko draw karti hai.
plt.show()

#only show point not line 
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y , 'o') #plot() function graph mein x aur y points ko draw karti hai.
plt.show()

#with labeled example 
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x,y,marker = 'o')
plt.title("My First Graph")
plt.xlabel("X values")
plt.ylabel("Y Values")
plt.show()
