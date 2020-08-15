from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk,Image
import time
import random

root = Tk()
root.title("The Flying Solo-Super Simple Quiz")
root.geometry("1080x600")
root.config(bg="SteelBlue4")
root.resizable(0, 0)

def show_fig():
    top = Toplevel()
    top.title("Figures are here.")
    top.geometry("800x650")
    top.config(bg="SteelBlue4")
    top.resizable(0, 0)
    photos = PhotoImage(file = r"img_001.png")
    photo2 = PhotoImage(file = r"img_002.png")
    photo3 = PhotoImage(file = r"img_003.png")
    photo4 = PhotoImage(file = r"img_004.png")
    photo5 = PhotoImage(file = r"img_005.png")
    photo6 = PhotoImage(file = r"img_006.png")
    photo7 = PhotoImage(file = r"img_007.png")

    figure_25_1 = Label(top,image=photos)
    figure_25_2 = Label(top, image=photo2,bg="SteelBlue4")
    figure_43 = Label(top, image=photo3,bg="SteelBlue4")
    figure_44 = Label(top, image=photo4,bg="SteelBlue4")
    figure_45 = Label(top, image=photo5,bg="SteelBlue4")
    figure_46_1 = Label(top, image=photo6,bg="SteelBlue4")
    figure_46_2 = Label(top, image=photo7,bg="SteelBlue4") 

    figure_1_txt = Label(top, text= "Figure-1",bg="SteelBlue4",foreground="black",font = ('courier', 30, 'bold'))
    figure_2_txt = Label(top, text= "Figure-2",bg="SteelBlue4",foreground="black",font = ('courier', 30, 'bold'))
    figure_3_txt = Label(top, text= "Figure-3",bg="SteelBlue4",foreground="black",font = ('courier', 30, 'bold'))
    figure_4_txt = Label(top, text= "Figure-4",bg="SteelBlue4",foreground="black",font = ('courier', 30, 'bold'))
    figure_5_txt = Label(top, text= "Figure-5",bg="SteelBlue4",foreground="black",font = ('courier', 30, 'bold'))

    figure_1_txt.place(x=50,y=50)
    figure_2_txt.place(x=50,y=150)
    figure_3_txt.place(x=50,y=300)
    figure_4_txt.place(x=50,y=400)
    figure_5_txt.place(x=50,y=520)

    figure_25_1.place(x=200+50,y=50)
    figure_25_2.place(x=200+150,y=50)
    figure_43.place(x=200+50,y=150)
    figure_44.place(x=200+50,y=300)
    figure_45.place(x=200+50,y=400)
    figure_46_1.place(x=200+50,y=520)
    figure_46_2.place(x=200+250,y=520)
    mainloop()

start_time = 0
current_time = 0

user_name = ""
user_enroll = 0
user_sem = 0

photo = PhotoImage(file = r"jet.png")

v = StringVar()

sequence = [0,1,2,3,4,5,6,7,8,9,
            10,11,12,13,14,15,16,17,18,19,
            20,21,22,23,24,25,26,27,28,29,
            30,31,32,33,34,35,36,37,38,39,
            40,41,42,43,44,45,46,47,48,49
            ]

random.shuffle(sequence)

next_button_status = "Next"


instructions = ["1. The Quiz is of 20 minutes.",
                "2. Maximum score = 100 and Cut-Off Score = 40.",
                "3. Once answered the question you cannot change it.",
                "4. You cannot go back and see your previous questions as well.",
                "5. Some questions needs figure. To view the figures...SHOW FIGURES button is provided.",
                "6. Your Score will be displayed immediately after the quiz.",
                "7. To view the Score you will asked to enter a 'key'",
                "8. Key will be provided by our volunteers.",
                "9. Do not close the window before viewing score.",
                "10. If you close the window before viewing score, your score will be considered as ZERO.",
                "11. In case of any other queries talk to our volunteers."
                ]

