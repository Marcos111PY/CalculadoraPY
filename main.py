import PySimpleGUI as sg
import re

layout = [
    [sg.Input(size=(27,10), border_width=(2), background_color="beige", text_color="blue", key="-INPUT-")],

    [sg.Button(" + ", button_color="grey", border_width=(2), size=(4), key="+"),
    sg.Button(" - ", button_color="grey", border_width=(2), size=(4), key="-"),
    sg.Button(" / ", button_color="grey", border_width=(2), size=(4), key="/"),
    sg.Button("<==", button_color="grey", border_width=(2), size=(4), key="c")],

    [sg.Button(" 7 ", size=(4), border_width=(2), key="7"), 
    sg.Button(" 8 ", size=(4), border_width=(2), key="8"), 
    sg.Button(" 9 ", size=(4), border_width=(2), key="9"),
    sg.Button(" X ", button_color="grey", border_width=(2), size=(4), key="*")],

    [sg.Button(" 4 ", size=(4), border_width=(2), key="4"), 
    sg.Button(" 5 ", size=(4), border_width=(2), key="5"), 
    sg.Button(" 6 ", size=(4), border_width=(2), key="6"),
    sg.Button(" % ", button_color="grey", border_width=(2), size=(4), key="%")],
    [sg.Button(" 1 ", size=(4), border_width=(2), key="1"), 
    sg.Button(" 2 ", size=(4), border_width=(2), key="2"), 
    sg.Button(" 3 ", size=(4), border_width=(2), key="3"),
    sg.Button("Del", size=(4), button_color="grey", border_width=(2), key="del")
    ],

    [sg.Button(" 0 ", size=(4), border_width=(2), key="0"), 
    sg.Button("", size=(4), border_width=(2), key=",", disabled=True, button_color="purple"), 
    sg.Button("", size=(4), border_width=(2), disabled=True, button_color="purple"), 
    sg.Button(" = ", button_color="grey", border_width=(2), size=(4), key="-RES-")]]
    
def RESULTADO(INPUT):
    try:
        sinal = re.sub("[0-9]", "", INPUT)
        separa = re.findall("[0-9]+", INPUT)

        if sinal == "+":
            resultado = int(separa[0]) + int(separa[1])
            window.Element("-INPUT-").Update(resultado)

        elif sinal == "%":
            NUM1 = int(separa[0]) * int(separa[1])
            PORCENT = NUM1 / 100
            resultado = str(separa[0]) + "% de " + str(separa[1]) + " é: " + str(PORCENT)
            window.Element("-INPUT-").Update(resultado)

        elif sinal == "-":
            resultado = int(separa[0]) - int(separa[1])
            window.Element("-INPUT-").Update(resultado)

        elif sinal == "/":
            resultado = int(separa[0]) / int(separa[1])
            window.Element("-INPUT-").Update(resultado)

        elif sinal == "*":
            resultado = int(separa[0]) * int(separa[1])
            window.Element("-INPUT-").Update(resultado)
            
        else:
            sg.Popup("Erro no calculo", "Utilize os sinais de soma(+), subtração(-), divisão(/), multiplicação(*) e porcentagem(%) entre os números.")

    except Exception as erro:
        sg.Popup(str(erro))

window = sg.Window("Calculadora", layout, icon="calculadora.ico")

while True:
    window.refresh()
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-RES-":
        RESULTADO(values["-INPUT-"])
    if event == "1":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "1")
    if event == "2":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "2")
    if event == "3":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "3")
    if event == "4":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "4")
    if event == "5":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "5")
    if event == "6":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "6")
    if event == "7":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "7")
    if event == "8":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "8")
    if event == "9":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "9")
    if event == "0":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "0")
    if event == "del":
        window.Element("-INPUT-").Update("")
    if event == "c":
        inicial = values["-INPUT-"]
        window.Element("-INPUT-").Update(inicial[0:-1])
    if event == "+":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "+")
    if event == "-":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "-")
    if event == "*":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "*")
    if event == "/":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "/")
    if event == "%":
        input_ = values["-INPUT-"]
        window.Element("-INPUT-").Update(input_ + "%")