from tkinter import *
from PIL import Image, ImageTk

class About:
    def __init__(self, parent):
        '''Main Window Configuration'''
        self.root = Toplevel(parent.root)
        self.root.title = parent.lang._('Acerca de')
        self.root.geometry('400x200')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='./assets/favicon.png'))

        '''Widget Initialization'''
        img = ImageTk.PhotoImage(Image.open('./assets/banner.png'))
        self.lbl_img = Label(self.root, image=img)

        self.lbl_header = Label(self.root, text=parent.lang._('Manejador BDD Redis\nCreado el 14/03/2022'))
        self.lbl_author = Label(self.root, text=parent.lang._('Autor Jorge Luis Rangel Benitez\nNo. de Control #19260943'))
        self.lbl_course = Label(self.root, text=parent.lang._('Materia Taller de Base de Datos\nProfesora Maria Yolanda Rodriguez Loya'))

        '''Widget Packing'''
        self.lbl_img.grid(row=0, column=0, rowspan=4)
        self.lbl_header.grid(row=0, column=1, padx=10)
        self.lbl_author.grid(row=1, column=1, padx=10)
        self.lbl_course.grid(row=2, column=1, padx=10)

        self.root.mainloop()