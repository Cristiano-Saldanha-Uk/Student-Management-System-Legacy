import customtkinter as tk
import random
import pyttsx3
import mysql.connector
from tkinter import messagebox

def VoiceOver(Speach):
    changes=random.randint(0,2)
    engine = pyttsx3.init()
    engine.setProperty('rate',150)  
    engine.setProperty('volume', 0.7) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.say(Speach)
    engine.runAndWait()
    engine.stop()
#-------------------Main Window 
oot=tk.CTk()
oot.title("Student Panel")
oot.resizable(False,False)
oot.geometry("950x550")


#-------------------
def login():
    user=en1.get()
    passs=en.get()
    if passs =="3377":
        username=("Welcome"+user)
        VoiceOver(username)
        frame.destroy()
        button1.destroy()
        #-------------------
        gr()
        #-------------------
    else:
        exc=0
        VoiceOver("Access Denied")
tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")
#-------------------Login Gui
frame = tk.CTkFrame(master=oot)
frame.pack(pady=12, padx=10, fill="both", expand=True)
label11 = tk.CTkLabel(master=frame, text="", font=("Copperplate Gothic", 30,"bold"))
label11.pack(pady=12, padx=10)
label1 = tk.CTkLabel(master=frame, text="GEMS", font=("Copperplate Gothic", 30,"bold"))
label1.pack(pady=12, padx=10)

en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Username", corner_radius=1000,height=50, width=250)
en1.pack(pady=12, padx=10)

en=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Password", corner_radius=1000, show="*",height=50, width=250)
en.pack(pady=12, padx=10)

