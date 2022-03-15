import os
from tkinter import *
from tkinter import messagebox

from utils.lang import Language
from utils.redis_cli import Redis


class Configuration:
    def __init__(self, parent) -> None:
        '''Main Window Configuration'''
        self.root = Toplevel(parent.root)
        self.root.geometry('420x250')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='./assets/favicon.png'))

        '''Setting Control Variables'''
        self.var_host = StringVar()
        self.var_port = StringVar()
        self.var_user = StringVar()
        self.var_password = StringVar()

        '''Widget Initialization'''
        self.lbl_header = Label(self.root, text=parent.lang._("Configuracion Global"))
        self.lbl_host = Label(self.root, text=parent.lang._("Nombre de Host"))
        self.lbl_port = Label(self.root, text=parent.lang._("Numero de Puerto"))
        self.lbl_user = Label(self.root, text=parent.lang._("Nombre de Usuario"))
        self.lbl_password = Label(self.root, text=parent.lang._("Contraseña"))

        self.txt_host = Entry(self.root, width=23, textvariable=self.var_host)
        self.spin_port = Spinbox(self.root, from_=1, to=100000, width=20, textvariable=self.var_port)
        self.txt_user = Entry(self.root, width=23, textvariable=self.var_user)
        self.txt_password = Entry(self.root, width=23, textvariable=self.var_password)
        self.btn_update = Button(self.root, text=parent.lang._('Actualizar'), width=30, cursor='hand2')


        '''Widget Configuration'''
        self.var_host.set(parent.redisdb.host)
        self.var_port.set(parent.redisdb.port)
        self.var_user.set(parent.redisdb.user)
        self.var_password.set(parent.redisdb.password)
        self.btn_update.bind('<Button-1>', lambda *args: self.update(parent.redisdb, parent.lang))


        '''Widget Packing'''
        self.lbl_header.grid(row=0, column=0, columnspan=3, padx=140, pady=20)
        self.lbl_host.grid(row=1,column=0, padx=20)
        self.lbl_port.grid(row=2,column=0, padx=20)
        self.lbl_user.grid(row=3,column=0, padx=20)
        self.lbl_password.grid(row=4, column=0, padx=20)

        self.txt_host.grid(row=1, column=1, columnspan=2, padx=20)
        self.spin_port.grid(row=2, column=1, columnspan=2, padx=20)
        self.txt_user.grid(row=3, column=1, columnspan=2, padx=20)
        self.txt_password.grid(row=4, column=1, columnspan=2, padx=20)

        self.btn_update.grid(row=5, column=0, columnspan=3, padx=20, pady=30)

        self.root.mainloop()
    
    def update(self, redis: Redis, lang: Language):
        host = self.var_host.get()
        port = int(self.var_port.get())
        user = self.var_user.get()
        password = self.var_password.get()

        try:
            temp_client = Redis(host, port, user, password)
            temp_client.client.ping()
            del temp_client
            redis.host = host
            redis.port = port
            redis.user = user
            redis.password = password

            language = os.getenv('LANG')

            with open('.env', 'w') as f:
                f.write(f'LANG="{language}"\n')
                f.write(f'HOST="{host}"\n')
                f.write(f'PORT="{port}"\n')
                f.write(f'USER="{user}"\n')
                f.write(f'PASSWORD="{password}"\n')
        
        except Exception as e:
            messagebox.showerror(lang._('Error de conexion'),lang._('No se pudo conectar al servidor, verifique sus datos.'))
            return

        messagebox.showinfo(lang._('Operacion exitosa'), lang._('Informacion Actualizada Correctamente'))
