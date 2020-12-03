from tkinter import*
import tkinter.messagebox
from tkinter import ttk

class MyGui:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Volvo")
        self.main_window.geometry("500x460")
        
        self.frame = LabelFrame(self.main_window, text = "Build & Price", width = 500, height = 460, font=("Arial",12), bg = "light blue")
        self.frame.place(x=0,y=0)
        
        ##############################################
        
        #Models
        self.modellabel = Label(self.frame, text = "Models:", font=("Arial",12, "bold italic"), bg = "light blue")
        self.modellabel.place(x=20,y=10)
        
        self.modvar = StringVar()
        
        self.combo1 = ttk.Combobox(self.frame, width = 12, font=("arial",16), textvariable = self.modvar)
        self.combo1.place(x=20,y=30)
        self.combo1['values'] = ("XC90   --   $61,250", "XC60   --   $46,350", "XC40   --   $39,750", "S90   --   $59,950", "S60   --   $42,400", "V90   --   $62,500")
        
        ############################################
        
        #Colour
        self.colorlabel = Label(self.frame, text = "Colours:", font=("Arial",12, "bold italic"), bg = "light blue")
        self.colorlabel.place(x=20,y=70)

        self.colvar = StringVar()
        
        self.combo2 = ttk.Combobox(self.frame, width = 16, font=("arial",16), textvariable = self.colvar)
        self.combo2.place(x=20,y=90)
        self.combo2['values'] = ("White", "Shadow Black   --   $900", "Smoke   --   $900", "Lightning Blue   --   $900", "Race Red   --   $900", "Moondust Silver   --   $900")
        
        ##############################################
        #Buttons
        self.cal = Button(self.frame, text = "Calculate", font=("arial",10, "bold"), command = self.calculate)
        self.cal.place(x=160,y=400)
        
        self.qui = Button(self.frame, text = "Quit", font=("arial",10, "bold"), command = self.main_window.destroy)
        self.qui.place(x=260,y=400)
        ################################################
        #CheckButtons
        self.ch1 = IntVar()
        self.ch2 = IntVar()
        self.ch3 = IntVar()
        self.ch4 = IntVar()
        
        self.cho1 = Checkbutton(self.frame, text = "Leather Seats          -- $1,950", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.ch1)
        self.cho1.place(x=10,y=140)
        
        self.cho2 = Checkbutton(self.frame, text = "360 View Camera   -- $300", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.ch2)
        self.cho2.place(x=10,y=160)
        
        self.cho3 = Checkbutton(self.frame, text = "Panoramic Sunroof -- $250", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.ch3)
        self.cho3.place(x=10,y=180)
        
        self.cho4 = Checkbutton(self.frame, text = "Load Bars                 -- $400", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.ch4)
        self.cho4.place(x=10,y=200)
        
        ################################################
        #RadioButtons
        self.tranlabel = Label(self.frame, text = "Transmission:", bg = "light blue", font=("Arial",12, "bold italic"))
        self.tranlabel.place(x=265, y=140)
        
        self.radio = IntVar()
        self.radio.set(1)
        
        self.rd1 = Radiobutton(self.frame, text = "Manual", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.radio, value = 1)
        self.rd1.place(x=255,y=165)
        
        self.rd2 = Radiobutton(self.frame, text = "Automatic -- $2,500", highlightbackground = "light blue", font=("arial",12), bg = "light blue", variable = self.radio, value = 2)
        self.rd2.place(x=255,y=185)
        ###############################################
        #logo
        self.canvas = Canvas(width=140,height=120, bg="light blue", highlightbackground = "light blue")
        self.canvas.place(x=290,y=15)
        self.logo = PhotoImage(file = "logo_volvo.png")
        
        self.canvas.create_image(70,70,image=self.logo, anchor = CENTER)
        ###############################################
        #Calculation
        self.sumlabel = Label(self.frame, text = "Summary", font=("arial",14, "bold italic underline"), bg = "light blue", highlightbackground = "light blue")
        self.sumlabel.place(x=20,y=230)
        
        self.total = Label(self.frame, text = "Total Price: ", font=("arial",12, "bold"), bg = "light blue", highlightbackground = "light blue")
        self.total.place(x=200,y=230)
        self.tot = StringVar()
        self.totallabel = Label(self.frame, width = 10, bg = "light blue", textvariable = self.tot)
        self.totallabel.place(x=290,y=230)
        
        self.car = Label(self.frame, text = "Car Price: ", font=("arial",12), bg = "light blue", highlightbackground = "light blue")
        self.car.place(x=20,y=260)
        self.carprice = StringVar()
        self.carpri = Label(self.frame, width = 10, bg = "light blue", textvariable = self.carprice)
        self.carpri.place(x=100,y=260)
        
        self.tax = Label(self.frame, text = "Tax: ", font=("arial",12), bg = "light blue", highlightbackground = "light blue")
        self.tax.place(x=20,y=280)
        self.taxprice = StringVar()
        self.taxpri = Label(self.frame, width = 10, bg = "light blue", textvariable = self.taxprice)
        self.taxpri.place(x=97,y=280)
        
        self.option = Label(self.frame, text = "Options: ", font=("arial",12), bg = "light blue", highlightbackground = "light blue")
        self.option.place(x=20,y=300)
        self.opprice = StringVar()
        self.oppri = Label(self.frame, width = 10, bg = "light blue", textvariable = self.opprice)
        self.oppri.place(x=97,y=300)
        ###############################################
        #dealership
        self.deallabel = Label(self.frame, text = "Find Nearest Dealership: (North Vancouver, Vancouver, Surrey)", font=("arial",12), bg = "light blue", highlightbackground = "light blue")
        self.deallabel.place(x=20,y=330)
        
        self.ent = Entry(self.frame, width = 20, bg = "light blue")
        self.ent.place(x=20,y=360)
        
        self.adbut = Button(self.frame, text = "Address", font=("arial",10), pady = 1, command = self.add)
        self.adbut.place(x=220,y=359)
        ###############################################
        
        mainloop()

    def calculate(self):
        totalprice = 0
        carprice = 0
        tax = 0
        option = 0
        
        #car prices
        if str(self.modvar.get()) == "XC90   --   $61,250":
            carprice += 61250
        if str(self.modvar.get()) == "XC60   --   $46,350":
            carprice += 46350
        if str(self.modvar.get()) == "XC40   --   $39,750":
            carprice += 39750
        if str(self.modvar.get()) == "S90   --   $59,950":
            carprice += 59950
        if str(self.modvar.get()) == "S60   --   $42,400":
            carprice += 42400
        if str(self.modvar.get()) == "V90   --   $62,500":
            carprice += 62500
      
        if str(self.modvar.get()) == "":
            tkinter.messagebox.showerror("Error", "You have to choose a car")
            totalprice = 0
            carprice = 0
            tax = 0
            option = 0

        #Car Colour
        if str(self.colvar.get()) == "White":
            option += 0
        if str(self.colvar.get()) == "Shadow Black   --   $900":
            option += 900
        if str(self.colvar.get()) == "Smoke   --   $900":
            option += 900
        if str(self.colvar.get()) == "Lightning Blue   --   $900":
            option += 900
        if str(self.colvar.get()) == "Race Red   --   $900":
            option += 900
        if str(self.colvar.get()) ==  "Moondust Silver   --   $900":
            option += 900
        
        #CheckButtons
        if (self.ch1.get()) == 1:
            option += 1950
        if (self.ch2.get()) == 1:
            option += 300
        if (self.ch3.get()) == 1:
            option += 250
        if (self.ch4.get()) == 1:
            option += 400

        #Radiobutton
        if (self.radio.get()) == 1:
            option += 0
        if (self.radio.get()) == 2:
            option += 2500
                
        tax = (carprice + option)*0.12
        totalprice = carprice + tax + option
        
        self.carprice.set(format(carprice, "2,.2f"))
        self.taxprice.set(format(tax, "2,.2f"))
        self.opprice.set(format(option, "2,.2f"))
        self.tot.set(format(totalprice, "2,.2f"))
        
    def add(self):
        if str(self.ent.get().lower()) == "north vancouver" or str(self.ent.get().lower()) == "north van":
            tkinter.messagebox.showinfo("Address", "1765 Marine Dr, North Vancouver, BC V7P 1V3")
            
        elif str(self.ent.get().lower()) == "vancouver" or str(self.ent.get().lower()) == "van":
            tkinter.messagebox.showinfo("Address", "8530 Cambie St, Vancouver, BC V6P 6N6")
            
        elif str(self.ent.get().lower()) == "surrey":
            tkinter.messagebox.showinfo("Address", "15393 Guildford Dr, Surrey, BC V3R 0H9")
            
        else:
            tkinter.messagebox.showerror("ERROR", "Wrong Input")


 
        
my_gui = MyGui()
