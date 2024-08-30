import flet as ft
#import os para aumentar a quantidade de argumentos

def main(page: ft.Page):
    page.window.center()
    page.title = 'Calculadora'
    page.window_width = 270
    page.window_height = 450
    page.window_resizable = True
    page.window_always_on_top = True
    page.update()

    #Funções:
    def entradas(e: ft.KeyboardEvent):
        print(e.key)
        if e.shift:
            match e.key:
                case '5':
                    return '%'
                case '8':
                    return '*'
                case '=':
                    return '+'
                case '-':
                    return '-'
                case 'Enter':
                    return '='
                case ',':
                    return '.'
        else:
            if e.key.isnumeric():
                return e.key
            match e.key:
                case ',':
                    return '.'
                case 'Numpad Multiply':
                    return '*'
                case 'Numpad Add':
                    return '+'
                case 'Numpad Subtract':
                    return '-'
                case 'Numpad Divide':
                    return '/'
                case 'Numpad Decimal':
                    return '.'
                case 'Numpad 1':
                    return '1'
                case 'Numpad 2':
                    return '2'
                case 'Numpad 3':
                    return '3'
                case 'Numpad 4':
                    return '4'
                case 'Numpad 5':
                    return '5'
                case 'Numpad 6':
                    return '6'
                case 'Numpad 7':
                    return '7'
                case 'Numpad 8':
                    return '8'
                case 'Numpad 9':
                    return '9'
                case 'Numpad 0':
                    return '0'
                case 'Enter':
                    return '='
                case '-':
                    return '-'
                case '=':
                    return '='
                case 'Backspace':
                    return '<'

    def tcinput(e):
        nonlocal novo, operador,val1
        data = entradas(e)
        if data == 'AC':
            resultado.value = '0'
            operador = ''
            novo = True
            val1 = -1
        elif data == '.':
            if resultado.value == '0' or novo == False:
                resultado.value += data
            elif val1 != 1:
                resultado.value += data
                novo = False
        elif data == '<':
            if len(resultado.value) != 1:
                    resultado.value = resultado.value[0:len(resultado.value) - 1]
            elif len(resultado.value) != 1 and val1 != -1:
                    resultado.value = resultado.value[0:len(resultado.value) - 1]
                    val1 = resultado.value
            elif len(resultado.value) == 1:
                resultado.value = '0'
                val1 = -1
                novo = True
        elif data == '+/-':
            if not '-' in resultado.value and resultado.value != '0':
                resultado.value = '-' + resultado.value
            else:
                resultado.value = resultado.value.replace('-','')
        elif valor(data):
            if resultado.value == '0' or novo == True:
                resultado.value = data
                novo = False
            elif operador == '=':
                val1 = formato(resultado.value)
                operador = ''
                resultado.value += data
            else:
                resultado.value += data
        elif valor(data,i=True):
            if data != '=':
                val1 = formato(resultado.value)
                operador = data
                novo = True
            else:
                if val1 == -1:
                    resultado.value = resultado.value
                else:
                    resultado.value = str(calculo(val1=val1,val2=resultado.value,operador=operador))
                    novo = True
        resultado.update()
    
    def calculo(val1, val2, operador):
        val1 = formato(val1)
        val2 = formato(val2)
        if operador == '+':
            result = val1 + val2
            return formato(result)
        elif operador == '*':
            result = val1 * val2
            return formato(result)
        elif operador == '-':
            result = val1 - val2
            return formato(result)
        elif operador == '/':
            if val2 != 0:
                result = val1 / val2
                return formato(result)
            else:
                return 0
        elif operador == '%':
            result = (val1 / 100) * val2
            return formato(result)
        
    def click(c):
        nonlocal novo, operador,val1
        data = c.control.text
        if data == 'AC':
            resultado.value = '0'
            operador = ''
            novo = True
            val1 = -1
        elif data == '.':
            if resultado.value == '0' or novo == False:
                resultado.value += data
            elif val1 != 1:
                resultado.value += data
                novo = False
        elif data == '<':
            if len(resultado.value) != 1:
                    resultado.value = resultado.value[0:len(resultado.value) - 1]
            elif len(resultado.value) != 1 and val1 != -1:
                    resultado.value = resultado.value[0:len(resultado.value) - 1]
                    val1 = resultado.value
            elif len(resultado.value) == 1:
                resultado.value = '0'
                val1 = -1
                novo = True
        elif data == '+/-':
            if not '-' in resultado.value and resultado.value != '0':
                resultado.value = '-' + resultado.value
            else:
                resultado.value = resultado.value.replace('-','')
        elif valor(data):
            if resultado.value == '0' or novo == True:
                resultado.value = data
                novo = False
            elif operador == '=':
                val1 = formato(resultado.value)
                operador = ''
                resultado.value += data
            else:
                resultado.value += data
        elif valor(data,i=True):
            if data != '=':
                val1 = formato(resultado.value)
                operador = data
                novo = True
            else:
                if val1 == -1:
                    resultado.value = resultado.value
                else:
                    resultado.value = str(calculo(val1=val1,val2=resultado.value,operador=operador))
                    novo = True
        resultado.update()

    def valor(dt,i=False):
        if i:
            if dt in ('+','-','*','/','%','='):
                return True
        else:
            if dt in ('1','2','3','4','5','6','7','8','9','0'):
                return True
        return False
        
    def formato(data):
        data = float(data)
        if data % 1 == 0:
            return int(data)
        else:
            return float(data)
        
    #Variaveis
    novo = True
    operador = ''
    val1 = -1

    #Captura das teclas    
    page.on_keyboard_event = tcinput

    #Layout dos Botões
    botoes_ac = [

        {"Valor": 'AC', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '%', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '<', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click},
        {"Valor": '+/-', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Forma": 2, "Comando": click}

    ]

    botoes_79 = [

        {"Valor": '7', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '8', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '9', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '/', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]
    
    botoes_46 = [

        {"Valor": '4', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '5', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '6', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '*', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

    botoes_13 = [

        {"Valor": '1', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '2', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '3', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '-', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

    botoes_0 = [

        {"Valor": '.', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '0', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.WHITE70, "Comando": click},
        {"Valor": '=', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_500, "Comando": click},
        {"Valor": '+', "Cor": ft.colors.BLACK, "Cor_de_fundo": ft.colors.BLUE_ACCENT_400, "Comando": click},
    ]

        #Botões
    bts_ac = [ft.Container(
        content = ft.FloatingActionButton(text=bts_ac['Valor'], foreground_color=bts_ac['Cor'],
                                           bgcolor=bts_ac['Cor_de_fundo'], aspect_ratio=bts_ac['Forma'], on_click=bts_ac['Comando']),
        width=55,
        height=55,
        alignment=ft.alignment.center,
    )   for bts_ac in botoes_ac]

    bts_79 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_79['Valor'], foreground_color=bts_79['Cor'],
                                         bgcolor=bts_79['Cor_de_fundo'], on_click=bts_79['Comando']),
        width=55,
        height=55,
    )   for bts_79 in botoes_79]

    bts_46 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_46['Valor'], foreground_color=bts_46['Cor'],
                                         bgcolor=bts_46['Cor_de_fundo'], on_click=bts_46['Comando']),
        width=55,
        height=55,
    )   for bts_46 in botoes_46]

    bts_13 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_13['Valor'], foreground_color=bts_13['Cor'],
                                         bgcolor=bts_13['Cor_de_fundo'], on_click=bts_13['Comando']),
        width=55,
        height=55,
    )   for bts_13 in botoes_13]

    bts_0 = [ft.Container(
        content=ft.FloatingActionButton(text=bts_0['Valor'], foreground_color=bts_0['Cor'],
                                         bgcolor=bts_0['Cor_de_fundo'], on_click=bts_0['Comando']),
        width=55,
        height=55,
    )   for bts_0 in botoes_0]

    #Textos
    resultado = ft.Text(
        value='0',
        size=40
    )
    
    #Linhas
    display = ft.Row(
        width=270,
        height=80,
        controls=[resultado],
        alignment='end',
    )

    l_ac = ft.Row(
        controls=bts_ac,
        alignment=ft.alignment.center,
        spacing=5,
        height=30
    )
    
    l_79 = ft.Row(
        controls=bts_79,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_46 = ft.Row(
        controls=bts_46,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_13 = ft.Row(
        controls=bts_13,
        alignment=ft.alignment.center,
        spacing=5
    )
    
    l_0 = ft.Row(
        controls=bts_0,
        alignment=ft.alignment.center,
        spacing=5
    )


    page.add(display,l_ac,l_79,l_46,l_13, l_0)


ft.app(target=main)
