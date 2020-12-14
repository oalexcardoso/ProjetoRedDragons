import robotClass
import ballClass
import action

import sim
import simConst

import numpy as n

class strategy:
    def __init__(self, clientIDAtr):

        print("Estrategia criada")    

        #robot1 = red
        #robot2 = pink
        #robot3 = green

        self.robot1 = robotClass.robot(0, 0, 0, 0, 0, "motorDireitaRed", "motorEsquerdaRed", clientIDAtr)
        self.robot2 = robotClass.robot(0, 0, 0, 0, 0, "motorDireitaPink", "motorEsquerdaPink", clientIDAtr)
        self.robot3 = robotClass.robot(0, 0, 0, 0, 0, "motorDireitaGreen", "motorEsquerdaGreen", clientIDAtr)
        self.ball = ballClass.ball(0, 0, clientIDAtr)

    #Atualizar  as posicoes e orientacao dos robos
    #Atualizar a posicao da bola
    def play(self, x1, y1, theta1, x2, y2, theta2, x3, y3, theta3, xBall, yBall, vLAtr1, vRAtr1, vLAtr2, vRAtr2, vLAtr3, vRAtr3):

        #Printar valores para ver se bate com o da vision
        self.robot1.setPos(y1, x1, theta1)
        self.robot2.setPos(x2, y2, theta2)
        self.robot3.setPos(x3, y3, theta3)
        self.ball.setPos(yBall, xBall)

        #action.stop(self.robot1, self.robot2, self.robot3)
        vRAtr1, vLAtr1 = action.follow(self.robot1.theta,self.robot1.xPos,self.robot1.yPos,self.ball.XPos,self.ball.YPos,0.3,2)
     
        print("dif ", n.sqrt(((self.robot1.xPos-self.ball.XPos)**2)+((self.robot1.yPos-self.ball.YPos)**2)))

        if(n.sqrt(((self.robot1.xPos-self.ball.XPos)**2)+((self.robot1.yPos-self.ball.YPos)**2))<=10):
            print("Entrou")
            vRAtr1 = 0
            vLAtr1 = 0

        #print("XPos ", self.ball.XPos)
        #print("YPos ", self.ball.YPos)

        #print("AngRobo ", (self.robot1.theta*180)/n.pi)

        #Decidir se robo vai andar ou parar
        #Andar = action.follow() 
        #Parar = action.stop()

        #Com base nas açoes, colocar as velocidades com base se robo ta andando ou parado
        self.robot1.setVel(vLAtr1, vRAtr1)
        self.robot2.setVel(vLAtr2, vRAtr2)
        self.robot3.setVel(vLAtr3, vRAtr3)