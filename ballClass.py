class ball:
	#Inicializacao das variaveis
    def __init__(self, XPosAtr, YPosAtr, clientIDAtr):
        self.XPos = XPosAtr
        self.YPos = YPosAtr
        self.clientID = clientIDAtr

    #Passar as posicoes da bola para setPos()
    def setPos(self, XPosAtr, YPosAtr):
        self.XPos = XPosAtr
        self.YPos = YPosAtr
