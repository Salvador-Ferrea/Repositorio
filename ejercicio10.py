imagenes=['im1','im2','im3']

lista = []

for i in range(3):

	listaImagenes = []
	listaImagenes.append(imagenes[i])
	
	print('   Coordenadas para la imagen', imagenes[i],":")
	print(' ')
	
	for i in range(3):
	
		numeroX = int(input("   Ingrese una coordenada X: "))
		print(' ')
	
		numeroY = int(input("   Ingrese una coordenada Y: "))
		print(' ')
	
		tupla = (numeroX,numeroY)
	
		while (tupla in listaImagenes):
			
			print("   La coordenada ingresada no es valida.")
			print(" ")
			
			numeroX = int(input("   Ingrese una coordenada X: "))
			print(' ')
	
			numeroY = int(input("   Ingrese una coordenada Y: "))
			print(' ')
	
			tupla = (numeroX,numeroY)
			
		listaImagenes.append(tupla)	
	
	lista.append(listaImagenes)	
	
print(lista)	
	
	
