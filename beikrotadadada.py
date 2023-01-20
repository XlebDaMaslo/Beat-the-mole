from tkinter import *
import random
import time
from _thread import start_new_thread
from PIL import ImageTk, Image

root = Tk()
root.title('Побей крота')
root.geometry('800x650')
b_st = Button(text="Старт", width=30, height=5, font="Arial 24")
b_ex = Button(text="Выход", width=30, height=5, font="Arial 24")

krots = []

pilBack = Image.open('background_test.jpg')
imBack = ImageTk.PhotoImage(pilBack)

pilneKrot = Image.open('nekrot_test.png')
imneKrot = ImageTk.PhotoImage(pilneKrot)
pilKrot = Image.open('3krot_test.png')
imKrot = ImageTk.PhotoImage(pilKrot)

def Start():
    global ochki, l2, root, krot
    b_st.destroy()
    b_ex.destroy()
    c1 = Canvas(root, width=800, height=150, bg='white')
    c1.create_text(400, 25, text="Игра Побей крота", 
                    justify=CENTER, font="Verdana 20")
    c2 = Canvas(root, width=800, height=500, bg='#90EE90')

    l1 = Label(c1, text="Игра Побей крота", font="Arial 24")


    ochki = 0
    l2 = Label(c1, text="Побито кротов " + str(ochki), font="Arial 12")

    #c2.create_oval(50, 10, 150, 110, width=2)
    spriteBack = c2.create_image(500,200,image=imBack)

    def krot_dviz():
        global rar, label,b_st, b_ex
        a = time.time()
        b = time.time()
        rar = random.choice(krots)
        print(krots)
        while True:
            if time.time() - b >= 10: #ограничение по времени
                #print('Время вышло.')
                c1.destroy()
                c2.destroy()
                txt = "Время вышло.\n" + 'Ваш счет: ' + str(ochki)
                label = Label(text=txt, font="Arial 60")
                b_st = Button(text="Старт", width=20, height=4, font="Arial 24")
                b_ex = Button(text="Выход", width=20, height=4, font="Arial 24")
                
                b_st.config(command=Start_second)
                b_ex.config(command=Exit)
                
                label.pack()
                b_st.pack()
                b_ex.pack()
                break
            elif time.time() - a < 1:
                pass
            else:
                #c2.itemconfig(krot[rar], fill='black')
                c2.itemconfig(rar, image = imneKrot)
                c2.tag_unbind(rar, '<Button-1>')
                root.update()
                #root.update()
                rar = random.choice(krots)
                print(rar)
                #c2.itemconfig(krot[rar], fill='red')
                c2.itemconfig(rar, image = imKrot)
                root.update()
                c2.tag_bind(rar, '<Button-1>', attack)
                a = time.time()
                
                
    def attack(event):
        global ochki, l2, root
        ochki += 1
        l2.destroy()
        l2 = Label(c1, text="Побито кротов " + str(ochki), font="Arial 12")
        l2.pack()
        root.update()
        #print(event)
        #c2.itemconfig(krot[rar], fill='black')
        c2.itemconfig(rar, image = imneKrot)
        c2.tag_unbind(rar, '<Button-1>')
        root.update()
        if ochki == 100:
            print('Получена очивка: Убица кратоф')
        
        
        


    l1.pack()
    l2.pack()
    c1.pack()
    c2.pack()

    chech = 0
    ah = 0
    ha = 0
    xex=100
    yey=200
    while chech != 3:
        chech += 1
        
        #print('cho')
        while ah != 3:
            #print('nuda')
            
            #krot += str(c2.create_oval(xex+50, yey-100, xex+150, yey, fill='black'))
            krots.append(c2.create_image(xex+50, yey-100, image = imneKrot))
            #print(krot)
            xex+=250
            ah+=1
            ha+=1
        yey+=150
        xex=100
        ah=0



    start_new_thread(krot_dviz,())
def Exit():
    global root
    root.destroy()
def Start_second():
    label.destroy()
    b_st.destroy()
    b_ex.destroy()
    Start()
b_st.config(command=Start)
b_ex.config(command=Exit)

b_st.pack()
b_ex.pack()
root.mainloop()
