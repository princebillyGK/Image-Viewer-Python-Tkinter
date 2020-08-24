from tkinter import Tk, Label, Button, DISABLED, SUNKEN, E, W

from PIL import ImageTk, Image

root = Tk()
root.title("Simple Image Viewer by princebillygk")

images = [
    ImageTk.PhotoImage(Image.open('assets/img/pic_1.webp')),
    ImageTk.PhotoImage(Image.open('assets/img/pic_2.webp')),
    ImageTk.PhotoImage(Image.open('assets/img/pic_3.webp')),
    ImageTk.PhotoImage(Image.open('assets/img/pic_4.webp'))
]


class ImageViewer:
    """Image gallery widget"""

    def __init__(self, rootWidget):
        # init
        self.root = rootWidget
        self.my_label = Label(image=images[0])
        self.button_back = Button(rootWidget, text="<<", state=DISABLED)
        self.button_exit = Button(rootWidget, text="Exit Program", command=root.quit)
        self.button_forward = Button(rootWidget, text=">>", command=lambda: self.forward(1))
        self.status_bar = Label(rootWidget, text="1 of %d" % len(images), bd=1, relief=SUNKEN, anc=E)

        # render
        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_back.grid(row=1, column=0)
        self.button_exit.grid(row=1, column=1, pady=10)
        self.button_forward.grid(row=1, column=2)
        self.status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)

    def forward(self, index):
        """Go to next img"""
        # update
        self.my_label = Label(self.root, image=images[index])
        self.button_back = Button(self.root, text="<<", command=lambda: self.back(index - 1))
        if index >= 3:
            self.button_forward = Button(self.root, text=">>", state=DISABLED)
        else:
            self.button_forward = Button(self.root, text=">>", command=lambda: self.forward(index + 1))
        self.status_bar = Label(self.root, text="%d of %d" % (index + 1, len(images)), bd=1, relief=SUNKEN, anc=E)

        # re-render
        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_back.grid(row=1, column=0)
        self.button_forward.grid(row=1, column=2)
        self.status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)

    def back(self, index):
        """Go to previous img"""
        # update
        self.my_label = Label(self.root, image=images[index])
        if index <= 0:
            self.button_back = Button(self.root, text="<<", state="disabled")
        else:
            self.button_back = Button(self.root, text="<<", command=lambda: self.back(index - 1))
        self.button_forward = Button(self.root, text=">>", command=lambda: self.forward(index + 1))
        self.status_bar = Label(self.root, text="%d of %d" % (index + 1, len(images)), bd=1, relief=SUNKEN, anc=E)

        # re-render
        self.my_label.grid(row=0, column=0, columnspan=3)
        self.button_back.grid(row=1, column=0)
        self.button_forward.grid(row=1, column=2)
        self.status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)


imageViewer = ImageViewer(root)
root.mainloop()
