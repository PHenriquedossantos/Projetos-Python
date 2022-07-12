from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

janela = Tk()
janela.title('')
janela.geometry("310x400")



cor1= "#333333"
cor2= "#000000"
cor3 = "#FFFFFF"
cor4 = "#fcc058"

frame_tela = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_secundario = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_secundario.grid(row=1, column=0)


def resultado():
    inicial = calendario001.get()
    final = calendario002.get()
    
    mes_inicial, dia_inicial, ano_inicial = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano_inicial, mes_inicial, dia_inicial)

    mes_final, dia_final, ano_final = [int(f) for f in final.split('/')]
    data_final = date(ano_final, mes_final, dia_final)
    
    years = relativedelta(data_inicial, data_final).years
    months = relativedelta(data_inicial, data_final).months
    days = relativedelta(data_inicial, data_final).days
    label_anos['text'] = years
    label_meses['text'] = months
    label_dias['text'] = days


label1 = Label(frame_tela, text="CALCULADORA DE IDADE", width=25, height=1, padx=3, relief="flat", anchor="center", font=('Ivy 15 bold'), bg=cor2, fg=cor3)
label1.place(x=0, y=30)


label_data_nascimento = Label(frame_secundario, text="DATA NASCIMENTO", width=15, height=1, padx=3, relief="flat", anchor=NW, font=('Ivy 8 bold'), bg=cor2, fg=cor3)
label_data_nascimento.place(x=5, y=50)

label_data_atual = Label(frame_secundario, text="DATA ATUAL", width=10, height=1, padx=3, relief="flat", anchor=NW, font=('Ivy 8 bold'), bg=cor2, fg=cor3)
label_data_atual.place(x=5, y=80)



label_anos = Label(frame_secundario, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 11 bold'), bg=cor2, fg=cor3)
label_anos.place(x=5, y=130)

label_dias = Label(frame_secundario, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 11 bold'), bg=cor2, fg=cor3)
label_dias.place(x=200, y=130)

label_meses = Label(frame_secundario, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 11 bold'), bg=cor2, fg=cor3)
label_meses.place(x=100, y=130)

label_anos_text = Label(frame_secundario, text="ANOS", height=1, padx=0, relief="flat", anchor="center", font=('Arial 9 bold'), bg=cor2, fg=cor3)
label_anos_text.place(x=5, y=160)

label_dias_text = Label(frame_secundario, text="DIAS", height=1, padx=0, relief="flat", anchor="center", font=('Arial 9 bold'), bg=cor2, fg=cor3)
label_dias_text.place(x=200, y=160)

label_meses_text = Label(frame_secundario, text="MESES", height=1, padx=0, relief="flat", anchor="center", font=('Arial 9 bold'), bg=cor2, fg=cor3)
label_meses_text.place(x=100, y=160)

calendario001 = DateEntry(frame_secundario, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern = 'dd/mm/y', y=2022)
calendario001.place(x=150, y=50)

calendario002 = DateEntry(frame_secundario, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern = 'dd/mm/y', y=2022)
calendario002.place(x=150, y=80)

button001 = Button(frame_secundario, command = resultado, text="Calcular", height=1, width=10, relief="raised", anchor="center", font=('Arial 15 bold'), bg=cor2, fg=cor3)
button001.place(x=80, y=200)

janela.mainloop()