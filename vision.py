import numpy as num
import sim
import simConst

#Funcao para rotacionar o robo
def rotacionarVetores(ang, x, y):
    ang = num.radians(ang)
    cosseno = num.cos(ang)
    seno = num.sin(ang)

    R = num.array([[cosseno, -seno], [seno, cosseno]])

    V = num.array([x, y])

    vetorRotacionado = num.matmul(R,V)

    angRotacionado = num.arctan2(vetorRotacionado[1], vetorRotacionado[0])

    return angRotacionado

#Definir orientação do codigo, ou seja, orientado pelo "Dummy"
def refPos(clientID):
    res,refPoint = sim.simxGetObjectHandle(clientID,'Dummy',sim.simx_opmode_blocking)

    if res!=0:
        print('Erro refPos()')

    return refPoint

#Pegar as posicoes da bola
def getPosBall(clientID, ref):
    res,client_jointHandle = sim.simxGetObjectHandle(clientID,'ball',sim.simx_opmode_blocking)
    res,alvoPos = sim.simxGetObjectPosition(clientID,client_jointHandle,ref,sim.simx_opmode_streaming)

    return 100*alvoPos[0],100*alvoPos[1]

#Pegar as posicoes e orientacao do robo com os parametros definidos
def getPosRobot(clientID, ref, nomeRobo, marcadorJogador, marcadorTime):
    res,client_jointHandle = sim.simxGetObjectHandle(clientID,nomeRobo,sim.simx_opmode_blocking)
    res,roboPos = sim.simxGetObjectPosition(clientID,client_jointHandle,ref,sim.simx_opmode_streaming)

    res,client_jointHandle = sim.simxGetObjectHandle(clientID,marcadorJogador,sim.simx_opmode_blocking)
    res,marcaJogador = sim.simxGetObjectPosition(clientID,client_jointHandle,ref,sim.simx_opmode_streaming)

    res,client_jointHandle = sim.simxGetObjectHandle(clientID,marcadorTime,sim.simx_opmode_blocking)
    res,marcaTime = sim.simxGetObjectPosition(clientID,client_jointHandle,ref,sim.simx_opmode_streaming)

    angRobo = rotacionarVetores(45,marcaJogador[0]-marcaTime[0],marcaJogador[1]-marcaTime[1])  

    return 100*roboPos[0],100*roboPos[1],((angRobo*180)/num.pi)