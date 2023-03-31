import tkinter
import OP_class as OP

root = tkinter.Tk()
root.resizable(False, False)

myDisplay = tkinter.Canvas(root, bg="white", height=500, width=1200)

# first row
fr1 = tkinter.PhotoImage(file="images/blue_oval.png")
fr1 = fr1.subsample(1, 1)
fr2 = tkinter.PhotoImage(file="images/pink_circle.png")
fr2 = fr2.subsample(1, 1)
fr3 = tkinter.PhotoImage(file="images/cat_eye.png")
fr3 = fr3.subsample(1, 1)

# second row
fr4 = tkinter.PhotoImage(file="images/clear_oval.png")
fr4 = fr4.subsample(1, 1)
fr5 = tkinter.PhotoImage(file="images/rectangle_frame.png")
fr5 = fr5.subsample(1, 1)
fr6 = tkinter.PhotoImage(file="images/square_frame.png")
fr6 = fr6.subsample(1, 1)

# images
blue_oval = myDisplay.create_image(200, 125, image=fr1)
pink_circle = myDisplay.create_image(600, 125, image=fr2)
cat_eye = myDisplay.create_image(1000, 125, image=fr3)
clear_oval = myDisplay.create_image(200, 350, image=fr4)
rectangle_frame = myDisplay.create_image(600, 350, image=fr5)
square_frame = myDisplay.create_image(1000, 350, image=fr6)


# Text boxes
f1_text = "1) Blue Oval Frame\n      Price: $" + str(OP.f1.get_price())
f2_text = "2) Pink Circle Frame\n       Price: $" + str(OP.f2.get_price())
f3_text = "3) Multi-Color Cat Eye Frame\n            Price: $" + str(OP.f3.get_price())
f4_text = "4) Transparent Oval Frame\n           Price: $" + str(OP.f4.get_price())
f5_text = "5) Black Rectangle Frame\n          Price: $" + str(OP.f5.get_price())
f6_text = "6) Brown Square Frame\n         Price: $" + str(OP.f6.get_price())

# first row
blue_oval_text = myDisplay.create_text(200, 215, text=f1_text, fill="black", font=('Helvetica 15'))
pink_circle_text = myDisplay.create_text(600, 215, text=f2_text, fill="black", font=('Helvetica 15'))
cat_eye_text = myDisplay.create_text(1000, 215, text=f3_text, fill="black", font=('Helvetica 15'))
# second row
clear_oval_text = myDisplay.create_text(200, 440, text=f4_text, fill="black", font=('Helvetica 15'))
rectangle_frame_text = myDisplay.create_text(600, 440, text=f5_text, fill="black", font=('Helvetica 15'))
square_text = myDisplay.create_text(1000, 440, text=f6_text, fill="black", font=('Helvetica 15'))

myDisplay.pack()
root.mainloop()

