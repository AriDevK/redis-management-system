import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, Menu
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

from utils.redis_cli import Redis
from utils.lang import Language, LangCode
from views.about_view import About
from views.configuration_view import Configuration


class App:
    def __init__(self) -> None:
        env = os.getenv
        host = env('HOST')
        port = int(env('PORT'))
        user = env('USER')
        password = env('PASSWORD')
        self.lang = Language(env('LANG'))
        print(self.lang)
        print(env('LANG'))
        self.redisdb = Redis(host, port, user, password)

        '''Main Window Configuration'''
        self.root = Tk()
        self.root.title(self.lang._('Manejador Redis'))
        self.root.geometry('450x550')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='./assets/favicon.png'))

        '''Setting Control Variables'''
        self.var_page = IntVar(value=1)
        self.var_name = StringVar()
        self.var_type = StringVar()
        self.var_data = StringVar()
        self.var_lang = StringVar(value=self.lang.lang)

        self.var_name.trace('w', lambda *args: self.check_name(args))
        self.var_type.trace('w', lambda *args: self.check_type(args))
        self.var_data.trace('w', lambda *args: self.check_data(args))

        '''Widget Initialization'''
        self.menu = Menu(self.root)
        self.menu_conf = Menu(self.menu, tearoff='off')
        self.menu_lang = Menu(self.menu_conf, tearoff='off')

        img = ImageTk.PhotoImage(Image.open('./assets/necoarc.jpg'))
        self.lbl_img = Label(image=img)
        self.txt_keys = ScrolledText(self.root, width=20, height=12, state='normal', cursor='arrow')

        self.lbl_message = Label(self.root, text=self.lang._('Seleccione una opcion'), font=("Arial Bold", 15))
        self.btn_read = Button(self.root, text=self.lang._("Leer Registro"), width=45, cursor='hand2')
        self.btn_create = Button(self.root, text=self.lang._("Crear/Actualizar Registro"), width=45, cursor='hand2')
        self.btn_delete = Button(self.root, text=self.lang._("Eliminar Registro"), width=45, cursor='hand2')

        self.lbl_name = Label(self.root, text=self.lang._('Nombre de clave'))
        self.txt_name = Entry(self.root, width=32, textvariable=self.var_name)

        self.lbl_type = Label(self.root, text=self.lang._('Tipo de dato'))
        self.combo_type = Combobox(self.root, width=30, textvariable=self.var_type, state='readonly')

        self.lbl_data = Label(self.root, text=self.lang._('Valor de clave'))
        self.txt_svalue = Entry(self.root, width=32, textvariable=self.var_data)
        self.txt_mvalue = ScrolledText(self.root, width=20, height=3)

        self.btn_cread = Button(self.root, text=self.lang._('Leer'), width=20, cursor='hand2')
        self.btn_ccreate = Button(self.root, text=self.lang._('Crear'), width=20, cursor='hand2')
        self.btn_cdelete = Button(self.root, text=self.lang._('Eliminar'), width=20, cursor='hand2')

        '''Widget Configuration'''
        self.menu_conf.add_command(label=self.lang._('Configuracion'), command=lambda: Configuration(self))
        self.menu_conf.add_cascade(label=self.lang._('Idioma'), menu=self.menu_lang)
        self.menu_conf.add_command(label=self.lang._('Salir'), command=self.root.quit)

        self.menu_lang.add_command(label=self.lang._('Español'), command=lambda: self.change_language(LangCode.ES.value))
        self.menu_lang.add_command(label=self.lang._('Ingles'), command=lambda: self.change_language(LangCode.EN.value))
        self.menu_lang.add_command(label=self.lang._('Noruego'), command=lambda: self.change_language(LangCode.NO.value))

        self.menu.add_cascade(label=self.lang._('Opciones'), menu=self.menu_conf)
        self.menu.add_command(label=self.lang._('Acerca de'), command=lambda: About(self))

        keys = '\n'.join(self.redisdb.get_keys())
        self.txt_keys.insert(INSERT, self.lang._('Claves Existentes\n'))
        self.txt_keys.insert(INSERT, '------------------\n')
        self.txt_keys.insert(INSERT, keys)

        self.combo_type['values'] = ('Variable', 'Lista')
        self.txt_keys.bind("<Key>", lambda e: "break")
        self.txt_mvalue.bind('<Key>', lambda *args: self.check_data())

        self.btn_read.bind('<Button-1>', lambda *args: self.show_read_page())
        self.btn_create.bind('<Button-1>', lambda *args: self.show_create_page())
        self.btn_delete.bind('<Button-1>', lambda *args: self.show_delete_page())

        self.btn_ccreate.bind('<Button-1>', lambda *args: self.create())
        self.btn_cdelete.bind('<Button-1>', lambda *args: self.delete())
        self.btn_cread.bind('<Button-1>', lambda *args: self.read())

        '''Packing Widgets'''
        self.lbl_img.grid(column=0, row=0, padx=10, pady=20, columnspan=2)
        self.txt_keys.grid(column=2, row=0, padx=10, pady=20)

        self.lbl_message.grid(column=0, row=1, padx=10, pady=7, columnspan=3)
        self.btn_read.grid(column=0, row=2, padx=10, columnspan=3)
        self.btn_create.grid(column=0, row=3, padx=10, columnspan=3)
        self.btn_delete.grid(column=0, row=4, padx=10, columnspan=3)

        self.root.config(menu=self.menu)
        self.root.mainloop()

    '''Decorators'''
    def use_name(function):
        def wrapper(*args):
            app: App = args[0]
            function(app)
            app.hide_control_widgets()
            app.lbl_name.grid(column=0, row=5, padx=10, pady=5)
            app.txt_name.grid(column=1, row=5, padx=10, pady=5, columnspan=2)
            app.check_name()

        return wrapper

    def reload_keys(function):
        def wrapper(*args):
            app: App = args[0]
            function(app)
            keys = '\n'.join(app.redisdb.get_keys())
            app.txt_keys.delete(1.0, END)
            app.txt_keys.insert(INSERT, app.lang._('Claves Existentes\n'))
            app.txt_keys.insert(INSERT, '------------------\n')
            app.txt_keys.insert(INSERT, keys)

        return wrapper

    '''Function Widget Show/Hide'''

    def hide_control_widgets(self):
        self.lbl_name.grid_forget()
        self.txt_name.grid_forget()
        self.lbl_type.grid_forget()
        self.combo_type.grid_forget()
        self.lbl_data.grid_forget()
        self.txt_svalue.grid_forget()
        self.txt_mvalue.grid_forget()
        self.btn_cread.grid_forget()
        self.btn_ccreate.grid_forget()
        self.btn_cdelete.grid_forget()

    @use_name
    def show_read_page(self):
        self.var_page.set(1)

    @use_name
    def show_create_page(self):
        self.var_page.set(2)

    @use_name
    def show_delete_page(self):
        self.var_page.set(3)

    def change_language(self, language):
        data: list[str] = None

        with open('.env', 'r') as f:
            data = f.readlines()

        with open('.env', 'w') as f:
            for i in data:
                if not i.startswith('LANG'):
                    f.write(f'{i}')
                else:
                    f.write(f'LANG="{language}"\n')

        messagebox.showwarning(self.lang._('Aviso'),
                               self.lang._('Reinicie la aplicacion para aplicar los cambios.'))

    '''Function Checkers'''

    def check_name(self, *args):
        if self.var_name.get():
            if self.var_page.get() == 1:
                self.btn_cread.grid(
                    column=2, row=6, padx=10, pady=5, columnspan=1)

            elif self.var_page.get() == 2:
                self.lbl_type.grid(column=0, row=6, padx=10, pady=5)
                self.combo_type.grid(
                    column=1, row=6, padx=10, pady=5, columnspan=2)

            elif self.var_page.get() == 3:
                self.btn_cdelete.grid(
                    column=2, row=6, padx=10, pady=5, columnspan=1)

        else:
            self.btn_cread.grid_forget()
            self.lbl_type.grid_forget()
            self.combo_type.grid_forget()
            self.btn_cdelete.grid_forget()

    def check_type(self, *args):
        self.hide_control_widgets()
        self.show_create_page()
        self.lbl_data.grid(column=0, row=8, padx=10, pady=5)

        if self.var_type.get() == 'Variable':
            self.txt_svalue.grid(column=1, row=8, padx=10,
                                 pady=5, columnspan=2)

        else:
            self.txt_mvalue.grid(column=1, row=8, padx=10,
                                 pady=5, columnspan=2)

        self.check_data()

    def check_data(self, *args):
        single_value = self.var_data.get()
        multiple_value = self.txt_mvalue.get("1.0", END)

        if single_value or multiple_value:
            self.btn_ccreate.grid(
                column=2, row=9, padx=10, pady=5, columnspan=1)

        else:
            self.btn_ccreate.grid_forget()

    '''CRUD Functions'''

    def read(self):
        name = self.var_name.get()
        print(self.redisdb.port)
        try:
            data = self.redisdb.get_var(name)
            messagebox.showinfo(self.lang._('Ejecucion Correcta'), data)
        except:
            messagebox.showerror(self.lang._('Ejecucion Incorrecta'),
                                 self.lang._('El elemento no existe'))

    @reload_keys
    def create(self):
        key = self.var_name.get()

        if self.var_type.get() == 'Variable':
            value = self.var_data.get()
            self.redisdb.create_var(key, value)

        elif self.var_type.get() == 'Lista':
            value = self.txt_mvalue.get('1.0', END)
            self.redisdb.create_var(key, value, 'list')

        messagebox.showinfo(self.lang._('Ejecucion Correcta'),
                            self.lang._('El elemento ha sido agregado correctamente'))

    @reload_keys
    def delete(self):
        name = self.var_name.get()
        try:
            self.redisdb.delete_var(name)
            messagebox.showinfo(self.lang._('Ejecucion Correcta'),
                                self.lang._('El elemento ha sido agregado correctamente'))

        except:
            messagebox.showerror(self.lang._(
                'Ejecucion Incorrecta'), self.lang._('El elemento no existe'))
