import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

sg.theme('DarkAmber')  


def guardarInformacion(nombre,juego):
	
	respuesta = sg.popup_yes_no('¿Desea guardar su informacion en un archivo preexistente?')
		
	if(respuesta == 'Yes'):
			
		nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extensión del archivo que desea abrir:', ''))
		
		with open(nombreArchivo, 'r') as archivo:
				
			jugadores = {}
				
			jugadores = json.load(archivo)
				
		if(nombre not in jugadores):
				
			if(juego != ""):
							
				jugadores[nombre] = [juego]
							
			else:
							
				jugadores[nombre] = []
							
		else:
						
			if(juego != ""):
			
				jugadores[nombre].append(juego)
			
		with open(nombreArchivo, 'w') as file:
	
			json.dump(jugadores, file, indent=4)	
			
	else:

		respuesta = sg.popup_yes_no('¿Desea guardar su informacion en un archivo nuevo?')

		if(respuesta == 'Yes'):
			
			nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extensión del archivo que desea crear:', ''))
			
			jugadores = {}
			
			if(juego != ""):
					
				jugadores[nombre] = [juego]
						
			else:
						
				jugadores[nombre] = []	
		
			with open(nombreArchivo, 'w') as file:
			
				json.dump(jugadores, file, indent=4)				
		
		else:
				
			sg.popup("La informacion ingresada no sera guardada.")
				


def main(args):

	sigo_jugando = True
	
	while sigo_jugando:

		layout = [
			[sg.Text('Ingrese nombre del jugador:'), sg.InputText()],
			[sg.Text('Elegí a qué juego querés jugar:'),sg.Button('Ahorcado'), sg.Button('Ta-Te-Ti'),sg.Button('Otello')],
			[sg.Button('Salir')]]

		window = sg.Window("Trabajo Prectico - Python Plus").Layout(layout)

		event, values = window.Read()
		window.Close()

		if event == 'Ahorcado':
			hangman.main()
			guardarInformacion(values[0],event)	
		elif event == 'Ta-Te-Ti':
			tictactoeModificado.main()
			guardarInformacion(values[0],event)	
		elif event == 'Otello':
			reversegam.main()
			guardarInformacion(values[0],event)		
		elif event == 'Salir':
			sigo_jugando = False
			
		
						
					
					
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
