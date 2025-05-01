from tkinter import *
import random
from numpy.ma.extras import column_stack

# Les boutons à gauche ne font qu'enlever les lignes correspondantes de l'affichage.

class Window:


    def __init__(self, width, height, w, h, list_):
        self.w = w
        self.h = h
        self.bg_color = "white"
        self.list = list_
        self.top = Tk()
        width = w*(2 * len(list_) + 1)
        height = h*(max(list_) + 2)
        self.Lcolor_init = ["red","green","blue","orange","yellow","pink","purple","grey","black","salmon","OliveDrab1","light blue","plum1","purple4",]
        self.Lcolor = self.Lcolor_init.copy()
        self.Lcolor_copy = self.Lcolor.copy()
        self.C = Canvas(self.top,width=width,height=height,bg=self.bg_color)
        self.b1 = Button(self.top, text="Quit", command=self.top.destroy)
        self.b2 = Button(self.top, text="Shuffle", command=self.shuffle)
        list_lab = Label(self.top, text="List = "+ str(self.list))
        self.b1.grid(row=max(self.list)+3,column=1)
        self.b2.grid(row=max(self.list)+3,column=2)
        list_lab.grid(row=max(self.list)+2,column=1)
        self.buttons = []
        self.display_left_buttons()



    def display_left_buttons(self):
        for i in range(max(self.list)+2):
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
            self.entrelacs()
        return erase_i

    def shuffle(self):
        for i in range(max(self.list)+2):
            self.buttons[i]["text"] = "-"
        self.Lcolor = self.Lcolor_init
        random.shuffle(self.Lcolor)
        self.C.delete("all")
        self.entrelacs(True)


    def entrelacs(self,shuffle=False):
        sortie = list(range(max(self.list) + 2))
        w,h = self.w,self.h
        list_ = self.list
        y_init = h/2
        x0, y0 = 0, y_init
        Lcolor = self.Lcolor[:max(list_)+2]
        for n in list_:
            y0 = y_init
            x1 = x0 + w
            for i in range(max(list_)+2):
                y1 = y0
                self.C.create_line(x0,y0,x1,y1, fill=Lcolor[i])
                y0 += h
            x0=x1
            x1 = x0+w
            for i in range(n):
                y0 = y_init + i * h
                y1 = y0
                self.C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            if max(list_)+1> n+1:
                for i in range(n+2,max(list_)+2):
                    y0 = y_init + i * h
                    y1 = y0
                    self.C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            self.C.create_line(x0,y_init+n*h,x1,y_init+(n+1)*h, fill=Lcolor[n])
            self.C.create_line(x0, y_init + (n + 1) * h, x1, y_init + n * h, fill=Lcolor[n+1])
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
            self.C.create_line(x0, y0, x1, y1, fill=Lcolor[i])
            y0 += h
        self.C.grid(row=0, column=1,rowspan=max(self.list)+2,columnspan=2)
        sortie_lab = Label(self.top, text="Sortie = "+ str(sortie))
        sortie_lab.grid(row=max(self.list)+2,column = 2)
        if shuffle == True:
            self.Lcolor_copy=self.Lcolor.copy()
        self.top.mainloop()

if __name__=="__main__":
    window = Window(1000,500,30,30,[3,1,0,0,0,2,2,7,4,3,2,2,2,8,0])
    window.entrelacs(shuffle=True)