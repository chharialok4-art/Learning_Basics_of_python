# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]
# w = [21,23,25,27]
# z = [100,0,10,3]

# plt.plot(x, y)
# plt.plot(w,z)
# plt.show()
print("--------------------------------------------------------------------------------")
# import matplotlib.pyplot as plt
# # Data
# x = [22,1,7,2,21,11,14,5]
# y = [24,2,12,5,5,5,9,12]
# plt.scatter(x,y, marker = 'd')

# # Customize the plot (optional)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title(' Scatter Plot with pentagonal marker')

# # Display the plot
# plt.show()
print("--------------------------------------------------------------------------------")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Load the image
img = mpimg.imread('/Users/dev/Downloads/My Image.jpeg')  # Load image file
# Display the image
plt.imshow(img)
plt.axis('on')  # Turn off axis labels and ticks (optional)
plt.show()