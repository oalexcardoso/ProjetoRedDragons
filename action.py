import strategy
import robotClass
import ballClass

import numpy as n

#Como parametro do follow eu preciso do setPos() do robotClass e do setPos() da ballClass
def follow(angRobo, roboX, roboY, alvoX, alvoY, Kp, velocidade):
	#Comandos para os robos seguirem a bola
	#controlador proporcioanal
	angAlvo = n.arctan2(alvoY-roboY,alvoX-roboX)

	angE = angAlvo - angRobo

	varControle = Kp * angE

	velRodaL = velocidade - varControle
	velRodaR = velocidade + varControle

	print("AngErro ", angE)

	return velRodaL, velRodaR

	#return as velocidades de cada roda

#Como parametro do follow eu preciso do setPos() do robotClass e do setPos() da ballClass
def stop(robot1, robot2, robot3):
	#Comando para o robo ficar parado
	robot1.setVel(0,0)
	robot2.setVel(0,0)
	robot3.setVel(0,0)

	#return as velocidades de cada roda