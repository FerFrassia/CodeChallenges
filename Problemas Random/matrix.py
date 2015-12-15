def matrix(columnas, filas):
	i = 0
	vFilas = []
	while (i < filas):
		j = 0
		vColumnas = []
		while (j < columnas):
			vColumnas.append(j)
			j += 1
		vFilas.append(vColumnas)
		i += 1
	return vFilas

def show(m):
	i = 0
	while (i < len(m)):
		print m[i]
		i += 1

show(matrix(5, 6))