questions = ["\nWhen a moving bus suddenly applies brakes, then the \npassengers sitting in it fall in the forward direction.\nThis can be explained by",
             "\n\nA particle is moving freely on the ground. Then, its",
             "\n\nRadius of gyration of a body depends on",
             "\nAn atom of carbon has 6 protons. It’s Mass number is \n12. How many neutrons are present in an atom of carbon?",
             "The acceleration due to gravity ‘g’ for objects on or near \nthe surface of the earth is related to the universal \ngravitation constant ‘G’ as (M is the mass of the earth and \nR is the radius)",
             "\nA deep sea diver may hurt his ear drum during diving \nbecause of",
             "\nA balloon filled up with gas would only go up in air it is \nfilled up with",
             "\n\nThe acid contained in vinegar is",
             "\nA hot object loses heat to its surroundings in the form of \nheat radiation. The rate of loss of heat depends upon",
             "\n\nThe spread in colors in a rainbow on sky is primarily due to",
             "\nWhich one among the following waves bats use to detect the \nobstacles in their flying path?",
             "\n\nWhich one of the following has the lowest melting point?",
             "\nTwo similarly charged bodies are kept 5 cm apart in the \nair. If the second body is shifted away from the first by \nanother 5 cm, their force of repulsion will be",
             "\nThe phenomenon of electromagnetic induction implies a \nproduction of induced ",
             "\nThe cleansing action of soap and detergent in the water \nis due to the formation of",
             "Select the word which is most nearly opposite in meaning \n[ANTONYM] to the capital word.\n\n'I have MALICE towards none'",
             "Select the word which is same in meaning [SYNONYM] to \nthe capital word.\n\n'He fell into a ABYSS of despair'",
             "\n\nWhat are you ___________  in the kitchen cupboard?",
             "P: the rain did not prevent\tQ: from being played\nR: to finish\tS: the match\nThe proper sequence should be:",
             "\n\nMany __________ decisions were taken at the meeting.",
             "\n\nWhat is the square root of i, where i = √-1?",
             "\n\nWhat is the binary equivalent of the decimal number 0.3125 ?",
             "\nWhat is the nth term of the sequence:\n\n1, 5, 9, 13, 17, …?",
             "\nThe number of permutations that can be formed from all \nletters of the word “BASEBALL” is-",
             "What is the order of the product of [x  y  z] ?\nReference Figure-1",
             "\nIf two rows of a determinant are identical, then what is the \nvalue of the determinant?",
             "\nWhat is the maximum value of ...\n\t“sin 3θ×cos2θ + cos 3θ×sin 2θ ”?",
             "The angle of elevation of the top of a tower from a point \n150m away from its base is 30 degrees. What is the \nheight of the tower?",
             "\nWhat is the inclination of the line\n       √3x - y -1 = 0?",
             "\n\nWhich is the derivative of x^3 with respect to x^2?",
             "\n\nIf “Country : President” then, “State : ____” ?",
             "\n\nChoose the word which is least like the other words \nin the group.",
             "\nWhich number would replace question mark in the series\n        7, 12, 19, ?, 39",
             "\nIf in a certain language MYSTIFY is coded as NZTUJGZ,\nhow is NEMESIS coded in that language?",
             "Pointing to a photograph, a man said,\n“I have no brother or sister but that man's \nfather is my father's son.”Whose photograph was it?",
             "A man is facing west. He turns 45° in the clockwise direction \nand then another 180° in the same direction \nand then 270° in the anticlockwise direction. \nWhich direction is he facing now?",
             "Arrange the given words in alphabetical order and tick \nthe one that comes first:",
             "\n   If ‘+’ means ‘+’, ‘-’ means ‘×’ and ‘×’ means ‘-’ \nthen 36 × 12 + 4 + 6 + 2 - 3 = ? ",
             "\nArrange the following in a meaningful sequence: \n1.Birth\t 2.Death\t 3.Funeral\n4.Marriage \t5.Education",
             "If in the examination hall, you find that the question paper is\ntoo tough to be answered satisfactorily by you, the best \nthing to do for you is to :",
             "\nIn 2019, Abhijit Banerjee won the Nobel Memorial prize \nin which field?",
             "\nReena is twice as old as Sunita. Three years ago, she was \nthree times as old as Sunita. How old is Reena now?",
             "This box is rolled three times and three positions are \nshown: Find the number opposite to 1?\nReference Figure-2",
             "Choose the alternative which is closely resembles the mirror \nimage of the given: Reference Figure-3",
             "Choose the figure which is different from the rest.\nReference Figure-4",
             "Find out the figure which contains (X) as its part.\nReference Figure-5",
             "\nWhich Indian American business executive got promoted as\nCEO of Alphabet Inc.?",
             "\nWho was the chief guest of 71th Republic Day Parade held \non 26 January 2020?",
             "\n\nWho is the First Chief of Defence Staff?",
             "\nWhich of the following is a helicopter used by the \nIndian Air Force?"
             ]
