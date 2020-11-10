import sim
import simConst

class robot:
    #Inicializacao das variaveis
    def __init__(self, xPosAtr, YPosAtr, thetaAtr, vLAtr, vRAtr, handleMotorLAtr, handleMotorRAtr, clientIDAtr):
        print("Robo Criado")

        self.xPos = xPosAtr
        self.yPos = YPosAtr
        self.theta = thetaAtr
        self.vL = vLAtr
        self.vR = vRAtr
        self.handleMotorL = handleMotorLAtr
        self.handleMotorR = handleMotorRAtr
        self.clientID = clientIDAtr

    #Passar as posicoes e orientação do robo para o setPos()
    def setPos(self, xPosAtr, YPosAtr, thetaAtr):
        self.xPos = xPosAtr
        self.yPos = YPosAtr
        self.theta = thetaAtr

    #Colocar as velocidades nos robos
    def sendVel(self, clientID, handleMotorL, handleMotorR):
        sim.simxSetJointTargetVelocity(clientID, handleMotorL, self.vL, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientID, handleMotorR, self.vR, sim.simx_opmode_oneshot)

    #Receber as velocidades e atribuir a sendVel()
    def setVel(self, vLAtr, vRAtr):
        self.vL = vLAtr
        self.vR = vRAtr
        self.sendVel(self.clientID, self.handleMotorL, self.handleMotorR)