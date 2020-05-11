import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

sg.theme('DarkAmber')  


def guardarInformacion(juego):
	
	nombre = str(sg.popup_get_text('Ingrese el nombre del jugador:', ''))
	
	respuesta = sg.popup_yes_no('¿Desea guardar su informacion en un archivo preexistente?')
		
	if(respuesta == 'Yes'):
			
		nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extención del archivo que desea abrir:', ''))
		
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
			
			nombreArchivo = str(sg.popup_get_text('Ingrese el nombre y la extención del archivo que desea crear:', ''))
			
			jugadores = {}
			
			if(juego != ""):
					
				jugadores[nombre] = [juego]
						
			else:
						
				jugadores[nombre] = []	
		
			with open(nombreArchivo, 'w') as file:
			
				json.dump(jugadores, file, indent=4)				
		
		else:
				
			sg.popup("La informacion ingresada no sera guardada.")
				


def main():
		
		juego = ""
				
		respuestaJuego = sg.popup_yes_no('¿Desea jugar al Ahorcado?')
				
		if respuestaJuego == 'Yes':
			hangman.main()
			
			juego = str("Hangman")
			
			guardarInformacion(juego)
			
		else:	
				
			respuestaJuego = sg.popup_yes_no('¿Desea jugar al Ta-Te-Ti?')
				
			if respuestaJuego == 'Yes':
				tictactoeModificado.main()
			
				juego = str("Tic-tac-toe")
				
				guardarInformacion(juego)
						
			else:	
			
				respuestaJuego = sg.popup_yes_no('¿Desea jugar al Otello?')

				if respuestaJuego == 'Yes':
					reversegam.main()

					juego = str("Reverse")
					
					guardarInformacion(juego)
						
					
					
main()