answers = []
options_for_questions = [
    ["Theory of relativity","Newton’s First Law","Newton’s Second Law","Newton’s Third Law"],
    ["Kinetic Energy is always greater than zero","Potential energy is greater than zero and kinetic energy is less than zero","Potential energy is less than zero and kinetic energy is greater than zero","Potential energy is zero and kinetic energy is less than zero"],
    ["Mass and size of body","Mass distribution and axis of rotation ","Size of body","Mass of body"],
    ["12","10","6","14"],
    ["G = gM/R^2","g = GM/R^2","M = gG/R^2","R = gG/M^2"],
    ["Lack of oxygen","High atmospheric pressure","High water pressure ","All of the Above"],
    ["A gas whose density is lower than air","A gas whose density is higher than air","Cold Air","Water vapour"],
    ["Acetic acid","Ascorbic acid","Citric acid","Tartaric acid"],
    ["Temperature of the object","Temperature of the surroundings","Temperature difference between the object and its surroundings","Average Temperature of the object and its surroundings"],
    ["Dispersion of sunlight","Reflection of sunlight","Refraction of sunlight","Total internal reflection of sunlight"],
    ["Infrared Waves","Electromagnetic Waves","Ultrasonic Waves","Radio Waves"],
    ["Sodium","Gallium","Calcium","Aluminium"],
    ["Doubled","Halved","Quadrupled","Reduced to one-forth"],
    ["Resistance in a coil when the magnetic field changes with time","Capacitance in a coil when an electric field changes with time","Current in a coil when an magnetic field changes with time ","Voltage in a coil when an electric field changes with time"],
    ["Acid","Salt","Micelles","Base"],
    ["sympathy","goodwill","friendship","attraction"],
    ["well","deep pit","sea","hollow"],
    ["Looking in","Looking on","Looking for","Looking to"],
    ["P Q R S","P S Q R","P S R Q","S Q P R"],
    ["hectic","historic","historical","histrionic"],
    ["(1+i)/2","(1-i)/2","(1+i)/√2 ","None of these"],
    ["0.0111","0.1010","0.0101","0.1111"],
    ["4n - 3","2n + 1","2n - 1 ","None of these"],
    ["540","1260","3780","5040"],
    ["3 × 1","1 × 1 ","1 × 3","3 × 3"],
    ["0","1","-1","Can be any real value"],
    ["0","1/√2","1","√2"],
    ["50 m","150 m","50/√3 m","50√3 m"],
    ["30 degrees","60 degrees","135 degrees","150 degrees"],
    ["3x^2","x","3x/2","3/2"],
    ["Governor","Chief Minister","Prime Minister","Citizen"],
    ["Butter","Oil","Cheese","Cream"],
    ["29","24","26","28"],
    ["MDLHRDR","OFNFTJT","ODNHTDR","PGOKUGU "],
    ["His own","His son's","His father's","None of these "],
    ["South","North-west","West","South-west"],
    ["Cloud","Chandelier","China","Chain"],
    ["2","18","42","6"],
    ["4,5,3,1,2","2,3,4,5,1","1,5,4,2,3","1,3,4,5,2"],
    ["tell the examiner that the questions are out of course.","provoke the candidates to walk out of the examination hall.","try to know something from your neighbor.","try to solve the questions as much as you know with a cool head."],
    ["Physiology or Medicine","Literature","Economic Sciences","Peace"],
    ["6 years","7 years","8 years","12 years"],
    ["2","6","5","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["Satya Nadella","Rajeev Suri","Ajaypal Banga","Sundar Pichai"],
    ["Jair Bolsonaro","Queen Elizabeth II","Donald Trump","Imran Khan"],
    ["General Mukund Naravane","General Bipin Rawat","Wing Commander Abhinandan","Admiral Kadambir Singh"],
    ["Sukhoi Su 30MKI","Boeing 747","AH 64 Apache","Dassault Rafale"]
    ]

ans=["B","A","B","C","B","C","A","A","C","A","C","B","D","C","C","B","B","C","B","B","C","C","A","D","B","A","C","D","B","C","A","B","D","B","B","D","D","C","C","D","C","D","C","D","C","A","D","A","B","C"]

current = 1

users_answer = StringVar()
score = 0
cut_off_marks = 40
def screen_9():
    global score
    global cut_off_marks
    for i in range(0,50):
        if answers[i]==ans[sequence[i]]:
            score+=2
    txt = Label(root, text= "Cut-Off Marks = "+str(cut_off_marks)+"\nYour Score = "+str(score),bg="SteelBlue4",foreground="white",font = ('Arial', 30, 'bold'))
    if score>=cut_off_marks:
        msg = Label(root, text= "Congratulations!!! You are qualified for the next round.",bg="SteelBlue4",foreground="pink",font = ('courier', 30, 'bold'))
    else:
        msg = Label(root, text= "Sorry. You cannot play the next round.",bg="SteelBlue4",foreground="pink",font = ('courier', 30, 'bold'))

    txt.place(x=400,y=100)
    msg.place(x=100,y=250)
    mainloop()

def screen_8(password,txt,key,submit_button):
    txt.place_forget()
    key.place_forget()
    submit_button.place_forget()
    if password!="jeet is awesome":
        showerror("Error", "Wrong Key Entered")
        screen_7()
    else:
        screen_9()

def screen_7():
    txt = Label(root, text="The Test has Ended.\nEnter the key to view your result...",bg="SteelBlue4",foreground="white",font = ('Arial', 30, 'bold'))
    key = Entry(root,font = ('courier', 30, 'bold'),foreground="green")
    submit_button = Button(text="Submit",width=10,command=lambda:screen_8(key.get(),txt,key,submit_button),bg="violet",font = ('courier', 40, 'bold'))

    txt.place(x=200,y=100)
    key.place(x=300,y=200)
    submit_button.place(x=375,y=300)
    mainloop()
    
def screen_6(option_1,option_2,option_3,option_4,next_button,background,question_text,name_display,enrollment_display,sem_display,questions_left,timer,user_background,show_fig_button):
    
    option_1.place_forget()
    option_2.place_forget()
    option_3.place_forget()
    option_4.place_forget()
    next_button.place_forget()
    background.place_forget()
    question_text.place_forget()
    name_display.place_forget()
    enrollment_display.place_forget()
    sem_display.place_forget()
    questions_left.place_forget()
    timer.place_forget()
    user_background.place_forget()
    show_fig_button.place_forget()
    
    screen_7()

def status_update_next(t,option_1,option_2,option_3,option_4,next_button,background,question_text,name_display,enrollment_display,sem_display,questions_left,timer,user_background,show_fig_button):
    global current
    global answers
    answers.append(t)
    current+=1
    if current==51:
        screen_6(option_1,option_2,option_3,option_4,next_button,background,question_text,name_display,enrollment_display,sem_display,questions_left,timer,user_background,show_fig_button)
    else:
        
        option_1.place_forget()
        option_2.place_forget()
        option_3.place_forget()
        option_4.place_forget()
        next_button.place_forget()
        background.place_forget()
        question_text.place_forget()
        name_display.place_forget()
        enrollment_display.place_forget()
        sem_display.place_forget()
        questions_left.place_forget()
        timer.place_forget()
        user_background.place_forget()
        show_fig_button.place_forget()
        screen_5_quiz()

    
    
def temp_5(start_quiz_txt,start_button):
    global current
    global current_time
    global start_time

    start_quiz_txt.place_forget()
    start_button.place_forget()
    start_time = time.time()
    
    screen_5_quiz()

    
def screen_5_quiz():
    
    global current
    global current_time
    global start_time

    global user_name
    global user_enroll
    global user_sem


    if current == 50:
        next_status = "Submit"
    else:
        next_status = "Next"
    
    background = Label(root,bg="white",width=120,height=10)
    question_text = Label(root,bg="white",text=questions[sequence[current-1]],font = ('Arial', 20, 'bold'))

    user_background = Label(root,bg="tomato",width=35,height=40)

    current_time = time.time()
    seconds_left = int(60-(current_time-start_time)%60)
    minutes_left = int(19-(current_time-start_time)//60)
    
    timer = Label(root,bg="tomato",foreground="black",text="Time Left: "+str(minutes_left)+":"+str(seconds_left),font = ('Arial', 20, 'bold'))

    name_display = Label(root,bg="tomato",foreground="black",text="Name:\n"+user_name,font = ('Arial', 20, 'bold'))
    enrollment_display = Label(root,bg="tomato",foreground="black",text="Enrollment No.:\n"+user_enroll,font = ('Arial', 20, 'bold'))
    sem_display = Label(root,bg="tomato",foreground="black",text="SEM: "+user_sem,font = ('Arial', 20, 'bold'))
    questions_left = Label(root,bg="tomato",foreground="black",text="Questions\nRemaining: "+str(50-current),font = ('Arial', 20, 'bold'))
    
    timer.place(x=20,y=20)
    
    option_1 = Radiobutton(root,text=options_for_questions[sequence[current-1]][0],width=83,height=3,bg="white",variable=v,selectcolor="green",font = ('courier', 12, 'bold'),indicatoron=False,value="A")
    option_2 = Radiobutton(root,text=options_for_questions[sequence[current-1]][1],width=83,height=3,bg="white",variable=v,selectcolor="green",font = ('courier', 12, 'bold'),indicatoron=False,value="B")
    option_3 = Radiobutton(root,text=options_for_questions[sequence[current-1]][2],width=83,height=3,bg="white",variable=v,selectcolor="green",font = ('courier', 12, 'bold'),indicatoron=False,value="C")
    option_4 = Radiobutton(root,text=options_for_questions[sequence[current-1]][3],width=83,height=3,bg="white",variable=v,selectcolor="green",font = ('courier', 12, 'bold'),indicatoron=False,value="D")
    show_fig_button = Button(text="Show\nFigures",width=10,command=show_fig,bg="light green",font = ('Arial',25, 'bold'))
    next_button = Button(text=next_status,width=10,command=lambda: status_update_next(v.get(),option_1,option_2,option_3,option_4,next_button,background,question_text,name_display,enrollment_display,sem_display,questions_left,timer,user_background,show_fig_button),bg="green",font = ('Arial', 20, 'bold'))

    
    if current_time-start_time>=20*60:
        screen_6(option_1,option_2,option_3,option_4,next_button,background,question_text,name_display,enrollment_display,sem_display,questions_left,timer,user_background,show_fig_button)
        
    option_1.deselect()
    option_2.deselect()
    option_3.deselect()
    option_4.deselect()
    

    user_background.place(x=0,y=0)
    
    option_1.place(x=250,y=250)
    option_2.place(x=250,y=320)
    option_3.place(x=250,y=390)
    option_4.place(x=250,y=460)

    question_text.place(x=280,y=40)
    background.place(x=270,y=20)
 
    next_button.place(x=880,y=550)
    show_fig_button.place(x=20,y=500)

    
    questions_left.place(x=20,y=100)
    name_display.place(x=20,y=200)
    enrollment_display.place(x=20,y=300)
    sem_display.place(x=10,y=400)
        
    mainloop()


    
def screen_4_start_quiz(instructions_label,next_button,instruction_1,instruction_2,instruction_3,instruction_4,instruction_5,instruction_6,instruction_7,instruction_8,instruction_9,instruction_10,instruction_11):
    
    instructions_label.grid_forget()
    next_button.place_forget()

    instruction_1.place_forget()
    instruction_2.place_forget()
    instruction_3.place_forget()
    instruction_4.place_forget()
    instruction_5.place_forget()
    instruction_6.place_forget()
    instruction_7.place_forget()
    instruction_8.place_forget()
    instruction_9.place_forget()
    instruction_10.place_forget()
    instruction_11.place_forget()
    
    start_quiz_txt = Label(root,text="When you are ready click the button...",bg="SteelBlue4",font = ('Arial', 20, 'bold'))
    start_button = Button(text="Start Quiz",width=10,command=lambda: temp_5(start_quiz_txt,start_button),bg="violet",font = ('courier', 40, 'bold'))

    start_quiz_txt.place(x=300,y=150)
    start_button.place(x=370,y=200)


# screen-3 ----- Quiz Instructions
def screen_3_instructions():
    global instructions

    instructions_label = Label(root, text="Instructions",foreground="white",bg="SteelBlue4",font = ('Arial', 30, 'bold'))

    instruction_1 = Label(root, text=instructions[0],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_2 = Label(root, text=instructions[1],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_3 = Label(root, text=instructions[2],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_4 = Label(root, text=instructions[3],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_5 = Label(root, text=instructions[4],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_6 = Label(root, text=instructions[5],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_7 = Label(root, text=instructions[6],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_8 = Label(root, text=instructions[7],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_9 = Label(root, text=instructions[8],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_10 = Label(root, text=instructions[9],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    instruction_11 = Label(root, text=instructions[10],foreground="yellow",bg="SteelBlue4",font = ('courier', 15, 'bold'))
    
    next_button = Button(text="Next",width=10,command=lambda: screen_4_start_quiz(instructions_label,next_button,instruction_1,instruction_2,instruction_3,instruction_4,instruction_5,instruction_6,instruction_7,instruction_8,instruction_9,instruction_10,instruction_11),bg="green",font = ('Arial', 20, 'bold'))

    instruction_1.place(x=20,y=20+50)
    instruction_2.place(x=20,y=20+90)
    instruction_3.place(x=20,y=20+130)
    instruction_4.place(x=20,y=20+170)
    instruction_5.place(x=20,y=20+210)
    instruction_6.place(x=20,y=20+250)
    instruction_7.place(x=20,y=20+290)
    instruction_8.place(x=20,y=20+330)
    instruction_9 .place(x=20,y=20+370)
    instruction_10.place(x=20,y=20+410)
    instruction_11.place(x=20,y=20+450)
    instructions_label.grid(row=0,column=0,padx=450)

    next_button.place(x=850,y=500)
    mainloop()
    
def submit(response,a,b,c,name_label,enroll_num_label,sem_label,name_text_box,enroll_num_text_box,sem_text_box,submit_button):
    global user_name
    global user_enroll
    global user_sem
    user_name = a
    user_enroll = str(b)
    user_sem = str(c)
    if user_name == "":
        user_name = "Bewakoof Insaan"
    if user_enroll == "":
        user_enroll = "111222333444"
    if user_sem == "":
        user_sem = "0"

    if response:
        name_label.grid_forget()
        enroll_num_label.grid_forget()
        sem_label.grid_forget()
        name_text_box.grid_forget()
        enroll_num_text_box.grid_forget()
        sem_text_box.grid_forget()
        submit_button.grid_forget()
        screen_3_instructions()
     
# screen-2 ----- Enter Your Details
def screen_2(flying_solo_logo,flying_solo_txt,quiz_txt,devloper_txt,next_button):

    flying_solo_logo.place_forget()
    flying_solo_txt.place_forget()
    quiz_txt.place_forget()
    devloper_txt.place_forget()
    next_button.place_forget() 
  
    name_label = Label(root, text="Name",bg="SteelBlue4",font = ('Arial', 30, 'bold'))
    enroll_num_label = Label(root, text="Enroll No",bg="SteelBlue4",font = ('Arial', 30, 'bold'))
    sem_label = Label(root, text="Semester",bg="SteelBlue4",font = ('Arial', 30, 'bold'))


    name_text_box = Entry(root,font = ('courier', 30, 'bold'),foreground="violet") 
    enroll_num_text_box = Entry(root,font = ('courier', 30, 'bold'),foreground="violet")
    sem_text_box = Entry(root,font = ('courier', 30, 'bold'),foreground="violet") 

    name_label.grid(row=0,column=0,sticky="e",padx=(200,0),pady=(150,5)) 
    enroll_num_label.grid(row=1,column=0,sticky="e",padx=(200,0),pady=5)
    sem_label.grid(row=2,column=0,sticky="e",padx=(200,0),pady=5)

    
    submit_button = Button(text="Submit",width=10,command=lambda: submit(askyesno('Confirm','Do you want to submit?'),name_text_box.get(),enroll_num_text_box.get(),sem_text_box.get(),name_label,enroll_num_label,sem_label,name_text_box,enroll_num_text_box,sem_text_box,submit_button),bg="green",font = ('Arial', 20, 'bold'))
        
    name_text_box.grid(row=0,column=1,pady=(150,5),sticky="w") 
    enroll_num_text_box.grid(row=1,column=1,pady=5,sticky="w")
    sem_text_box.grid(row=2,column=1,pady=5,sticky="w")

    submit_button.grid(row=3,column=1,padx=(20,0),sticky="n")
    mainloop()


flying_solo_logo = Label(root, image=photo,bg="SteelBlue4") 
flying_solo_txt = Label(root, text="The Flying Solo",bg="SteelBlue4",foreground="yellow",font = ('Helvetica', 50, 'bold'))
quiz_txt = Label(root, text="Super Simple Quiz",bg="SteelBlue4",foreground="white",font = ('Arial', 30, 'bold'))
devloper_txt = Label(root, text="Devloped By: JEET DHANESHA",bg="SteelBlue4",foreground="light salmon",font = ('Helvetica', 20, 'bold italic'))
next_button = Button(text="Next",width=10,bg="green",command=lambda: screen_2(flying_solo_logo,flying_solo_txt,quiz_txt,devloper_txt,next_button),font = ('Arial', 20, 'bold'))

flying_solo_logo.place(x=500,y=120)
flying_solo_txt.place(x=300,y=250)
quiz_txt.place(x=370,y=330)
devloper_txt.place(x=320,y=560)
next_button.place(x=850,y=500)

mainloop()
