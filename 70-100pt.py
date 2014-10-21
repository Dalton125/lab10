##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# 70 point lab
#house outline 
rectangle1 = drawpad.create_rectangle(170,300,500,600,fill = 'red')
line1 = drawpad.create_line(170,300,350,150)
line2 = drawpad.create_line(500,300,350,150)

#80 point lab
#windows 
window1 = drawpad.create_rectangle(200,350,300,450,fill = 'blue')
window2 = drawpad.create_rectangle(400,350,450,450,fill = 'blue')
window3 = drawpad.create_rectangle(300,250,350,200,fill = 'blue')
window4 = drawpad.create_rectangle(497,500,450,550,fill = 'blue')
#door
door = drawpad.create_rectangle(300,500,350,600,fill = 'brown')

#90 point version
#door handle
oval = drawpad.create_oval(335,565,340,570)
#chimney
chimney1 = drawpad.create_line(390,190,390,150)
chimney2 = drawpad.create_line(390,150,415,150)
chimney3 = drawpad.create_line(415,150,415,215)

#100 point lab
#green grass
grass1 = drawpad.create_rectangle(0,550,170,600,fill = 'green')
grass2 = drawpad.create_rectangle(500,550,800,600,fill = 'green')
root.mainloop()
