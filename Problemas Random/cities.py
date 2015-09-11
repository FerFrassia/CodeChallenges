def cities(cities, meters):
	bestStart = 0
	bestEnd = 0
	start = 0
	actual = 0
	cities = map(int, cities.split())

	while actual < len(cities):
		while cities[actual] - cities[start] > meters:
			start = start + 1

		if actual - start > bestEnd - bestStart:
			bestStart = start
			bestEnd = actual

		actual = actual + 1

	output = 0
	print 'path chosen: ', cities[bestStart:bestEnd + 1]
	if bestStart != bestEnd:
		output = bestEnd - bestStart + 1

	return output

print 'result: ', cities(raw_input('Enter cities: '), int(raw_input('Enter meters: ')))


# La comunicaci ́on es el progreso! decididos a entrar de lleno en la nueva era el pa ́ıs decidi ́o conectar telegr ́aficamente todas las estaciones del moderno sistema f ́erreo que recorre el pa ́ıs en abanico con origen en la capita (el kil ́ometro 0). Por lo escaso del presupuesto, se ha decidido ofrecer cierta cantidad de kilometros de cable a cada ramal. Pero para maximizar el impacto en epocas electorales se busca lograr conectar la mayor cantidad de ciudades con los metros asignados (sin hacer cortes en el cable)
# Resolver cuantas ciudades se pueden conectar para cada ramal en O(n) , con n la cantidad de estaciones en cada ramal, y justificar por qu ́e el procedimiento desarrollado resuelve efectivamente el problema.
# Entrada Tp1Ej1.in
# Cada ramal ocupa dos l ́ıneas, la primera contiene un entero con los kilometros de cable dedicados al ramal y la segunda los kilometrajes de las estaciones en el ramal sin cosiderar el 0.
# Salida Tp1Ej1.out
# Para cada ramal de entrada, se debe indicar una l ́ınea con la cantidad de ciudades conectables encontradas.