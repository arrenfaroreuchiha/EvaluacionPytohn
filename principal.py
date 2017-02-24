# -*- coding: utf-8 -*-


from proyecto import mein

repetir = 1
while repetir != 0:
	mein()
	print "Si en verdad deseas salir marque 0 si deseas volver a las opcciones marque 1:\n"
	repetir = int(raw_input("1 o 0:"))
	print "\n"
	while repetir > 1:
		print "Por favor marque como se le indica arriba gracias.\n"
		repetir = int(raw_input("1 o 0:\n"))
	




