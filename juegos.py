import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

sg.theme('DarkAmber')      

layout = [
    [sg.Text('Trabajo practico - Python Plus')],
    [sg.Button('Comenzar'),sg.Button('Salir')]]

window = sg.Window('', layout)
    
    
while True:
	
	event, values = window.Read()

	if event is 'Comenzar':
		
				
				nombre = str(sg.popup_get_text('Ingrese el nombre del jugador:', ''))
		
				preexistente = False
		
				nuevo = False
	
				respuesta = sg.popup_yes_no('¿Desea guardar su informacion en un archivo preexistente?')
		
				if(respuesta == 'Yes'):
			
					nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extención del archivo que desea abrir:', ''))
			
					with open(nombreArchivo, 'r') as archivo:
				
						jugadores = {}
				
						jugadores = json.load(archivo)
				
						preexistente = True
			
				else:

					respuesta = sg.popup_yes_no('¿Desea guardar su informacion en un archivo nuevo?')

					if(respuesta == 'Yes'):
			
						nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extención del archivo que desea crear:', ''))
						
						nuevo = True
		
					else:
				
						sg.popup("La informacion ingresada no sera guardada.")
						

				juego = ""
				
				respuestaJuego = sg.popup_yes_no('¿Desea jugar al Ahorcado?')
				
				if respuestaJuego == 'Yes':
					hangman.main()
			
					juego = str("Hangman")
			
				else:	
				
					respuestaJuego = sg.popup_yes_no('¿Desea jugar al Ta-Te-Ti?')
				
					if respuestaJuego == 'Yes':
						tictactoeModificado.main()
			
						juego = str("Tic-tac-toe")
						
					else:	
			
						respuestaJuego = sg.popup_yes_no('¿Desea jugar al Otello?')

						if respuestaJuego == 'Yes':
							reversegam.main()

							juego = str("Reverse")


				if(preexistente == True):

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
		
				if(nuevo == True):
			
					jugadores = {}
			
					if(juego != ""):
					
						jugadores[nombre] = [juego]
						
					else:
						
						jugadores[nombre] = []	
		
					with open(nombreArchivo, 'w') as file:
			
						json.dump(jugadores, file, indent=4)
						
	
				sg.popup("Fin del juego.")
				
				
	if event == ('Salir'):
		
		break
