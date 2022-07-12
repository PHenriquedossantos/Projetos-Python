import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTK

bg_dia = "#ffd359"
bg_noite = "#1c1c1a"
bg_tarde = "#ffd359"
bg = "#ffd359"
black = "#181a1c"
cor_botao = "#dadee3"
letra_botao = "#0f4991"

janela = Tk()
janela.title('')
janela.geometry('400x450')
janela.configure(bg=bg_dia)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)



first_frame = Frame(janela, width = 400, height = 50, bg = black, pady = 0)
first_frame.grid(row=1, column=0)

second_frame = Frame(janela, width = 400, height = 370, bg = bg_tarde, pady = 0)
second_frame.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

campo_pesquisa = Entry(first_frame, width = 20, justify = 'left', font = ("", 14), highlightthickness = 1, relief = 'solid')
campo_pesquisa.place(x = 13, y = 12)

click = Button(first_frame, width = 15, text = 'Pesquisar', bg = cor_botao, fg = letra_botao, font = ("Ivy 9 bold"), relief = 'raised', overrelief = RIDGE)
click.place(x = 260, y = 12)

label_cidade = Label(second_frame, text = 'Rio de Janeiro - Brasil / America do Sul', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 12 bold"), anchor = 'center')
label_cidade.place(x = 13, y = 12)

data = Label(second_frame, text = '12 07 2022, 15:02 PM', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 10 bold"), anchor = 'center')
data.place(x = 13, y = 45)

graus = Label(second_frame, text = '36 graus', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 35 bold"), anchor = 'center')
graus.place(x = 13, y = 100)

humidade = Label(second_frame, text = '57', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 9 bold"), anchor = 'center')
humidade.place(x = 13, y = 199)

humidade_porcento = Label(second_frame, text = '%', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 9 bold"), anchor = 'center')
humidade_porcento.place(x = 28, y = 199)

humidade_text = Label(second_frame, text = 'De humidade', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 9 bold"), anchor = 'center')
humidade_text.place(x = 40, y = 199)

pressao = Label(second_frame, text = 'Pressão : 1000', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 10 bold"), anchor = 'center')
pressao.place(x = 13, y = 225)

velocidade_vento = Label(second_frame, text = 'Velocidade do vento : 1000', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 10 bold"), anchor = 'center')
velocidade_vento.place(x = 13, y = 250)

descricao = Label(second_frame, text = 'Nublado', bg = bg_tarde, fg = "#ffffff",  font = ("Ivy 10 bold"), anchor = 'center')
descricao.place(x = 13, y = 250)

imagem = Image.open('img\Dia.png')
imagem = imagem.resize((130, 130))
imagem = ImageTK.PhotoImage(imagem)

label_icone = Label(second_frame, image = imagem, bg = bg_tarde)
label_icone.place(x = 13, y = 250)

janela.mainloop()