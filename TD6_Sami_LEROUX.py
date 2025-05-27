from tkinter import *
import random
import numpy as np
# Les boutons à gauche ne font qu'enlever les lignes correspondantes de l'affichage.

class Data:
    def __init__(self,list_,max_entrelacs,n_fils):
        self.list = list_
        self.max_entrelacs = max_entrelacs
        self.n_fils = n_fils
        self.init_list()
        self.D_count = {x : 0 for x in set(self.list)}
        self.grid = np.array([[0 for j in range(2*len(self.list)+1)] for i in range(max(self.list)+1)])
        self.modif_grid()
        print(self.grid)
        self.is_r_node()
        print(self.grid)

    def modif_grid(self):
        for i in range(len(self.list)):
            self.grid[self.list[i],2*i+1] = 1

    def is_r_node(self):
        for i in range(self.grid.shape[0]):
            a = -1
            for j in range(self.grid.shape[1]):
                if i==0:
                    if self.grid[i, j] == 1:
                        if a != -1:
                            self.grid[i, a] = 2
                            self.grid[i, j] = 2
                        else:
                            a = j
                    if self.grid[i + 1, j] == 1:
                        a = -1
                        print(i+1,j,a)
                elif i==self.grid.shape[0]-1:
                    if self.grid[i, j] == 1:
                        if a != -1:
                            self.grid[i, a] = 2
                            self.grid[i, j] = 2
                            a = -1
                        else:
                            a = j
                    if self.grid[i - 1, j] == 1 :
                        a = -1
                else:
                    if self.grid[i,j]==1:
                        if a != -1:
                            self.grid[i,a]=2
                            self.grid[i,j]=2
                            a=-1
                        else:
                            a = j
                    if self.grid[i-1,j]==1 or self.grid[i+1,j]==1:
                        a=-1




    def init_list(self):
        if self.max_entrelacs != 0:
            self.list = np.random.randint(self.max_entrelacs+1,size=self.n_fils)

    def entrelacs(self,w,h,Lcolor,Lcolor_copy,C,top,shuffle=False):
        sortie = list(range(max(self.list) + 2))
        list_ = self.list
        y_init = h/2
        x0, y0 = 0, y_init
        Lcolor = Lcolor[:max(list_)+2]
        for n in list_:
            y0 = y_init
            x1 = x0 + w
            for i in range(max(list_)+2):
                y1 = y0
                C.create_line(x0,y0,x1,y1, fill=Lcolor[i])
                y0 += h
            x0=x1
            x1 = x0+w
            for i in range(n):
                y0 = y_init + i * h
                y1 = y0
                C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            if max(list_)+1> n+1:
                for i in range(n+2,max(list_)+2):
                    y0 = y_init + i * h
                    y1 = y0
                    C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            C.create_line(x0,y_init+n*h,x1,y_init+(n+1)*h, fill=Lcolor[n])
            C.create_line(x0, y_init + (n + 1) * h, x1, y_init + n * h, fill=Lcolor[n+1])
            color_0 = Lcolor[n]
            Lcolor[n]=Lcolor[n+1]
            Lcolor[n + 1] = color_0
            sortie_0 = sortie[n]
            sortie[n] = sortie[n + 1]
            sortie[n + 1] = sortie_0
            x0 = x1
        y0 = y_init
        x1 = x0 + w
        for i in range(max(list_) + 2):
            y1 = y0
            C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            y0 += h
        C.grid(row=0, column=1,rowspan=max(self.list)+2,columnspan=2)
        sortie_lab = Label(top, text="Sortie = "+ str(sortie))
        sortie_lab.grid(row=max(self.list)+2,column = 2)
        if shuffle == True:
            Lcolor_copy=Lcolor.copy()
        top.mainloop()

class App:

    def __init__(self, w, h, list_=[],max_entrelacs=0,n_fils=0):
        self.data = Data(list_,max_entrelacs=max_entrelacs,n_fils=n_fils)
        self.w = w
        self.h = h
        self.bg_color = "white"
        self.top = Tk()
        width = w*(2 * len(self.data.list) + 1)
        height = h*(max(self.data.list) + 2)
        self.Lcolor_init = ["red","green","blue","orange","yellow","pink","purple","grey","black","salmon","OliveDrab1","light blue","plum1","purple4",]
        self.Lcolor = self.Lcolor_init.copy()
        self.Lcolor_copy = self.Lcolor.copy()
        self.C = Canvas(self.top,width=width,height=height,bg=self.bg_color)
        self.b1 = Button(self.top, text="Quit", command=self.top.destroy)
        self.b2 = Button(self.top, text="Shuffle", command=self.shuffle)
        list_lab = Label(self.top, text="List = "+ str(self.data.list))
        self.b1.grid(row=max(self.data.list)+3,column=1)
        self.b2.grid(row=max(self.data.list)+3,column=2)
        list_lab.grid(row=max(self.data.list)+2,column=1)
        self.buttons = []
        self.display_left_buttons()
        self.data.entrelacs(self.w,self.h,self.Lcolor,self.Lcolor_copy,self.C,self.top,shuffle=True)

    def display_left_buttons(self):
        for i in range(max(self.data.list)+2):
            self.buttons.append(Button(self.top, text="-", command=self.erase(i)))
            self.buttons[i].grid(row = i, column = 0)

    def erase(self,i):
        def erase_i():
            if self.buttons[i]["text"]=="-":
                self.buttons[i]["text"] = "+"
                self.Lcolor[i] = self.bg_color
            else:
                self.buttons[i]["text"] = "-"
                self.Lcolor[i]=self.Lcolor_copy[i]
            self.data.entrelacs(self.w,self.h,self.Lcolor,self.Lcolor_copy,self.C,self.top)
        return erase_i

    def shuffle(self):
        for i in range(max(self.data.list)+2):
            self.buttons[i]["text"] = "-"
        self.Lcolor = self.Lcolor_init
        random.shuffle(self.Lcolor)
        self.C.delete("all")
        self.data.entrelacs(self.w,self.h,self.Lcolor,self.Lcolor_copy,self.C,self.top,shuffle=True)




if __name__=="__main__":
    app = App(30,30,[3,1,0,1,0,1,1,0,1,2,1,3,0],0,9)
    print(np.random.randint(3+1,size=3))
    print(6%2)
    print(set([1,1,0]))
