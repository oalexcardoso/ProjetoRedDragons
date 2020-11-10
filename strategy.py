import robotClass
import ballClass
import action

class strategy:
    def __init__(self, clientIDAtr):
        print("Estrategia criada")

        self.robot1 = robotClass.robot(0, 0, 0, 0, 0, 0, 0, clientIDAtr)
        self.robot2 = robotClass.robot(0, 0, 0, 0, 0, 0, 0, clientIDAtr)
        self.robot3 = robotClass.robot(0, 0, 0, 0, 0, 0, 0, clientIDAtr)
        self.ball = ballClass.ball(0, 0, 0)

    #Atualizar  as posicoes e orientacao dos robos
    #Atualizar a posicao da bola
    def play(self, x1, y1, theta1, x2, y2, theta2, x3, y3, theta3, xBall, yBall, vLAtr1, vRAtr1, vLAtr2, vRAtr2, vLAtr3, vRAtr3):
        
        print("Aqui Foi");

        #Printar valores para ver se bate com o da vision
        self.robot1.setPos(x1, y1, theta1)
        self.robot2.setPos(x2, y2, theta2)
        self.robot3.setPos(x3, y3, theta3)
        self.ball.setPos(xBall, yBall)

        action.stop();

        #Decidir se robo vai andar ou parar
        #Andar = action.follow()
        #Parar = action.stop()

        #Com base nas açoes, colocar as velocidades com base se robo ta andando ou parado
        self.robot1.setVel(vLAtr1, vRAtr1)
        self.robot2.setVel(vRAtr2, vRAtr2)
        self.robot3.setVel(vRAtr3, vRAtr3)