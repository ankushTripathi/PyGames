__author__ = 'ankush'
import numpy as np
import pygame


x = np.array(
    [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ],
    dtype= int
)
y = np.array(
    [
        [0],
        [1],
        [1],
        [1]
    ],
    dtype= int
)

class Neural_Nets():

    weights = []
    X = []
    y = []
    estY  = []
    cost = []
    a = []
    z = []
    d = []
    def __init__(self,(ins,hls,ops),x,y):
        self.weights.append(np.random.normal(scale=1,size=[ins,hls]))
        self.weights.append(np.random.normal(scale=1,size=[hls,ops]))
        self.X = x
        self.y = y

    def forward(self):

        z1 = self.X.dot(self.weights[0])
        a1 = 1/(1+np.exp(-1*z1))

        z2 = a1.dot(self.weights[1])
        a2 = 1/(1+np.exp(-1*z2))

        self.z = z1,z2
        self.a = a1
        self.estY = a2>0.5

    def sigmprime(self,z):
        return np.exp(-1*z)/((1+np.exp(-1*z))**2)

    def costFunction(self):
        a1 = self.a
        z1,z2 = self.z
        self.cost = sum(0.5*(self.y-self.estY)**2)
        del3 = np.multiply(-(self.y-self.estY),self.sigmprime(z2))
        d2 = np.dot(a1.T,del3)
        del2 = np.dot(del3,self.weights[1].T)*self.sigmprime(z1)
        d1 = np.dot(self.X.T,del2)
        self.d = d1,d2

NN = Neural_Nets((2,3,1),x,y)
NN.forward()
NN.costFunction()
print(NN.estY)
alpha = 5
d1,d2 = NN.d

for i in range(0,1000):
    if np.abs(np.floor(np.log10(np.mean(NN.cost)))) > 5:
        break
    NN.weights[0] = NN.weights[0] - alpha*d1
    NN.weights[1] = NN.weights[1] - alpha*d2
    NN.forward()
    NN.costFunction()
    print("cost at %d is %s"%(i,NN.cost))

NN.forward()
print(NN.estY)

pygame.init()
dispSurface = pygame.display.set_mode((1080,720))
dispSurface.fill((200,200,200))
pygame.display.set_caption("neural network")
pygame.display.flip()
end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                end = True
    pygame.display.flip()

pygame.quit()

