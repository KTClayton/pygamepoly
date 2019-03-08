import pygame
import math
pygame.init()

class Polygon:
    x = 0
    y = 0
    Vertices = []
    Rotation = 0
    def __init__(self, x, y, Vertices):
        assert len(Vertices)>2, "Not enough vertices. Mustbe more than 2, "+str(len(Vertices))+" Given"
        self.x = x
        self.y = y
        self.Vertices = Vertices
        self._content = None

    def rotatePoly(self, theta):
        theta *= -1
        for i in range(0, len(self.Vertices)):
            oldx = self.Vertices[i][0]
            oldy = self.Vertices[i][1]
            self.Vertices[i][0] = oldx*math.cos(theta) - oldy*math.sin(theta)
            self.Vertices[i][1] = oldx*math.sin(theta) + oldy*math.cos(theta)
        Rotation += theta


    def scalePoly(self, sx, sy):
        for i in range(0, len(self.Vertices)):
            if abs(self.Vertices[i][0]) >0.1 and abs(self.Vertices[i][1]) >0.1:
                self.Vertices[i][0] *= sx
                self.Vertices[i][1] *= sy


    def setPolyPosition(self, x, y):
        self.x = x
        self.y = y

    
    def adjustVertices(self,i, newPoint):
        self.Vertices[i] = newPoint
        

    def polyCollide(self, Polygon):
        polygonCollision = False

        return polygonCollision
        

    def returnDuplicate(self):
        newVerts = self.Vertices
        newPoly = Polygon(self.x, self.y, newVerts)
        return newPoly


    def mapImage(self):
        pass
    
    
    def drawPoly(self, Surface):
        for i in range(0, len(self.Vertices)):
            if i != len(self.Vertices) - 1:
                pygame.draw.line(Surface, (0, 0, 0), (self.Vertices[i][0]+self.x, self.Vertices[i][1]+self.y),
                            (self.Vertices[i+1][0]+self.x, self.Vertices[i+1][1]+self.y))
            if i == len(self.Vertices) - 1:
                pygame.draw.line(Surface, (0, 0, 0), (self.Vertices[i][0]+self.x, self.Vertices[i][1]+self.y),
                             (self.Vertices[0][0]+self.x, self.Vertices[0][1]+self.y))
                    



