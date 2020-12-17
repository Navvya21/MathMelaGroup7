import json
import tkinter
from tkinter import *
import random
from tkinter.filedialog import askopenfile 

# load questions and answer choices from json file
with open('./data3.json', encoding="utf8") as f:
    data3 = json.load(f)

# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data3[0].values()]
answers_choice = [v for v in data3[1].values()]

answers = [2,1,2,2,2,1,2,1,1,0] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score == 25:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text = "Awesome! Your score is 25!\n You have cleared all levels")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')
    elif (score == 20):
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text= "Awesome!!Your score is 20!\n You have cleared all levels")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')
    elif (score == 15):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text= "Not Bad!!Your score is 15!\n You have cleared all levels")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')
    elif (score == 10):
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text= "Work Harder!!Your score is 10!\nYou didn't clear the last level")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')
    elif (score == 5):
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text= "Work Harder!!Your score is 5!\n You didn't clear the last level")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text= "Work harder!!Your score is 0!\n You didn't clear the last level")
        btn = Button(root, text = 'Game Over !', bd = '5',command = root.destroy)
        btn.pack(side = 'top')


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
                calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Math Mela Std 6 Group no 7.")
root.geometry("1000x800")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="startimage.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Math Mela Std 6 Group 7",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Level 3: Challenging: Click Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 5 questions\n Each question is 5 points. 15 seconds per question.\n Once you click it is the final choice",
    width = 100,
    font = ("Times",15),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
