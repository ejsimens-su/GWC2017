from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("cat.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata()
image_list = list(image_list) #THis will hold a list of 

recolored = [] #list holding the pixel data for the new image.

#check for intensity and color the pixel in recolored based on intensity. 

for i in image_list:
    i = list(i)
    total = i[0] + i[1] + i[2]
    if total < 182:
    	i = darkBlue
    elif total >= 182 and total <= 364:
    	i = red
    elif total >= 364 and total <= 546:
    	i = lightBlue
    else:
    	i = yellow
    recolored.append(i)


#A pixel's "intensity" will be higher if the value of Red Green and Blue added together is higher.
#Good numbers to start with for intensity - 182, 364, 546 - but your numbers may vary
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.



# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
