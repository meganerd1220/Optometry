import OP_class as OP
import tkinter
window = tkinter.Tk()
window.resizable(False, False)
myCanvas = tkinter.Canvas(window, bg="white", height=300, width=500)
total = "Total: $" + str(OP.self.__cost)
myCanvas.create_text(100, 100, text=total)
myCanvas.pack()
window.mainloop()