button1=tk.CTkButton(master=frame, corner_radius=1000 ,font=("Hebrew", 20,"bold"),text="Login",command=login,height=50, width=150)
button1.pack(pady=12, padx=10)
def gr():
    #-----------Searchdef Search():
    def Search():
        def Searching():
            def back():
                geg.destroy()
                Search()

            stu1=en21.get()
            stu=en1.get()
            if stu1 == "":
                '''global stu'''
                frame.destroy()
                print(stu)
                geg =  tk.CTkFrame(master=oot)
                geg.pack(pady=12, padx=10, fill="both", expand=True)
                button3=tk.CTkButton(master=geg,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
                button3.pack(pady=12, padx=10)

                connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
                cursor=connection.cursor()
                cursor.execute("select * from details;")

                label11 = tk.CTkLabel(master=geg,width=200,fg_color='#E77471', corner_radius=500, text="Searched Data", font=("Copperplate Gothic", 30,"bold"))
                label11.pack(pady=20, padx=15)

                #--------------Heading
                la= tk.CTkFrame(master=geg)
                la.pack(pady=5, padx=10, fill="both", expand=False)
                label11.pack(pady=5, padx=1)
                label11 = tk.CTkLabel(master=la,width=120,fg_color='#E77471', corner_radius=500, text='Id', font=("Copperplate Gothic", 30,"bold"))
                label11.pack(side='left',pady=5, padx=2)
                label12 = tk.CTkLabel(master=la,width=300,fg_color='#E77471', corner_radius=500, text='Name', font=("Copperplate Gothic", 30,"bold"))
                label12.pack(side='left',pady=5, padx=2)
                label13 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Age', font=("Copperplate Gothic", 30,"bold"))
                label13.pack(side='left',pady=5, padx=2)
                label14 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Grade', font=("Copperplate Gothic", 30,"bold"))
                label14.pack(side='left',pady=5, padx=2)
                label5= tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Section', font=("Copperplate Gothic", 30,"bold"))
                label5.pack(side='left',pady=5, padx=2)

                laa= tk.CTkFrame(master=geg)
                laa.pack(pady=5, padx=10, fill="both", expand=False)
                for i in cursor:
                    if int(i[0]) == int(stu) :
                        print(i)
                        label111 = tk.CTkLabel(master=laa,width=120,fg_color='#E77471', corner_radius=500, text=i[0], font=("Copperplate Gothic", 30,"bold"))
                        label111.pack(side='left',pady=5, padx=2)
                        label112 = tk.CTkLabel(master=laa,width=300,fg_color='#E77471', corner_radius=500, text=i[1], font=("Copperplate Gothic", 30,"bold"))
                        label112.pack(side='left',pady=5, padx=2)
                        label113 = tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[2], font=("Copperplate Gothic", 30,"bold"))
                        label113.pack(side='left',pady=5, padx=2)
                        label114 = tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[3], font=("Copperplate Gothic", 30,"bold"))
                        label114.pack(side='left',pady=5, padx=2)
                        label15= tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[4], font=("Copperplate Gothic", 30,"bold"))
                        label15.pack(side='left',pady=5, padx=2)
            else:
                frame.destroy()
                print(stu1)
                geg =  tk.CTkFrame(master=oot)
                geg.pack(pady=12, padx=10, fill="both", expand=True)
                button3=tk.CTkButton(master=geg,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
                button3.pack(pady=12, padx=10)

                connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
                cursor=connection.cursor()
                cursor.execute("select * from details;")

                label11 = tk.CTkLabel(master=geg,width=200,fg_color='#E77471', corner_radius=500, text="Searched Data", font=("Copperplate Gothic", 30,"bold"))
                label11.pack(pady=20, padx=15)
                #--------------Heading
                la= tk.CTkFrame(master=geg)
                la.pack(pady=5, padx=10, fill="both", expand=False)
                label11.pack(pady=5, padx=1)
                label11 = tk.CTkLabel(master=la,width=120,fg_color='#E77471', corner_radius=500, text='Id', font=("Copperplate Gothic", 30,"bold"))
                label11.pack(side='left',pady=5, padx=2)
                label12 = tk.CTkLabel(master=la,width=300,fg_color='#E77471', corner_radius=500, text='Name', font=("Copperplate Gothic", 30,"bold"))
                label12.pack(side='left',pady=5, padx=2)
                label13 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Age', font=("Copperplate Gothic", 30,"bold"))
                label13.pack(side='left',pady=5, padx=2)
                label14 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Grade', font=("Copperplate Gothic", 30,"bold"))
                label14.pack(side='left',pady=5, padx=2)
                label5= tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Section', font=("Copperplate Gothic", 30,"bold"))
                label5.pack(side='left',pady=5, padx=2)

                laa= tk.CTkFrame(master=geg)
                laa.pack(pady=5, padx=10, fill="both", expand=False)
                for i in cursor:
                    if str(i[1]) == str(stu1) :
                        print(i)
                        label111 = tk.CTkLabel(master=laa,width=120,fg_color='#E77471', corner_radius=500, text=i[0], font=("Copperplate Gothic", 30,"bold"))
                        label111.pack(side='left',pady=5, padx=2)
                        label112 = tk.CTkLabel(master=laa,width=300,fg_color='#E77471', corner_radius=500, text=i[1], font=("Copperplate Gothic", 30,"bold"))
                        label112.pack(side='left',pady=5, padx=2)
                        label113 = tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[2], font=("Copperplate Gothic", 30,"bold"))
                        label113.pack(side='left',pady=5, padx=2)
                        label114 = tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[3], font=("Copperplate Gothic", 30,"bold"))
                        label114.pack(side='left',pady=5, padx=2)
                        label15= tk.CTkLabel(master=laa,width=150,fg_color='#E77471', corner_radius=500, text=i[4], font=("Copperplate Gothic", 30,"bold"))
                        label15.pack(side='left',pady=5, padx=2)


        def back():
            frame.destroy()
            gr()
        #-----Search start gui
        frame2.destroy()
        frame = tk.CTkFrame(master=oot)
        frame.pack(pady=12, padx=10, fill="both", expand=True)
        en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Student ID", corner_radius=1000,height=50, width=250)
        en1.pack(pady=12, padx=10)
        label1 = tk.CTkLabel(master=frame, text="OR", font=("Copperplate Gothic", 20,"bold"))
        label1.pack(pady=5, padx=8)
        en21=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Name", corner_radius=1000,height=50, width=250)
        en21.pack(pady=12, padx=10)
        button2=tk.CTkButton(master=frame, font=("Hebrew", 20,"bold"),text="Enter", corner_radius=1000,command=Searching,height=50, width=250)
        button2.pack(pady=12, padx=10)
        button3=tk.CTkButton(master=frame,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
        button3.pack(pady=12, padx=10)

    #-----------View
    def View():
        def back():
            geg.destroy()
            gr()
        frame2.destroy()
        geg =  tk.CTkFrame(master=oot)
        geg.pack(pady=12, padx=10, fill="both", expand=True)
        button3=tk.CTkButton(master=geg,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
        button3.pack(pady=12, padx=10)

        connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
        cursor=connection.cursor()
        a=cursor.execute("select * from details;")
        scrollable_frame = tk.CTkScrollableFrame(master=geg, width=200, height=200)
        scrollable_frame.pack( side='right',fill="both",expand=True)
        label11 = tk.CTkLabel(master=scrollable_frame,width=200,fg_color='#E77471', corner_radius=500, text="DATA", font=("Copperplate Gothic", 30,"bold"))
        label11.pack(pady=12, padx=10)
        #--------------Heading
        la= tk.CTkFrame(master=scrollable_frame)
        la.pack(pady=5, padx=10, fill="both", expand=True)
        label11.pack(pady=5, padx=1)
        label11 = tk.CTkLabel(master=la,width=120,fg_color='#E77471', corner_radius=500, text='Id', font=("Copperplate Gothic", 30,"bold"))
        label11.pack(side='left',pady=5, padx=2)
        label12 = tk.CTkLabel(master=la,width=300,fg_color='#E77471', corner_radius=500, text='Name', font=("Copperplate Gothic", 30,"bold"))
        label12.pack(side='left',pady=5, padx=2)
        label13 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Age', font=("Copperplate Gothic", 30,"bold"))
        label13.pack(side='left',pady=5, padx=2)
        label14 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Grade', font=("Copperplate Gothic", 30,"bold"))
        label14.pack(side='left',pady=5, padx=2)
        label5= tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text='Section', font=("Copperplate Gothic", 30,"bold"))
        label5.pack(side='left',pady=5, padx=2)

        for i in cursor:
            la= tk.CTkFrame(master=scrollable_frame)
            la.pack(pady=5, padx=10, fill="both", expand=True)
            label11.pack(pady=5, padx=2)
            label11 = tk.CTkLabel(master=la,width=120,fg_color='#E77471', corner_radius=500, text=i[0], font=("Copperplate Gothic", 30,"bold"))
            label11.pack(side='left',pady=5, padx=2)
            label12 = tk.CTkLabel(master=la,width=300,fg_color='#E77471', corner_radius=500, text=i[1], font=("Copperplate Gothic", 30,"bold"))
            label12.pack(side='left',pady=5, padx=2)
            label13 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text=i[2], font=("Copperplate Gothic", 30,"bold"))
            label13.pack(side='left',pady=5, padx=2)
            label14 = tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text=i[3], font=("Copperplate Gothic", 30,"bold"))
            label14.pack(side='left',pady=5, padx=2)
            label5= tk.CTkLabel(master=la,width=150,fg_color='#E77471', corner_radius=500, text=i[4], font=("Copperplate Gothic", 30,"bold"))
            label5.pack(side='left',pady=5, padx=2)
        connection.commit()
        connection.close()
    def Add():
        def back():
            frame.destroy()
            gr()
        def adding():
            connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
            cursor=connection.cursor()
            a="insert into details (Name,Age,Grade,Section) values(%s,%s,%s,%s)"
            b=(en1.get(),Age.get(),Grade.get(),Secotion.get())
            cursor.execute(a,b)
            messagebox.showinfo("Confirmation","Details Added")
            connection.commit()
            connection.close()
        frame2.destroy()
        frame = tk.CTkFrame(master=oot, width=10)
        frame.pack(pady=12, padx=10, fill="both")
        en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Name", corner_radius=1000,height=50, width=250)
        en1.pack(pady=12, padx=10)
        Age=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Age", corner_radius=1000,height=50, width=250)
        Age.pack(pady=12, padx=10)
        Grade=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Grade", corner_radius=1000,height=50, width=250)
        Grade.pack(pady=12, padx=10)
        Secotion=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Section", corner_radius=1000,height=50, width=250)
        Secotion.pack(pady=12, padx=10)
        button2=tk.CTkButton(master=frame, font=("Hebrew", 20,"bold"),text="Enter", corner_radius=1000,command=adding,height=50, width=200)
        button2.pack(pady=12, padx=10)
        button3=tk.CTkButton(master=frame,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
        button3.pack(pady=60, padx=10)
        #--------Display
        ''' def dis():
            connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='project')
            cursor=connection.cursor()
            a=cursor.execute("select * from details;")
            scrollable_frame = tk.CTkScrollableFrame(master=geg, width=200, height=200)
            scrollable_frame.pack( side='right',fill="both",expand=True)
            label11 = tk.CTkLabel(master=scrollable_frame,width=200,fg_color='#E77471', corner_radius=500, text="DATA", font=("Copperplate Gothic", 30,"bold"))
            label11.pack(pady=5, padx=1)
            for i in cursor:
                label11 = tk.CTkLabel(master=scrollable_frame,width=500,fg_color='#E77471', corner_radius=500, text=i, font=("Copperplate Gothic", 30,"bold"))
                label11.pack(pady=5, padx=1)
            connection.commit()
            connection.close()
         dis()'''


    #-----------Delete
    def Delete():
        def back():
            frame.destroy()
            gr()

        def reamove():
            connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
            cursor=connection.cursor()
            sq="DELETE FROM details WHERE Id=%s"
            ad=[en1.get()]
            cursor.execute(sq,ad)
            connection.commit()
            connection.close()
            messagebox.showinfo("Confirmation","Details Deleted")
        frame2.destroy()
        frame = tk.CTkFrame(master=oot)
        frame.pack(pady=12, padx=10, fill="both", expand=True)
        en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Student ID", corner_radius=1000,height=50, width=250)
        en1.pack(pady=12, padx=10)
        button2=tk.CTkButton(master=frame, font=("Hebrew", 20,"bold"),text="Enter", corner_radius=1000,command=reamove,height=50, width=250)
        button2.pack(pady=12, padx=10)
        button3=tk.CTkButton(master=frame,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
        button3.pack(pady=12, padx=10)
    #-----------Update    
    def Update():
        def up():
            def ArwinCantUpdate():
                connection=mysql.connector.connect(host="localhost",username='root',password='2260',database='workers')
                cursor=connection.cursor()
                a="update details set name = %s, Age = %s, Grade = %s, Section = %s where id = %s"
                b=(en2.get(),Age.get(),Grade.get(),Secotion.get(),aa)
                cursor.execute(a,b)
                messagebox.showinfo("Confirmation","Details Updated")
                connection.commit()
                connection.close()

            def backk():
                frame1.destroy()
                Update()
            aa=en1.get()
            print(aa)
            frame.destroy()
            frame1 = tk.CTkFrame(master=oot, width=10)
            frame1.pack(pady=12, padx=10, fill="both",expand=True)
            en2=tk.CTkEntry(master=frame1 , font=("Hebrew", 15,"bold"), placeholder_text="Name", corner_radius=1000,height=50, width=250)
            en2.pack(pady=12, padx=10)
            Age=tk.CTkEntry(master=frame1 , font=("Hebrew", 15,"bold"), placeholder_text="Age", corner_radius=1000,height=50, width=250)
            Age.pack(pady=12, padx=10)
            Grade=tk.CTkEntry(master=frame1 , font=("Hebrew", 15,"bold"), placeholder_text="Grade", corner_radius=1000,height=50, width=250)
            Grade.pack(pady=12, padx=10)
            Secotion=tk.CTkEntry(master=frame1 , font=("Hebrew", 15,"bold"), placeholder_text="Section", corner_radius=1000,height=50, width=250)
            Secotion.pack(pady=12, padx=10)
            button2=tk.CTkButton(master=frame1, font=("Hebrew", 20,"bold"),text="Enter", corner_radius=1000,command=ArwinCantUpdate,height=50, width=200)
            button2.pack(pady=12, padx=10)
            button3=tk.CTkButton(master=frame1,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=backk,height=50, width=150)
            button3.pack(pady=60, padx=10)
        def back():
            frame.destroy()
            gr()
        frame2.destroy()
        frame = tk.CTkFrame(master=oot)
        frame.pack(pady=12, padx=10, fill="both", expand=True)
        en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Student ID", corner_radius=1000,height=50, width=250)
        en1.pack(pady=12, padx=10)
        button2=tk.CTkButton(master=frame, font=("Hebrew", 20,"bold"),text="Enter", corner_radius=1000,command=up,height=50, width=250)
        button2.pack(pady=12, padx=10)
        button3=tk.CTkButton(master=frame,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Back",command=back,height=50, width=150)
        button3.pack(pady=12, padx=10)
    def logout():
        VoiceOver("Logging Out")
        def login():
            user=en1.get()
            passs=en.get()
            if passs =="3377":
                username=("Welcome"+user)
                VoiceOver(username)
                frame.destroy()

                #-------------------
                gr()
            #-------------------
            else:
                exc=0
                VoiceOver("Access Denied")
        frame2.destroy()
        frame = tk.CTkFrame(master=oot)
        frame.pack(pady=12, padx=10, fill="both", expand=True)
        label1 = tk.CTkLabel(master=frame, text="GEMS", font=("Copperplate Gothic", 30,"bold"))
        label1.pack(pady=12, padx=10)

        en1=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Username", corner_radius=1000,height=50, width=250)
        en1.pack(pady=12, padx=10)

        en=tk.CTkEntry(master=frame , font=("Hebrew", 15,"bold"), placeholder_text="Password", corner_radius=1000, show="*",height=50, width=250)
        en.pack(pady=12, padx=10)

        button1=tk.CTkButton(master=frame, corner_radius=1000 ,font=("Hebrew", 20,"bold"),text="Login",command=login,height=50, width=150)
        button1.pack(pady=12, padx=10)

    #-------------------Portal Frame
    frame2 = tk.CTkFrame(master=oot)
    frame2.pack(pady=12, padx=10, fill="both", expand=True)
    label11 = tk.CTkLabel(master=frame2, text="Student Portal", font=("Copperplate Gothic", 30,"bold"))
    label11.pack(pady=12, padx=1)
    button11=tk.CTkButton(master=frame2, corner_radius=1000, font=("Hebrew", 20,"bold"),text="Search Student",command=Search,height=50, width=200)
    button11.pack(pady=12, padx=10)

    button22=tk.CTkButton(master=frame2, corner_radius=1000, font=("Hebrew", 20,"bold"),text="View Student",command=View,height=50, width=200)
    button22.pack(pady=12, padx=10)

    button33=tk.CTkButton(master=frame2, corner_radius=1000, font=("Hebrew", 20,"bold"),text="Add Student",command=Add,height=50, width=200)
    button33.pack(pady=12, padx=10)

    button44=tk.CTkButton(master=frame2, corner_radius=1000, font=("Hebrew", 20,"bold"),text="Delete Student",command=Delete,height=50, width=200)
    button44.pack(pady=12, padx=10)

    button55=tk.CTkButton(master=frame2, corner_radius=1000, font=("Hebrew", 20,"bold"),text="Update Student",command=Update,height=50, width=200)
    button55.pack(pady=12, padx=10)

    button66=tk.CTkButton(master=frame2,fg_color='#E77471',hover_color='#C24641', corner_radius=1000, font=("Hebrew", 20,"bold"),text="Logout",command=logout,height=50, width=150)
    button66.pack(pady=12, padx=10)
    #-------------------
oot.mainloop()
