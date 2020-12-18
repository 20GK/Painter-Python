from tkinter import *

class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.color = "black"
        self.brush_size = 150
        self.setUI()
        
    def set_color(self, new_color):
        self.color = new_color
    def set_brush_size(self, new_size):
        self.brush_size = new_size
    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
        #print("Painted Circle an: "+  "x:"+str(event.x)  +  "  y:"+str(event.y))
    def setUI(self):
        self.parent.title("Mesmoon Developer Paint")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(12, weight=1)
        self.rowconfigure(3, weight=1)

        self.canv = Canvas(self, bg="#ffffff")
        self.canv.grid(row=3, column=0, columnspan=13,
                        padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind("<B1-Motion>", self.draw)


        def firstRowColor():
            color_lab = Label(self, text="Color: ")
            color_lab.grid(row=0, column=0, padx=7)

            white_btn = Button(self, text="Black", width=10, command=lambda: self.set_color("#000000"))
            white_btn.grid(row=0, column=1)

            white_btn = Button(self, text="Gray", width=10, command=lambda: self.set_color("#808080"))
            white_btn.grid(row=0, column=2)

            white_btn = Button(self, text="Dark Red", width=10, command=lambda: self.set_color("#800000"))
            white_btn.grid(row=0, column=3)

            white_btn = Button(self, text="Red", width=10, command=lambda: self.set_color("#ff0000"))
            white_btn.grid(row=0, column=4)

            white_btn = Button(self, text="Orange", width=10, command=lambda: self.set_color("#ff8000"))
            white_btn.grid(row=0, column=5)

            white_btn = Button(self, text="Yellow", width=10, command=lambda: self.set_color("#ffff00"))
            white_btn.grid(row=0, column=6)

            white_btn = Button(self, text="Green", width=10, command=lambda: self.set_color("#00ff00"))
            white_btn.grid(row=0, column=7)

            white_btn = Button(self, text="Light blue", width=10, command=lambda: self.set_color("#00ffff"))
            white_btn.grid(row=0, column=8)

            white_btn = Button(self, text="Blue", width=10, command=lambda: self.set_color("#0000ff"))
            white_btn.grid(row=0, column=9)

            white_btn = Button(self, text="Purple", width=10, command=lambda: self.set_color("#800080"))
            white_btn.grid(row=0, column=10)
        def secondRowColor():

            white_btn = Button(self, text="White", width=10, command=lambda: self.set_color("#ffffff"))
            white_btn.grid(row=1, column=1)

            white_btn = Button(self, text="Light Gray", width=10, command=lambda: self.set_color("#d4d4d4"))
            white_btn.grid(row=1, column=2)

            white_btn = Button(self, text="Brown", width=10, command=lambda: self.set_color("#ca6932"))
            white_btn.grid(row=1, column=3)

            white_btn = Button(self, text="Pink", width=10, command=lambda: self.set_color("#ffa1f5"))
            white_btn.grid(row=1, column=4)

            white_btn = Button(self, text="Dark Yellow", width=10, command=lambda: self.set_color("#ffcf00"))
            white_btn.grid(row=1, column=5)

            white_btn = Button(self, text="Light Yellow", width=10, command=lambda: self.set_color("#f0eda3"))
            white_btn.grid(row=1, column=6)

            white_btn = Button(self, text="Lime", width=10, command=lambda: self.set_color("#7dff26"))
            white_btn.grid(row=1, column=7)

            white_btn = Button(self, text="Light+ blue", width=10, command=lambda: self.set_color("#8fffe9"))
            white_btn.grid(row=1, column=8)

            white_btn = Button(self, text="Light- blue", width=10, command=lambda: self.set_color("#4dabe0"))
            white_btn.grid(row=1, column=9)

            white_btn = Button(self, text="Light Pink", width=10, command=lambda: self.set_color("#d1b1e0"))
            white_btn.grid(row=1, column=10)
        def BrushRow():
            clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
            clear_btn.grid(row=2, column=10, sticky=W)



            size_lab = Label(self, text="Brush size: ")
            size_lab.grid(row=2, column=0, padx=5)

            one_btn = Button(self, text="Two", width=10, command=lambda: self.set_brush_size(2))
            one_btn.grid(row=2, column=1)

            two_btn = Button(self, text="Five", width=10, command=lambda: self.set_brush_size(5))
            two_btn.grid(row=2, column=2)

            five_btn = Button(self, text="Seven", width=10, command=lambda: self.set_brush_size(7))
            five_btn.grid(row=2, column=3)

            seven_btn = Button(self, text="Ten", width=10, command=lambda: self.set_brush_size(10))
            seven_btn.grid(row=2, column=4)

            ten_btn = Button(self, text="Twenty", width=10, command=lambda: self.set_brush_size(20))
            ten_btn.grid(row=2, column=5)

            twenty_btn = Button(self, text="Fifty", width=10, command=lambda: self.set_brush_size(50))

            twenty_btn.grid(row=2, column=6, sticky=W)

        firstRowColor()
        secondRowColor()
        BrushRow()

def main():
    root = Tk()
    root.geometry("1920x1080" + "+300+300")
    app = Paint(root)
    root.mainloop()
if __name__ == '__main__':
    main()
