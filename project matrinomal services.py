from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
ob = Tk()
ob.title("divinebandhan.com")
ob.geometry("1000x1000")
def getyourcard1():
    CARD01.config(text= (CARDE01.get()), bg ="RED",fg = "BLACK", anchor= CENTER, width = "20", height = "2")
    CARD01.place(x = 480, y = 50)
    
    CARD001.config(text= (CARDE001.get()), bg ="RED",fg = "BLACK", anchor= CENTER, width = "20", height = "2" )
    CARD001.place(x = 750, y = 50)
    CARDBG1.config(text= (CARDE1.get()),bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG1.place(x = 430, y = 80)
    CARDBG2.config(text= (CARDE2.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG2.place(x = 430, y = 110)
    CARD7.config(text= (CARDE3.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD7.place(x = 430, y = 140)
    CARD8.config(text= (CARDE4.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD8.place(x = 430, y = 170)
    CARD9.config(text= (CARDE5.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD9.place(x = 430, y = 200)
    CARD10.config(text= (CARDE6.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD10.place(x = 430, y = 230)
    CARD11.config(text= (CARDE7.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD11.place(x = 430, y = 260)
    CARD12.config(text= (CARDE8.get()), bg ="BISQUE",fg = "MAROON", anchor= E, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD12.place(x = 430, y = 290)
    CARD13.config(text= (CARDE9.get()), bg ="BISQUE",fg = "MAROON", anchor= E, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD13.place(x = 430, y = 320)
    CARD14.config(text= (CARDE10.get()), bg ="BISQUE",fg = "MAROON", anchor= E, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD14.place(x = 430, y = 350)
    CARD15.config(text= (CARDE11.get()), bg ="BISQUE",fg = "MAROON", anchor= E, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD15.place(x = 430, y = 380)
    CARD16.config(text= (CARDE12.get()), bg ="BISQUE",fg = "MAROON", anchor= E  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD16.place(x = 430, y = 410)
    
    CARDBG3.config(text= (CARDE13.get()), bg ="BISQUE",fg = "MAROON", anchor= E  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG3.place(x = 430, y = 440)
    
    CARDBG4.config(text= (CARDE14.get()), bg ="BISQUE",fg = "MAROON", anchor= E  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG4.place(x = 430, y = 470)
    CARDBG5.config(text= (CARDE15.get()), bg ="BISQUE",fg = "MAROON", anchor= E  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG5.place(x = 430, y = 500)
    CARDBG6.config(text= (CARDE16.get()), bg ="BISQUE",fg = "MAROON", anchor= CENTER  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG6.place(x = 430, y = 510)
    CARDBG7.config(text= (CARDE17.get()), bg ="red",fg = "white", anchor= CENTER  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG7.place(x = 430, y = 540)
    messagebox.showinfo("PLEASE MAKE SURE", "YOU CAN ALSO MAKE CHANGES IN THIS INVITATION CARD")
    
    
    
def getyourcard2():
    CARD01.config(text= (CARDE01.get()), bg ="RED",fg = "BLACK", anchor= CENTER, width = "20", height = "1")
    CARD01.place(x = 480, y = 50)
    
    CARD001.config(text= (CARDE001.get()), bg ="RED",fg = "BLACK", anchor= CENTER, width = "20", height = "1" )
    CARD001.place(x = 750, y = 50)
    CARDBG1.config(text= (CARDE1.get()),bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","12","bold"))
    CARDBG1.place(x = 430, y = 80)
    CARDBG2.config(text= (CARDE2.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG2.place(x = 430, y = 110)
    CARD7.config(text= (CARDE3.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD7.place(x = 430, y = 140)
    CARD8.config(text= (CARDE4.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD8.place(x = 430, y = 170)
    CARD9.config(text= (CARDE5.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD9.place(x = 430, y = 200)
    CARD10.config(text= (CARDE6.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD10.place(x = 430, y = 230)
    CARD11.config(text= (CARDE7.get()), bg ="BISQUE",fg = "MAROON", anchor= N, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD11.place(x = 430, y = 260)
    CARD12.config(text= (CARDE8.get()), bg ="BISQUE",fg = "MAROON", anchor= E, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD12.place(x = 430, y = 290)
    CARD13.config(text= (CARDE9.get()), bg ="BISQUE",fg = "MAROON", anchor= NE, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD13.place(x = 430, y = 320)
    CARD14.config(text= (CARDE10.get()), bg ="BISQUE",fg = "MAROON", anchor= NE, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD14.place(x = 430, y = 350)
    CARD15.config(text= (CARDE11.get()), bg ="BISQUE",fg = "MAROON", anchor= NE, width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD15.place(x = 430, y = 380)
    CARD16.config(text= (CARDE12.get()), bg ="BISQUE",fg = "MAROON", anchor= NE  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARD16.place(x = 430, y = 410)
    
    CARDBG3.config(text= (CARDE13.get()), bg ="BISQUE",fg = "MAROON", anchor= NE  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG3.place(x = 430, y = 440)
    
    CARDBG4.config(text= (CARDE14.get()), bg ="BISQUE",fg = "MAROON", anchor= NE  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG4.place(x = 430, y = 470)
    CARDBG5.config(text= (CARDE15.get()), bg ="BISQUE",fg = "MAROON", anchor= NE  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG5.place(x = 430, y = 500)
    CARDBG6.config(text= (CARDE16.get()), bg ="BISQUE",fg = "MAROON", anchor= CENTER  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG6.place(x = 430, y = 510)
    CARDBG7.config(text= (CARDE17.get()), bg ="white",fg = "maroon", anchor= CENTER  , width = "80", height = "2",font = ("TIMES NEW ROMAN","8","bold"))
    CARDBG7.place(x = 430, y = 540)
    messagebox.showinfo("PLEASE MAKE SURE", "YOU CAN ALSO MAKE CHANGES IN THIS INVITATION CARD")
    
        
def marriagecard():
    mc = Tk()
    mc.configure(background = "darkred")
    mc.geometry("1000x1000")
    global CARDBG1
    global CARDE01
    global CARDE001
    global CARDE1
    global CARDE2
    global CARDE3
    global CARDE4
    global CARDE5
    global CARDE6
    global CARDE7
    global CARDE8
    global CARDE9
    global CARDE10
    global CARDE11
    global CARDE12
    global CARDE13
    global CARDE14
    global CARDE15
    global CARDE16
    global CARDE17
    global CARDHEAD
    global CARD01
    global CARD001
    global CARD1
    global CARD2
    global CARD3
    global CARD4
    global CARD5
    global CARD6
    global CARD7
    global CARD8
    global CARD9
    global CARD10
    global CARD11
    global CARD12
    global CARD13
    global CARD14
    global CARD15
    global CARD16
    global CARDBG1
    global CARDBG2 
    global CARDBG3 
    global CARDBG4
    global CARDBG5 
    global CARDBG6
    global CARDBG7 
    cinvitor = StringVar()
    cinvitee = StringVar()
    cheading = StringVar()
    ccouplename = StringVar()
    cvenue = StringVar()
    cprogrammeheading = StringVar()
    cprogrammeday1 = StringVar()
    cprogrammeday2 = StringVar()
    cprogrammeday3 = StringVar()
    cprogrammeday4 = StringVar()
    crsvp1 = StringVar()
    crsvp2 = StringVar()
    crsvp3 = StringVar()
    crsvp4 = StringVar()
    crsvp5 = StringVar()
    crsvp6 = StringVar()
    crsvp7 = StringVar()
    crsvp8 = StringVar()
    crsvp9 = StringVar()
    crsvp10 = StringVar()
    
    CARDHEAD = Label(mc,text= "GET YOUR MARRIAGE CARD IN MINUTES ",bg ="RED",fg = "WHITE", anchor= CENTER, width = "120", height = "1",font = ("Franklin Gothic Medium","15","bold")).place(x = 0   , y = 0)
    CARDBG1 = Label(mc,text= "Dear\t\t\t\tI\t\t\t\tInvite you ",bg ="RED",fg = "BLACK", anchor= CENTER, width = "80", height = "2",font = ("Franklin Gothic Medium","8","bold")).place(x = 430   , y = 50)  

    CARD01 = Label(mc, text= "NAME OF INVITEE", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold")).place(x = 20, y = 50)
    CARDE01 = Entry(mc,width = "30",textvariable= cinvitor)
    CARDE01.place(x = 200, y = 50)
    CARD001 = Label(mc, text= "NAME OF INVITER", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold")).place(x = 20, y = 80)
    CARDE001 = Entry(mc,width = "30",textvariable= cinvitee)
    CARDE001.place(x = 200, y = 80)
    CARD1 = Label(mc, text= "ENTER SALUTATIONS", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold")).place(x = 20, y = 110)
    CARDE1 = Entry(mc,width = "30",textvariable= cheading)
    CARDE1.place(x = 200, y = 110)
    CARD2 = Label(mc, text= "ENTER HEADING DETAILS", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold")).place(x = 20, y = 140)
    CARDE2 = Entry(mc,width = "30",textvariable= ccouplename)
    CARDE2.place(x = 200, y = 140)
    CARD3 = Label(mc, text= "ENTER COUPLE DETAILS", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold")).place(x = 20, y = 170)
    CARDE3 = Entry(mc,width = "30",textvariable= cvenue)
    CARDE3.place(x = 200, y = 170)
    CARD4 = Label(mc, text= "PROGRAMME HEADING", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD4.place(x = 20, y = 200)
    CARDE4 = Entry(mc,width = "30",textvariable= cprogrammeheading)
    CARDE4.place(x = 200, y = 200)
    CARD04 = Label(mc, text= "PROGRAMME DAY1", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD04.place(x = 20, y = 230)
    CARDE4 = Entry(mc,width = "30",textvariable= cprogrammeday1)
    CARDE4.place(x = 200, y = 230)
    CARD05 = Label(mc, text= "PROGRAMME DAY2", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD05.place(x = 20, y = 260)
    CARDE5 = Entry(mc,width = "30",textvariable= cprogrammeday2)
    CARDE5.place(x = 200, y = 260)
    CARD06 = Label(mc, text= "PROGRAMME DAY3", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD06.place(x = 20, y = 290)
    CARDE6 = Entry(mc,width = "30",textvariable= cprogrammeday3)
    CARDE6.place(x = 200, y = 290)
    CARD07 = Label(mc, text= "PROGRAMME DAY4", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD07.place(x = 20, y = 320)
    CARDE7 = Entry(mc,width = "30",textvariable= cprogrammeday4)
    CARDE7.place(x = 200, y = 320)
    CARD08 = Label(mc, text= "RSVP", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD08.place(x = 20, y = 350)
    CARDE8 = Entry(mc,width = "30",textvariable= crsvp1)
    CARDE8.place(x = 200, y = 350)
    CARD09 = Label(mc, text= "RSVP NAME 1", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD09.place(x = 20, y = 380)
    CARDE9 = Entry(mc,width = "30",textvariable= crsvp2)
    CARDE9.place(x = 200, y = 380)
    CARD010 = Label(mc, text= "RSVP NAME 2", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD010.place(x = 20, y = 410)
    CARDE10 = Entry(mc,width = "30",textvariable= crsvp3)
    CARDE10.place(x = 200, y = 410)
    CARD011 = Label(mc, text= "RSVP NAME 3", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD011.place(x = 20, y = 440)
    CARDE11 = Entry(mc,width = "30",textvariable= crsvp4)
    CARDE11.place(x = 200, y = 440)
    CARD012 = Label(mc, text= "RSVP NAME 4", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD012.place(x = 20, y = 470)
    CARDE12 = Entry(mc,width = "30",textvariable= crsvp5)
    CARDE12.place(x = 200, y = 470)
    CARD013 = Label(mc, text= "RSVP NAME 1", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD013.place(x = 20, y = 500)
    CARDE13 = Entry(mc,width = "30",textvariable= crsvp6)
    CARDE13.place(x = 200, y = 500)
    CARD014 = Label(mc, text= "RSVP NAME 6", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD014.place(x = 20, y = 530)
    CARDE14 = Entry(mc,width = "30",textvariable= crsvp7)
    CARDE14.place(x = 200, y = 530)
    CARD015 = Label(mc, text= "RSVP NAME 7", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD015.place(x = 20, y = 560)
    CARDE15 = Entry(mc,width = "30",textvariable= crsvp8)
    CARDE15.place(x = 200, y = 560)
    CARD016 = Label(mc, text= "TEXT CHOICE", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD016.place(x = 20, y = 590)
    CARDE16 = Entry(mc,width = "30",textvariable= crsvp9)
    CARDE16.place(x = 200, y = 590)
    CARD016 = Label(mc, text= "TEXT CHOICE", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("Franklin Gothic Medium","8","bold"))
    CARD016.place(x = 20, y = 620)
    CARDE17 = Entry(mc,width = "30",textvariable= crsvp10)
    CARDE17.place(x = 200, y = 620)
    CARD5 = Label(mc)
    CARD5.place()
    CARD5 = Label(mc)
    CARD5.place()
    CARD6 = Label(mc)
    CARD6.place()
    CARD7 = Label(mc)
    CARD7.place()
    CARD7 = Label(mc)
    CARD7.place()
    CARD8 = Label(mc)
    CARD8.place()
    CARD9 = Label(mc)
    CARD9.place()
    CARD10 = Label(mc)
    CARD10.place()
    CARD11 = Label(mc)
    CARD11.place()
    CARD12 = Label(mc)
    CARD12.place()
    CARD13 = Label(mc)
    CARD13.place()
    CARD14 = Label(mc)
    CARD14.place()
    CARD15 = Label(mc)
    CARD15.place()
    CARD16 = Label(mc)
    CARD16.place()
    CARD01 = Label(mc)
    CARD01.place()
    CARD001 = Label(mc)
    CARD001.place()
    CARD001 = Label(mc)
    CARD001.place()
    CARDBG1 = Label(mc)
    CARDBG1.place()
    CARDBG2 = Label(mc)
    CARDBG2.place()
    CARDBG3 = Label(mc)
    CARDBG3.place()
    CARDBG4 = Label(mc)
    CARDBG4.place()
    CARDBG5 = Label(mc,)
    CARDBG5.place()
    CARDBG6 = Label(mc)
    CARDBG6.place()
    CARDBG7 = Label(mc)
    CARDBG7.place()
    MARRIAGECARD1 = Button(mc, text= "SHOW BISQUE3 COLOR", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "17", height = "1", command= getyourcard1)
    MARRIAGECARD1.place(x = 200, y = 720)
    MARRIAGECARD2 = Button(mc, text= "SHOW RED COLOR", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "17", height = "1", command= getyourcard2)
    MARRIAGECARD2.place(x = 400 , y = 720)
    mc.mainloop()

def passent():
    var.get()
    #global ppas3
    ppas3.config(text = (pe.get()),bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "20", height = "1")
    ppas3.place(x = 500, y = 318)
    
    

    

    
   
    
    
    
    
   
   
   #how to get value
   

 
  
    
# GET YOUR PASSES 
def pas():
    ob = Tk()
    global pe
    global ppas0
    global pen
    global ppas1
    global ppas2
    global ppas3
    global ppas5
    global var
    ppas0 = Label(ob, text= "NOW YOU CAN GET PASSES \nFOR SWAYAMWAR JUST TAKE SCREENSHOT OF \nYOUR PASS \nAND\n SHOW IT IN SWAYAMWAR", bg ="red",fg = "white", anchor= CENTER, width = "80", height = "50",font = ("TIMES NEW ROMAN","20","bold")).place(x = 1, y = 1)
    
    pen = Label(ob, text= "ENTER YOUR DETAILS TO GRAB THE PASS", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "40", height = "1",font = ("TIMES NEW ROMAN","10","bold")).place(x = 400, y = 30)
    entn = Button(ob, text= "PASS", bg ="YELLOW",fg = "BLACK", anchor= CENTER, width = "5", height = "1", command= passent)
    entn.place(x = 900, y = 30)
    var = StringVar()
    pe = Entry(ob,width = "30",textvariable= var)
    pe.place(x = 700, y = 30)
    ppas1 = Label(ob, text= "PASS", bg ="BLACK",fg = "WHITE", anchor= CENTER, width = "20", height = "2",font = ("TIMES NEW ROMAN","20","bold")).place(x = 500, y = 200)
    ppas2 = Label(ob, text= "SWAYAMWAR\nPARTICIPANT", bg ="MAROON",fg = "WHITE", anchor= CENTER, width = "20", height = "2",font = ("TIMES NEW ROMAN","20","bold")).place(x = 500, y = 250)
  
    ppas3 = Label (ob, text = "", bg ="MAROON",fg = "WHITE", anchor= CENTER, width = "20", height = "1",font = ("TIMES NEW ROMAN","20","bold"))
    ppas3.place(x = 500, y = 318)
    
    
    ppas5 = Label(ob, text= "WISH YOU \nBEST OF LUCK", bg ="MAROON",fg = "white", anchor= CENTER, width = "20", height = "2",font = ("TIMES NEW ROMAN","20","bold")).place(x = 500, y = 355)
    ppas5 = Label(ob, text= "THANK YOU\n FOR YOUR VISIT", bg ="BLACK",fg = "RED", anchor= CENTER, width = "20", height = "3",font = ("TIMES NEW ROMAN","20","bold")).place(x = 500, y = 419) 
      
    ob.mainloop()
def loginuserpage():
    USD = usdb.get()
    PSD = pasdb.get()
    if USD == "" and PSD =="":
        messagebox.showerror(title="error", message="PLEASE ENTER \nUSERNAME AND PASSWORD TO PROCEED")
    elif USD == "DBUSER" and PSD == "PASSWORD":
        messagebox.showinfo("LOGIN SUCCESSFULL\n WELCOME TO \nDIVINE BANDHAN")
        global MSE01
        global MSE1
        global var1
        global MSE3 
        global MSE4
        global MSE5
        global MSE6
        global MSE7
        global MSE8
        global MSE9
        global MSE10
        global MSE11
        global MSE12
        global MSE13
        global MSE14
        global MSDIVINETRVI
        global lfshowdata0
        global lfshowdata1
        global lfshowdata2
        global lfshowdata3
        global lfshowdata4
        global lfshowdata5
        global lfshowdata6
        global lfshowdata7
        global lfshowdata8
        global lfshowdata9
        global lfshowdata10
        global lfshowdata11
        global lfshowdata12
        global lfshowdata13
        global lfshowdata14
        
        global lfshowdata0A
        global lfshowdata1A
        global lfshowdata2A
        global lfshowdata3A
        global lfshowdata4A
        global lfshowdata5A
        global lfshowdata6A
        global lfshowdata7A
        global lfshowdata8A
        global lfshowdata9A
        global lfshowdata10A
        global lfshowdata11A
        global lfshowdata12A
        global lfshowdata13A
        global lfshowdata14A
    
    
        msno = StringVar()
        mname = StringVar()
        var1 = StringVar()
        mdob = StringVar()
        mperaddress = StringVar()
        mpresaddress = StringVar()
        mjobprofile = StringVar()
        manydosh = StringVar()
        mmobilenumber = StringVar()
        msmaritalstatus = StringVar()
        mstimeofbirth = StringVar()
        mmarriagechoice = StringVar()
        mssearchingfor = StringVar()
        memailid = StringVar()
        
        usen_0 = Label(ob, bg ="red",anchor= NW,fg = "maroon", width = "120", height = "60",font = ("garamond","20","bold"))
        usen_0.place(x = 1, y = 5)
        
        usen = Label(ob, text = "ENTER YOUR DETAILS HERE TO GET REGISTERD",bg ="bisque3",anchor= CENTER,fg = "black", width = "90", height = "1",font = ("garamond","20","bold"))
        usen.place(x = 0, y = 10)
       
        usen01 = Label(ob, text = "S NO",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen01.place(x = 10, y = 70)
        MSE01 = Entry(ob,width= "30",textvariable= msno)
        MSE01.place(x =170 , y =70 )
        usen02 = Label(ob, text = "NAME OF MATCH",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen02.place(x = 10, y = 100)
        MSE1 = Entry(ob,width= "30",textvariable= mname)
        MSE1.place(x =170 , y =100 )
        
        usen1 = Label(ob, text = "GENDER",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen1.place(x = 10, y = 130)
        MSE3 =ttk.Radiobutton(ob, text = "Female", variable= var1, value= "Female")
        MSE3.place(x =170 , y = 130 )
        MSE2 =ttk.Radiobutton(ob, text = "Male", variable= var1, value= "male")
        MSE2.place(x =260 , y =130 )
        usen2 = Label(ob, text = "DATE OF BIRTH",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen2.place(x = 10, y = 160)
        MSE4 = Entry(ob,width= "30",textvariable= mdob)
        MSE4.place(x =170 , y =160 )
        usen3 = Label(ob, text = "PER. ADDRESS",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen3.place(x = 10, y = 190)
        MSE5 = Entry(ob,width= "30",textvariable= mperaddress)
        MSE5.place(x =170 , y =190 )
        usen4 = Label(ob, text = "PRESENT ADDRESS",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen4.place(x = 10, y = 220)
        MSE6 = Entry(ob,width= "30",textvariable= mpresaddress)
        MSE6.place(x =170 , y =220 )
        usen5 = Label(ob, text = "JOB PROFILE",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen5.place(x = 10, y = 250)
        MSE7 = Entry(ob,width= "30",textvariable= mjobprofile)
        MSE7.place(x =170 , y =250, )
        usen6 = Label(ob, text = "ANY DOSH",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen6.place(x = 10, y = 280)
        MSE8 = ttk.Combobox(ob,values= ("MANGLIK","KAALSARPDOSH","PREFER NOT TO SAY"),textvariable = manydosh )
        MSE8.set("DOSH IF ANY")
        MSE8.place(x =170 , y =280 )
        usen7 = Label(ob, text = "MOBILE NUMBER",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen7.place(x = 10, y = 310)
        MSE9 = Entry(ob,width= "30",textvariable= mmobilenumber)
        MSE9.place(x =170 , y =310 )
        usen7 = Label(ob, text = "MARITAL STATUS",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen7.place(x = 10, y = 340)
        MSE10 = ttk.Combobox(ob, values = ("DIVORCEE","WAITING FOR DIVORCE","SINGLE","WIDOW","PREFER NOT TO SAY"),textvariable= msmaritalstatus)
        MSE10.set("PLEASE SELECT YOUR CHOICE")
        MSE10.place(x =170 , y =340 )
        usen8 = Label(ob, text = "TIME OF BIRTH",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen8.place(x = 10, y = 370)
        MSE11 = Entry(ob,width= "30",textvariable= mstimeofbirth)
        MSE11.place(x =170 , y =370 )
        usen9 = Label(ob, text = "MARRIAGE PREFERENCE",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen9.place(x = 10, y = 400)
        MSE12 = ttk.Combobox(ob, values = ("OWN CASTE","INTER-CASTE","ANY","PREFER NOT TO SAY"),textvariable= mmarriagechoice)
        MSE12.set("PLEASE SELECT YOUR CHOICE")
        MSE12.place(x =170 , y =400 )
        usen10 = Label(ob, text = "SEARCHING FOR ",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen10.place(x = 10, y = 430)
        MSE13 = ttk.Combobox(ob,values= ("MYSELF","MY BROTHER", "MY SISTER", "MY SON", "MY DAUGHTER", "SOMEONE ELSE", "MY RELATEVE", "PREFER NOT TO SAY"),width= "30",textvariable= mssearchingfor)
        MSE13.place(x =170 , y =430, )
        usen11 = Label(ob, text = "EMAIL ID",bg ="bisque3",fg = "maroon", width = "15", height = "1",font = ("garamond","10","bold"))
        usen11.place(x = 10, y = 460)
        MSE14 = Entry(ob,width= "30",textvariable= memailid)
        MSE14.place(x =170 , y = 460 )
        k1 = Button(ob, text = "ENTER DATA",bg ="black",fg = "yellow", width = "15", height = "1",font = ("garamond","10","bold"), command= insertmatrouser )
        k1.place(x = 10,y=670)
        pk = Button(ob, text = "PASS",bg ="black",fg = "yellow", width = "15", height = "1",font = ("garamond","10","bold"), command= pas ).place(x = 160,y=670)
        pk = Button(ob, text = "MARRIAGE CARD",bg ="black",fg = "yellow", width = "15", height = "1",font = ("garamond","10","bold"), command= marriagecard ).place(x = 310,y=670)
        k3 = Button(ob, text = "CLEAR",bg ="black",fg = "yellow", width = "15", height = "1",font = ("garamond","10","bold"), command= clear )
        k3.place(x = 460,y=670)
        global MSDIVINETRVI
        MSDIVINETRVI = ttk.Treeview(ob) 
        MSDIVINETRVI["column"]=("SNO","NAMEOFMATCH","GENDER","DATEOFBIRTH","PERMANANTADDRESS","PRESENTADDRESS","JOBPROFILE","ANYDOSH","MOBILENUMBER","MARITALSTATUS","TIMEOFBIRTH","MARRIAGEPREFERENCE","SEARCHINGFOR","EMAILID")	
        MSDIVINETRVI.column("#0",width= 80)
        MSDIVINETRVI.column("SNO",width= 80)
        MSDIVINETRVI.column("NAMEOFMATCH",width= 80)
        MSDIVINETRVI.column("GENDER",width= 80)
        MSDIVINETRVI.column("DATEOFBIRTH",width= 80)
        MSDIVINETRVI.column("PERMANANTADDRESS",width= 100)
        MSDIVINETRVI.column("PRESENTADDRESS",width= 100)
        MSDIVINETRVI.column("JOBPROFILE",width= 80)
        MSDIVINETRVI.column("ANYDOSH",width= 80)
        MSDIVINETRVI.column("MOBILENUMBER",width= 80)
        MSDIVINETRVI.column("MARITALSTATUS",width= 80)
        MSDIVINETRVI.column("TIMEOFBIRTH",width= 80)
        MSDIVINETRVI.column("MARRIAGEPREFERENCE",width= 100)
        MSDIVINETRVI.column("SEARCHINGFOR",width= 80)
        MSDIVINETRVI.column("EMAILID",width= 80)
    
        MSDIVINETRVI["show"] = ("headings")
        MSDIVINETRVI.heading("#0",text = "",anchor= CENTER)
        MSDIVINETRVI.heading("SNO",text = "S NO",anchor= CENTER)
        MSDIVINETRVI.heading("NAMEOFMATCH",text = "NAME OF MATCH",anchor= CENTER)
        MSDIVINETRVI.heading("GENDER",text = "GENDER",anchor= CENTER)
        MSDIVINETRVI.heading("DATEOFBIRTH",text = "DATE OF BIRTH",anchor= CENTER)
        MSDIVINETRVI.heading("PERMANANTADDRESS",text = "PERMANANT ADDRESS",anchor= CENTER)
        MSDIVINETRVI.heading("PRESENTADDRESS",text = "PRESENT ADDRESS",anchor= CENTER)
        MSDIVINETRVI.heading("JOBPROFILE",text = "JOB PROFILE",anchor= CENTER)
        MSDIVINETRVI.heading("ANYDOSH",text = "ANY DOSH",anchor= CENTER)
        MSDIVINETRVI.heading("MOBILENUMBER",text = "MOBILE NUMBER",anchor= CENTER)
        MSDIVINETRVI.heading("MARITALSTATUS",text = "MARITAL STATUS",anchor= CENTER)
        MSDIVINETRVI.heading("TIMEOFBIRTH",text = "TIME OF BIRTH",anchor= CENTER)
        MSDIVINETRVI.heading("MARRIAGEPREFERENCE",text = "MARRIAGE PREFERENCE",anchor= CENTER)
        MSDIVINETRVI.heading("SEARCHINGFOR",text = " SEARCHING FOR  ",anchor= CENTER)
        MSDIVINETRVI.heading("EMAILID",text = "EMAIL ID",anchor= CENTER)
        MSDIVINETRVI.grid(row = 0,column= 0, padx= 10,pady= 700)
        k2 = Button(ob, text = "SHOW DATA",bg ="black",fg = "yellow", width = "15", height = "1",font = ("garamond","10","bold"), command= showmatrouser )
        k2.place(x = 610,y=670)
        lfshowdata0 = Label(ob,)
        lfshowdata0.place(x= 500, y= 50)
        lfshowdata1 = Label(ob,)
        lfshowdata1.place(x= 500, y= 50)
        lfshowdata2 = Label(ob,)
        lfshowdata2.place(x= 500, y= 50)
        lfshowdata3 = Label(ob,)
        lfshowdata3.place(x= 500, y= 50)
        lfshowdata4 = Label(ob,)
        lfshowdata4.place(x= 500, y= 50)
        lfshowdata5 = Label(ob,)
        lfshowdata5.place(x= 500, y= 50)
        lfshowdata6 = Label(ob,)
        lfshowdata6.place(x= 500, y= 50)
        lfshowdata7 = Label(ob,)
        lfshowdata7.place(x= 500, y= 50)
        lfshowdata8 = Label(ob,)
        lfshowdata8.place(x= 500, y= 50)
        lfshowdata9 = Label(ob,)
        lfshowdata9.place(x= 500, y= 50)
        lfshowdata10 = Label(ob,)
        lfshowdata10.place(x= 500, y= 50)
        lfshowdata11 = Label(ob,)
        lfshowdata11.place(x= 500, y= 50)
        lfshowdata12 = Label(ob,)
        lfshowdata12.place(x= 500, y= 50)
        lfshowdata13 = Label(ob,)
        lfshowdata13.place(x= 500, y= 50)
        lfshowdata14 = Label(ob,)
        lfshowdata14.place(x= 500, y= 50)
        
        lfshowdata0A = Label(ob,)
        lfshowdata0A.place(x= 500, y= 50)
        lfshowdata1A = Label(ob,)
        lfshowdata1A.place(x= 500, y= 50)
        lfshowdata2A = Label(ob,)
        lfshowdata2A.place(x= 500, y= 50)
        lfshowdata3A = Label(ob,)
        lfshowdata3A.place(x= 500, y= 50)
        lfshowdata4A = Label(ob,)
        lfshowdata4A.place(x= 500, y= 50)
        lfshowdata5A = Label(ob,)
        lfshowdata5A.place(x= 500, y= 50)
        lfshowdata6A = Label(ob,)
        lfshowdata6A.place(x= 500, y= 50)
        lfshowdata7A = Label(ob,)
        lfshowdata7A.place(x= 500, y= 50)
        lfshowdata8A = Label(ob,)
        lfshowdata8A.place(x= 500, y= 50)
        lfshowdata9A = Label(ob,)
        lfshowdata9A.place(x= 500, y= 50)
        lfshowdata10A = Label(ob,)
        lfshowdata10A.place(x= 500, y= 50)
        lfshowdata11A = Label(ob,)
        lfshowdata11A.place(x= 500, y= 50)
        lfshowdata12A = Label(ob,)
        lfshowdata12A.place(x= 500, y= 50)
        lfshowdata13A = Label(ob,)
        lfshowdata13A.place(x= 500, y= 50)
        lfshowdata14A = Label(ob,)
        lfshowdata14A.place(x= 500, y= 50)
        
        ob.mainloop()
    else:
        messagebox.showinfo(title="",message="WRONG PASSORD \nOR USER NAME")
def details():
    db = Tk()
    db.configure(background= "bisque2")
    
    
        
    
    db.mainloop()
    
def insertmatrouser():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "DIVINEBANDHAN"
        )
    mycursor = mydb.cursor()
    SQL =  ("INSERT INTO DIVINEBANDHANDA(SNO,NAMEOFMATCH,GENDER,DATEOFBIRTH,PERMANANTADDRESS,PRESENTADDRESS,JOBPROFILE,ANYDOSH,MOBILENUMBER,MARITALSTATUS,TIMEOFBIRTH,MARRIAGEPREFERENCE,SEARCHINGFOR,EMAILID)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    values = (MSE01.get(),
              MSE1.get(),
              var1.get(),
              MSE4.get(),
              MSE5.get(),
              MSE6.get(),
              MSE7.get(),
              MSE8.get(),
              MSE9.get(),
              MSE10.get(),
              MSE11.get(),
              MSE12.get(),
              MSE13.get(),
              MSE14.get()
              )
    mycursor.execute(SQL,values)
    mydb.commit()
   
    
def showmatrouser():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "DIVINEBANDHAN"
        )
    mycursor = mydb.cursor()
    SQL =  ("SELECT*FROM DIVINEBANDHANDA")
    mycursor.execute(SQL)
    MSDIVINETRVI.insert("",END,values = (MSE01.get(),MSE1.get(),var1.get(),MSE4.get(),MSE5.get(),MSE6.get(),MSE7.get(),MSE8.get(),MSE9.get(),MSE10.get(),MSE11.get(),MSE12.get(),MSE13.get(),MSE14.get()))
    lfshowdata0.config(text= "YOUR MATCH DETAILS",width= "61",height= "1", bg = "BLACK",fg = "RED",font = ("schadow bt",10,"bold"))
    lfshowdata0.place(x= 499, y= 70)
    lfshowdata1.config(text= "S.NO",anchor= W,width= "30",height= "1")
    lfshowdata1.place(x= 500, y= 90)
    lfshowdata1A.config(text= MSE01.get(),anchor= W,width= "48",height= "1")
    lfshowdata1A.place(x= 650, y= 90)
    
    
    
    lfshowdata2.config(text= "NAME OF MATCH",anchor= W,width= "30",height= "1")
    lfshowdata2.place(x= 500, y= 110)
    lfshowdata2A.config(text= MSE1.get(),anchor= W,width= "48",height= "1")
    lfshowdata2A.place(x= 650, y= 110)
   
    
    lfshowdata3.config(text= "GENDER",anchor= W,width= "30",height= "1")
    lfshowdata3.place(x= 500, y= 130)
    lfshowdata3A.config(text= var1.get(),anchor= W,width= "48",height= "1")
    lfshowdata3A.place(x= 650, y= 130)
    
    lfshowdata4.config(text= "DATE OF BIRTH",anchor= W,width= "30",height= "1")
    lfshowdata4.place(x= 500, y= 150)
    lfshowdata4A.config(text= MSE4.get(),anchor= W,width= "48",height= "1")
    lfshowdata4A.place(x= 650, y= 150)
    
    lfshowdata5.config(text= "PERMANANT ADDRESS",anchor= W,width= "30",height= "1")
    lfshowdata5.place(x= 500, y= 170)
    lfshowdata5A.config(text= MSE5.get(),anchor= W,width= "48",height= "1")
    lfshowdata5A.place(x= 650, y= 170)
    
    lfshowdata6.config(text= "PRESENT ADDRESS",anchor= W,width= "30",height= "1")
    lfshowdata6.place(x= 500, y= 190)
    lfshowdata6A.config(text= MSE6.get(),anchor= W,width= "48",height= "1")
    lfshowdata6A.place(x= 650, y= 190)
    
    lfshowdata7.config(text= "PRESENT ADDRESS",anchor= W,width= "30",height= "1")
    lfshowdata7.place(x= 500, y= 190)
    lfshowdata7A.config(text= MSE6.get(),anchor= W,width= "48",height= "1")
    lfshowdata7A.place(x= 650, y= 190)
    
    lfshowdata7.config(text= "JOB PROFILE",anchor= W,width= "30",height= "1")
    lfshowdata7.place(x= 500, y= 210)
    lfshowdata7A.config(text= MSE7.get(),anchor= W,width= "48",height= "1")
    lfshowdata7A.place(x= 650, y= 210)
    
    lfshowdata8.config(text= "ANY DOSH",anchor= W,width= "30",height= "1")
    lfshowdata8.place(x= 500, y= 230)
    lfshowdata8A.config(text= MSE8.get(),anchor= W,width= "48",height= "1")
    lfshowdata8A.place(x= 650, y= 230)
    
    lfshowdata9.config(text= "MOBILE NUMBER",anchor= W,width= "30",height= "1")
    lfshowdata9.place(x= 500, y= 250)
    lfshowdata9A.config(text= MSE9.get(),anchor= W,width= "48",height= "1")
    lfshowdata9A.place(x= 650, y= 250)
    
    lfshowdata10.config(text= "MARITAL STATUS",anchor= W,width= "30",height= "1")
    lfshowdata10.place(x= 500, y= 270)
    lfshowdata10A.config(text= MSE10.get(),anchor= W,width= "48",height= "1")
    lfshowdata10A.place(x= 650, y= 270)
    
    lfshowdata11.config(text= "TIME OF BIRTH",anchor= W,width= "30",height= "1")
    lfshowdata11.place(x= 500, y= 290)
    lfshowdata11A.config(text= MSE11.get(),anchor= W,width= "48",height= "1")
    lfshowdata11A.place(x= 650, y= 290)
    
    lfshowdata12.config(text= "MARRIAGE PREFERENCE",anchor= W,width= "30",height= "1")
    lfshowdata12.place(x= 500, y= 310)
    lfshowdata12A.config(text= MSE12.get(),anchor= W,width= "48",height= "1")
    lfshowdata12A.place(x= 650, y= 310)
    
    lfshowdata13.config(text= "SEARCHING FOR",anchor= W,width= "30",height= "1")
    lfshowdata13.place(x= 500, y= 330)
    lfshowdata13A.config(text= MSE13.get(),anchor= W,width= "48",height= "1")
    lfshowdata13A.place(x= 650, y= 330)
    
    lfshowdata14.config(text= "EMAIL ID",anchor= W,width= "30",height= "1")
    lfshowdata14.place(x= 500, y= 350)
    lfshowdata14A.config(text= MSE14.get(),anchor= W,width= "48",height= "1")
    lfshowdata14A.place(x= 650, y= 350)
    
    lfshowdata0A.config(text= "PLEASE TAKE A SCREENSHOT OF THESE DETAIL\n FOR YOUR ACKNOWLAGEMENT",width= "61",height= "2", bg = "maroon",fg = "white",font = ("schadow bt",10,"bold"))
    lfshowdata0A.place(x= 499, y= 370)
    
    
   
def clear():
    MSE01.delete(0,END)
    MSE1.delete(0,END)
    var1.set("")
    MSE4.delete(0,END)
    MSE5.delete(0,END)
    MSE6.delete(0,END)
    MSE7.delete(0,END)
    MSE7.delete(0,END)
    MSE7.delete(0,END)
    MSE8.delete(0,END)
    MSE9.delete(0,END)
    MSE10.delete(0,END)
    MSE11.delete(0,END)
    MSE12.delete(0,END)
    MSE13.delete(0,END)
    MSE14.delete(0,END)
    
    
    
    print("all items are deleted")


    
   
  
    print ("wow we have done it")






ldb = Label(ob, anchor = NW, bg ="bisque3", fg = "Black", width = "200", height = "80").place(x = 0, y = 1)
ldbt = Label(ob, text = "\nNow It become easy for us to find matches for yourself if you are teenager and above.Parents do not have to \nworry about their kids from now onwards.\n Be it a relatives, be it a loved one, now everyone can find matches for \ntheir relatives and  loved ones\n so it does not matter where do you live, where do you belong globally.\nDivine Bandhan is the best option to choose the better match for you.", anchor = NW, bg ="bisque3", fg = "black", width = "120", height = "50", font=( "Times new roman", 12, "bold")).place(x = 350, y = 150)
logdb = Label(ob,text = "LOGIN", bg ="BLACK", fg= "white", width = "10", height = "1").place(x = 600, y = 350)
logdb = Label(ob,text = "PASSWORD", bg ="BLACK",fg= "white", width = " 10", height = "1").place(x = 600, y = 380)
blog = Button(ob,text = " L   O   G   I   N  ", bg ="red",fg = "white", width = "23", height = "1",font = ("garamond","10","bold"), command = loginuserpage).place(x = 600, y = 420)
usdb = Entry(ob,width= "20")
usdb.place(x = 690, y = 350)
pasdb = Entry(ob,show= "•",width= "20")
pasdb.place(x = 690, y = 380)
ldbT1 = Label(ob, text = "\nDivinebandhan provides you the service of selection of matches from different parts of countries and offcourse within your communities, \nso time to time we provide swayamwar service also for our subscribers so that they should get their \nmatches according to their choice, We also provide marriage card service for our service who get bond after \nchoice of each other in swayamwar", anchor = NW, bg ="bisque3", fg = "MAROON", width = "120", height = "50", font=( "Times new roman", 12, "bold")).place(x = 350, y = 600)
usen_0 = Label(ob, text = "DO YOU \n WANT \nTO GET \n MARRIED? \n\nJUST \nENTER \nDETAILS\n AND PRESS \nBUTTON\n AWAY", bg ="bisque3",anchor= NE,fg = "black", width = "10", height = "15",font = ("garamond","40","bold")).place(x = 1, y = 150)
ldb = Label(ob, text= "Divine Bandhan", bg ="red",fg = "white", anchor= CENTER, width = "85", height = "2",font = ("TIMES NEW ROMAN","20","italic","bold")).place(x = 0, y = 1)
LABT = Label(ob,text = " Software Engineered by : Rajinder\n\nThis project is Devloped for Academic Purpose  ",anchor= N,bg = "WHITE", fg = "maroon", width = "145", height = "4",font = ("Schadow BT",12,"bold"))
LABT.place(x = 0, y = 880)
ob.mainloop()