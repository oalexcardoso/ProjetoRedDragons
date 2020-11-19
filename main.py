try:
    # Importar o arquivo sim.py
    import sim
    import simConst
except:
    # Caso não conseguir importar o arquivo
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

# Importando bibliotecas
import time
import numpy as num

# Importando arquivos .py
import vision
import strategy

#Y, X, orientacao
posRoboRed = [0,0,0]
posRoboPink = [0,0,0]
posRoboGreen = [0,0,0]

posBola = [0,0]

print ('Program started')
# Parametro -1 cancela todas as comunicações
sim.simxFinish(-1)
# Criando comunicação
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID!=-1:
    print('Connected to remote API server')

# Código para printar teste

sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot)

#Dicas

    #robo parado
    #chamar visao e ver se ta certo em todos robo
    #chamar strategy e ver se ta tudo ok
    #print todos valores

#Também deve ser criado o objeto da classe estratégia(Strategy). (??????)
#instanciar o strategy aqui

strategy = strategy.strategy(clientID)

#chamar o play do strategy para atualizar tudo e jogar
#Chamar o vision e obter o setPose() do ballClass e setPose do robotClass()
#Chamar o play() do strategy para excutar os comandos dos robos

while(True):

    #Pegar posicao da bola
    posBola = vision.getPosBall(clientID, vision.refPos(clientID))
    #Pegar posicao do robo "Red"
    posRoboRed = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynRed','marcadorPosicaoRed','marcadorEquipeRed')
    #Pegar posicao do robo "Pink"
    posRoboPink = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynPink','marcadorPosicaoPink','marcadorEquipePink')
    #Pegar posicao do robo "Green"
    posRoboGreen = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynGreen','marcadorPosicaoGreen','marcadorEquipeGreen')

    strategy.play(posRoboRed[1], posRoboRed[0], posRoboRed[2], posRoboPink[1], posRoboPink[0], posRoboPink[2], posRoboGreen[1], posRoboGreen[0], posRoboGreen[2], posBola[1], posBola[0], 0, 0, 0, 0, 0, 0)
    
    print("Red:   ", posRoboRed)
    print("Pink:  ", posRoboPink)
    print("Green: ", posRoboGreen)
    print("Bola:  ", posBola)
    print("")

    #Parar
    #sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)

try:
    # Importar o arquivo sim.py
    import sim
    import simConst
except:
    # Caso não conseguir importar o arquivo
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

# Importando bibliotecas
import time
import numpy as num

# Importando arquivos .py
import vision
import strategy

#Y, X, orientacao
posRoboRed = [0,0,0]
posRoboPink = [0,0,0]
posRoboGreen = [0,0,0]

posBola = [0,0]

print ('Program started')
# Parametro -1 cancela todas as comunicações
sim.simxFinish(-1)
# Criando comunicação
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if clientID!=-1:
    print('Connected to remote API server')

# Código para printar teste

sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot)

#Dicas

    #robo parado
    #chamar visao e ver se ta certo em todos robo
    #chamar strategy e ver se ta tudo ok
    #print todos valores

#Também deve ser criado o objeto da classe estratégia(Strategy). (??????)
#instanciar o strategy aqui

strategy = strategy.strategy(clientID)

#chamar o play do strategy para atualizar tudo e jogar
#Chamar o vision e obter o setPose() do ballClass e setPose do robotClass()
#Chamar o play() do strategy para excutar os comandos dos robos

while(True):

    #Pegar posicao da bola
    posBola = vision.getPosBall(clientID, vision.refPos(clientID))
    #Pegar posicao do robo "Red"
    posRoboRed = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynRed','marcadorPosicaoRed','marcadorEquipeRed')
    #Pegar posicao do robo "Pink"
    posRoboPink = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynPink','marcadorPosicaoPink','marcadorEquipePink')
    #Pegar posicao do robo "Green"
    posRoboGreen = vision.getPosRobot(clientID, vision.refPos(clientID),'soccerRob_dynGreen','marcadorPosicaoGreen','marcadorEquipeGreen')

    strategy.play(posRoboRed[1], posRoboRed[0], posRoboRed[2], posRoboPink[1], posRoboPink[0], posRoboPink[2], posRoboGreen[1], posRoboGreen[0], posRoboGreen[2], posBola[1], posBola[0], 0, 0, 0, 0, 0, 0)

    print("Red:   ", posRoboRed)
    print("Pink:  ", posRoboPink)
    print("Green: ", posRoboGreen)
    print("Bola:  ", posBola)
    print("")

    #Parar
    #sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)

    '''
    Tarefas:
        action.py:
            Fazer funcao stop()

        strategy.py:
            Usar função follow() dentro do play()
            Usar função stop() dentro do play()

        main.py:
            Startar com robo parado
            Chamar o play() para fazer o robo jogar(seguir ou parar)
            Decidir movimentos de cada robo com base na bola
    '''