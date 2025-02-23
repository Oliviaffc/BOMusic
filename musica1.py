'''BOMusic'''

from tkinter import *
import pygame

#from musicas import Musicas

class App(Toplevel):

    cor1 = '#171717'
    cor2 = '#58009D'
    cor3 = '#efefef'

    def __init__(self, original):

        self.frame_original = original
        Toplevel.__init__(self)      
        
        self.config()
        self.frames()
        self.widgetsButton1()
        self.widgetsButton2()
        self.widgetsButton3()
        self.widgetsimg()
        self.widgetstitulo()

    def config(self):
        self.title('BoMusic')
        self.geometry('380x380+700+350')
        self.resizable(False, False)
        self.configure(bg = self.cor1)
        pygame.mixer.init()
        self.iconbitmap('provaDevSistemas\icone.ico')

    def som(self):
        pygame.mixer.music.load('provaDevSistemas\musica1.mp3')
        pygame.mixer.music.play()
        StopIteration

        print('tocando')
        print('')

    def stop(self):
        pygame.mixer.music.pause()
        print('parando')
        print('')
        StopIteration

    def onClose(self):
        self.stop()
        self.destroy()
        self.frame_original.show()

    def frames(self):
        self.titulo = Frame(
            self,
            bg = self.cor1,
        )

        self.titulo.place(
            x = 0,
            y = 20,
            width = 380,
            height = 100
        )

        self.logo = Frame(
            self,
            bg = self.cor1,
        )

        self.logo.place(
            x = 0,
            y = 140,
            width = 380,
            height = 100
        )

        self.voltar = Frame(
            self,
            bg = self.cor3,
        )

        self.voltar.place(
            x = 12.5,
            y = 280,
            width = 110,
            height = 50
        )

        self.play = Frame(
            self,
            bg = self.cor1,
        )

        self.play.place(
            x = 135,
            y = 280,
            width = 110,
            height = 50
        )

        self.parar = Frame(
            self,
            bg = self.cor3,
        )

        self.parar.place(
            x = 257.5,
            y = 280,
            width = 110,
            height = 50
        )

    def widgetstitulo(self):
        title = Label(self.titulo,
            text='Olivia Rodrigo\ngood 4 u',
            font=('Poppins', 20, 'bold'),
            bg = self.cor1,
            fg = self.cor2,
        )
        title.pack()

    def widgetsimg(self):
        self.album = PhotoImage(file = r'provaDevSistemas\album1.png')
        self.img2 = Label(
            self.logo,
            image = self.album,
            bd = 0
        )
        self.img2.pack()

    def widgetsButton1(self):
        self.botao3 = Button(
            self.voltar,
            text = 'Voltar',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.onClose
        )

        self.botao3.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        ) 

    def widgetsButton2(self):
        self.botao = Button(
            self.play,
            text = 'Play',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.som
        )

        self.botao.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )     
        
    def widgetsButton3(self):
        self.botao2 = Button(
            self.parar,
            text = 'Stop',
            font = ('Poppins', 25),
            fg = self.cor3,
            activeforeground = self.cor3,
            bg = self.cor2,
            activebackground = self.cor2,
            command=self.stop
        )

        self.botao2.place(
            relx = 0,
            rely = 0,
            relwidth = 1,
            relheight = 1
        )