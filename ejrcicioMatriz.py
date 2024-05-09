matriz = [['❣','❣','❣','❣','❣',], ['❣','❣','❣','❣','❣'], ['❣','❣','❣','❣','❣'], ['❣','❣','❣','❣','❣'], ['❣','❣','❣','❣','❣']]

correcto = '✔'
incorrecto = '✘'
ls_preguntas = ['¿QUÉ ES PYTHON?\n\n1. JUEGO\n2. LENGUAJE DE PROGRAMACION\n3. MARCA DE AUTOS\n4. NINGUNA DE LAS ANTERIORES',
                '¿QUÉ ES HTML?\n\n1. LENGUAJE DE MAQUETACIÓN\n2. MARCA DE GASEOSA\n3. NAVEGADOR\n4. PERRO CALIENTE']
Ls_respuestas = ['2','1']



def fnt_pinta_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='    ')
        print('\n\n')
        
contador = 0  
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        import os
        os.system('cls')
        fnt_pinta_matriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input('->')
        if r == ls_preguntas[contador]:
            matriz[i][j] = correcto
        else:
            matriz[i][j] = incorrecto
        contador += 1
            