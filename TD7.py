import time

import numpy as np
import random
from tkinter import *
import tkinter as tk

class Data:

    def __init__(self,graph):
        self.graph = graph
        self.k = 100.
        self.m = 5.
        self.l0 = 1
        self.dt = 0.05

    def calc_next_pos(self,a,vit,pos,a_copy,vit_copy,pos_copy,HEIGHT,WIDTH,i):
        X = []
        Y = []
        for j in self.graph[i]:
            X.append(pos[j][0])
            Y.append(pos[j][1])
        X = np.array(X,dtype=np.float32)
        Y = np.array(Y,dtype=np.float32)

        a_copy[i][0]  = self.k / self.m * sum((X - pos[i][0]) / ((X - pos[i][0]) ** 2 + (Y - pos[i][1]) ** 2) * ((((X - pos[i][0]) ** 2) + (Y - pos[i][1]) ** 2) ** (1 / 2)-self.l0))
        vit_copy[i][0]+= a[i][0]*self.dt
        a_copy[i][1] = self.k / self.m * sum((Y - pos[i][1]) / ((X - pos[i][0]) ** 2 + (Y - pos[i][1]) ** 2) * ((((X - pos[i][0]) ** 2) + (Y - pos[i][1]) ** 2) ** (1 / 2)-self.l0))
        vit_copy[i][1] += a[i][1] * self.dt
        pos_copy[i][1] += vit[i][1] * self.dt
        pos_copy[i][0]+=vit[i][0]*self.dt



class Affiche:

    def __init__(self,WIDTH,HEIGHT,graph):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.data = Data(graph)
        self.graph = self.data.graph
        self.pos = np.array([(random.randrange(WIDTH/4,3*WIDTH/4), random.randrange(HEIGHT/4,3*HEIGHT/4))
                        for i in range(len(graph))],dtype=np.float32)
        #self.pos = np.array([[WIDTH/2,HEIGHT/2],[WIDTH/2+100,HEIGHT/2+100]])
        self.vit = np.array([((random.randrange(1)-0.5)*10, (random.randrange(1)-0.5)*10)
                             for i in range(len(graph))],dtype=np.float32)
        self.vit = np.array([((random.randrange(-1,1)*10), (random.randrange(-1,1)*10))
                             for i in range(len(graph))],dtype=np.float32)
        self.vit = np.array([(0, 0) for i in range(len(graph))],dtype=np.float32)
        self.a = np.array([(0,0) for i in range(len(graph))],dtype=np.float32)

        self.top = Tk()
        self.bg_color="white"
        self.can = Canvas(self.top,width=WIDTH,height=HEIGHT,bg=self.bg_color)
        self.can.grid(row=0,column=0)
        self.top.bind("<f>", self.press_button)
        self.top.mainloop()

    def press_button(self,e):
        self.draw_changes()
        time.sleep(0.01)

    def draw(self,stop=False):
        self.can.delete("all")
        for i in range(len(self.graph)):
            for j in self.graph[i]:  # sucs de i a j
                if self.can.winfo_exists():
                    self.can.create_line(self.pos[i,0], self.pos[i,1], self.pos[j,0], self.pos[j,1])
                else:
                    print(["[INFO] Canvas doesn't exist anymore"])
        i=0
        for (x, y) in self.pos:
            self.can.create_oval(x - 8, y - 8, x + 8, y + 8, fill="#f3e1d4")
            self.can.create_text(x, y, text=str(i), fill="black")
            i+=1

    def draw_changes(self):
        a = self.a.copy()
        vit = self.vit.copy()
        pos = self.pos.copy()
        for i in range(len(self.graph)):
            self.data.calc_next_pos(self.a,self.vit,self.pos,a,vit,pos,self.WIDTH,self.HEIGHT,i)
        self.a = a.copy()
        self.vit = vit.copy()
        self.pos = pos.copy()
        self.draw(False)






if __name__=="__main__":

    graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
    [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
    graph2 = [[1,2],[0,2],[0,1]]
    affiche = Affiche(700,700,graph2)
    print(affiche.pos.shape)
    print(affiche.pos)
    affiche.draw_changes()
