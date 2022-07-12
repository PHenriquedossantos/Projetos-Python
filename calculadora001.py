from tkinter import *
from tkinter import ttk
# cores
cor1 = "#1e1f1e"   # Um pouco preto
cor2 = "#feffff"   # Branco 
cor3 = "#38576b"   # Azul carregado
cor4 = "#ECEFF1"   # Cinzenta
cor5 = "#FFAB40"   # Laranja

principal = Tk()
principal.title('Calculadora')

# primeiro número é horizontal o segundo é vertical

principal.geometry("235x310")
principal.config(bg=cor1)
# Criando frames
frame_tela = Frame(principal, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_botoes = Frame(principal, width=235, height=268)
frame_botoes.grid(row=1, column=0)
# variável todos os
todos_valores = ''
#Criando funcoes
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    

    
    valor_texto.set(todos_valores)
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


valor_texto = StringVar()
display = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor= "e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
display.place(x=0,y=0)

b_1 = Button(frame_botoes, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_botoes, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_botoes, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_botoes, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_botoes, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_botoes, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_botoes, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_botoes, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_botoes, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_botoes, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_botoes, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_botoes, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_botoes, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_botoes, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_botoes, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)


b_1 = Button(frame_botoes, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)
b_2 = Button(frame_botoes, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=208)
b_3 = Button(frame_botoes, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)




principal.mainloop()