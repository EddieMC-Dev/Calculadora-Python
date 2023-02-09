from tkinter import Tk, Frame, Label, Button, RAISED, RIDGE, StringVar


def execute_functions(event):
    if event == "=":
        calculate()
    elif event == "C":
        clear_display()
    else:
        input_values(event)

def calculate():
    global contents
    resultado = eval(contents)
    clear_display()
    text_display.set(str(resultado))

def clear_display():
    global contents
    contents = ' '
    text_display.set(contents)

def input_values(event):
    global contents
    if contents[-1] in "-+." and event in "-+.":
        pass
    else:
        contents = contents + str(event)
    text_display.set(contents)


# Cores
black = "#3b3b3b"
white = "#feffff"
blue = "#38576b"
gray = "#c7c6c5"
orange = "#d18513"

# Janela e suas configurações
window = Tk()
window.title("Calculadora")
window.geometry("320x425")
window.maxsize(320, 425)
window.minsize(320, 425)
window.config(bg=black)

# Configurando dados do visor
text_display = StringVar()
contents = ' '
text_display.set(contents)

# Construção da tela de exibição dos cálculos e resultados
frame_display = Frame(window, width=320, height=70, bg=blue)
frame_display.grid(row=0, column=0)
label_display = Label(frame_display, textvariable=text_display, width=15,
                      bg=blue, fg=white, height=2, anchor="e",font=('Ivy 28'))
label_display.place(x=-14, y=-3)

# Construção da zona de botões da calculadora
frame_buttons = Frame(window, width=320, height=355, bg=white)
frame_buttons.grid(row=1, column=0)
buttons_text = [char for char in "C%/789*456-123+0.="]
buttons_width = [15] + [7] * 14 + [15, 7, 7]
buttons_bg = ([gray, gray, orange] + [gray, gray, gray, orange] 
             * 3 + [gray, gray, orange])
buttons_fg = ([black, black, white] + [black, black, black, white] 
             * 3 + [black, black, white])
buttons_x = [0, 160, 240] + [0, 80, 160, 240] * 3 + [0, 160, 240]
buttons_y = [0] * 3 + [71] * 4 + [142] * 4 + [213] * 4 + [284] * 3

for idx, text in enumerate(buttons_text):
    button = Button(frame_buttons, text=text, width=buttons_width[idx],
                    height=3, bg=buttons_bg[idx], fg=buttons_fg[idx],
                    font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE,
                    activebackground=buttons_bg[idx],
                    activeforeground=buttons_fg[idx],
                    command=lambda event=text: execute_functions(event))
    button.place(x=buttons_x[idx], y=buttons_y[idx])


window.mainloop()
