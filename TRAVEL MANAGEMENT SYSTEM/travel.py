from tkinter import *  # Import everything from the tkinter module for easy access to its classes and functions
from tkinter import ttk  # Import the themed tkinter module for additional widgets
import random  # Import the random module for generating random numbers or choices
import tkinter as tk  # Import the tkinter module with an alias "tk" for convenience
import time  # Import the time module for various time-related functions
import tkinter.messagebox  # Import the messagebox module from tkinter for displaying message boxes
from tkinter import Tk  # Import the Tk class from tkinter to create the main window
from datetime import datetime  # Import the datetime class from the datetime module for working with dates and times
import os  # Import the os module for interacting with the operating system (e.g., file operations)



class Travel:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Travel Management Systems" )
        self.root.geometry("1920x1080")
        self.root.configure(background = 'white')
        
        self.cboDestination = {'value': ()}  
        self.txtExtLuggage = Text(root)
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d-%m-%y"))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        
        
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = StringVar()
        var12 = StringVar()
        var13 = StringVar()
        
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Telephone = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        
        
        AirportTax = StringVar()
        Mile = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        
        Standard = StringVar()
        Economy = StringVar()
        FirstClass = StringVar()
        
        
        AirportTax.set("0")
        Mile.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")
        
        Standard.set("0")
        Economy.set("0")
        FirstClass.set("0")
#================================================Defined Function========================================================================
      
        
        def iLogout():
            confirm_exit = tkinter.messagebox.askyesno("Travel Management System", "Confirm if you want to Logout")
            if confirm_exit:
                self.root.destroy()  # Destroy the main application window
                from registration import LoginPage
                 #Create an instance of the LoginPage and open it
                root = tkinter.Tk()
                login_page = LoginPage(root)
                root.mainloop()

                        

                        
        def Reset():
            AirportTax.set("0")
            Mile.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Mobile.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtRecepipt= Text(root)         

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set("0")
            var12.set("0")
            var13.set("0")

            self.cboDeparture.current(0)
            self.cboDestination.current(0)
            self.cboAccommodation.current(0)

            self.txtAirportTax.configure(state = DISABLED)
            self.txtMile.configure(state = DISABLED)
            self.txtTravelling_Insurance.configure(state = DISABLED)
            self.txtExtLuggage.configure(state = DISABLED)

            self.txtStandard.configure(state = DISABLED)
            self.txtEconomy.configure(state = DISABLED)
            self.txtFirstClass.configure(state = DISABLED)

        def save_to_text():
                try:
                        filename = "D:\\projects\\TRAVEL MANAGEMENT SYSTEM\\travel receipt.txt"


                        with open(filename, "w", encoding="utf-8") as file:
                                file.write("Receipt Ref: " + Receipt_Ref.get() + "\n")
                                file.write("Date Ref: " + DateofOrder.get() + "\n")
                                file.write("Flight: Travelling Details\n")
                                file.write("Firstname: " + Firstname.get() + "\n")
                                file.write("Surname: " + Surname.get() + "\n")
                                file.write("Address: " + Address.get() + "\n")
                                file.write("PostCode: " + PostCode.get() + "\n")
                                file.write("Telephone: " + Telephone.get() + "\n")
                                file.write("Mobile: " + Mobile.get() + "\n")
                                file.write("Email: " + Email.get() + "\n")
                                file.write("Standard: " + var11.get() + "\n")
                                file.write("Economy: " + var12.get() + "\n")
                                file.write("FirstClass: " + var13.get() + "\n")
                                file.write("Standard: " + Standard.get() + "\n")
                                file.write("Economy: " + Economy.get() + "\n")
                                file.write("FirstClass: " + FirstClass.get() + "\n")
                                file.write("Paid: " + PaidTax.get() + "\n")
                                file.write("SubTotal: " + str(SubTotal.get()) + "\n")
                                file.write("TotalCost: " + str(TotalCost.get()))
                                print("Receipt information saved successfully.")
                                
                                print("Current working directory:", os.getcwd())
                                
                                tkinter.messagebox.showinfo("Success", "Receipt information saved successfully.")
                except Exception as e:
                        print("An error occurred while saving the receipt information:", e)
                        
                        tkinter.messagebox.showerror("Error", f"An error occurred while saving the receipt information: {e}")
                pass
                            
        
        def Receipt():
                self.txtReceipt.delete("1.0", END)  
                x = random.randint(10853, 500831)  
                randomRef = str(x)
                Receipt_Ref.set("Travel Bill: " + randomRef)

                # Get current date and time
                current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                self.txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t\t' + Receipt_Ref.get() + "\n") 
                self.txtReceipt.insert(END, 'Date Ref:\t\t\t\t\t' + current_datetime + "\n")  
                self.txtReceipt.insert(END, 'Flight:\t\t\t\t\t' + "Travelling Details \n")  
                self.txtReceipt.insert(END, 'Firstname:\t\t\t\t\t' + Firstname.get() + "\n")  
                self.txtReceipt.insert(END, 'Surname:\t\t\t\t\t' + Surname.get() + "\n")  
                self.txtReceipt.insert(END, 'Address:\t\t\t\t\t' + Address.get() + "\n") 
                self.txtReceipt.insert(END, 'PostCode:\t\t\t\t\t' + PostCode.get() + "\n")  
                self.txtReceipt.insert(END, 'Telephone:\t\t\t\t\t' + Telephone.get() + "\n")  
                self.txtReceipt.insert(END, 'Mobile:\t\t\t\t\t' + Mobile.get() +"\n")  
                self.txtReceipt.insert(END, 'Email:\t\t\t\t\t' + Email.get() + "\n")  
                self.txtReceipt.insert(END, 'Standard:\t\t\t\t\t' + var11.get() + "\n")  
                self.txtReceipt.insert(END, 'Economy:\t\t\t\t\t' + var12.get() + "\n") 
                self.txtReceipt.insert(END, 'FirstClass:\t\t\t\t\t' + var13.get() + "\n")  
                self.txtReceipt.insert(END, 'Standard:\t\t\t\t\t' + Standard.get() + "\n")  
                self.txtReceipt.insert(END, 'Economy:\t\t\t\t\t' + Economy.get() + "\n") 
                self.txtReceipt.insert(END, 'FirstClass:\t\t\t\t\t' + FirstClass.get() + "\n")  
                self.txtReceipt.insert(END, 'Paid:\t\t\t\t\t' + PaidTax.get() + "\n")  
                self.txtReceipt.insert(END, 'SubTotal:\t\t\t\t\t' + str(SubTotal.get()) + "\n") 
                self.txtReceipt.insert(END, 'TotalCost:\t\t\t\t\t' + str(TotalCost.get())) 
         
                
        def Airport_Tax():
            global paid1
            if var1.get() == 1:
                self.txtAirportTax.configure(state=NORMAL)
        # Assuming the airport tax is 45 INR
                Item1 = 45
        # Set the airport tax in Indian Rupees
                AirportTax.set(u"\u20B9" + str(Item1))
                paid1 = AirportTax.get()  
            elif var1.get() == 0:
                self.txtAirportTax.configure(state=DISABLED)
                AirportTax.set(u"\u20B9" + "0")
                
        def Mileage():
            global Item2
            if var2.get() == 1:
                self.txtMile.configure(state=NORMAL)
        # Assuming the mileage value is 23345
                Item2 = 23345
        # Set the mileage value
                Mile.set(str(Item2))  
            elif var2.get() == 0:  # Corrected condition to check var2
                self.txtMile.configure(state=DISABLED)
                Mile.set("0")


        def Travelling():
            global Item3
            if var3.get() == 1:
                self.txtTravelling_Insurance.configure(state=NORMAL)
        # Assuming the travel insurance cost is 63
                Item3 = 63
        # Set the travel insurance cost with the Indian Rupee symbol
                Travel_Ins.set(u"\u20B9" + str(Item3))
            elif var3.get() == 0:
                self.txtTravelling_Insurance.configure(state=DISABLED)
                Travel_Ins.set(u"\u20B9" + "0")  # Set travel insurance cost to 0 when unchecked


        def Lug():
            global Item4
            if var4.get() == 1:
                self.txtLuggage.configure(state=NORMAL)  
        # Assuming the luggage cost is 334.59
                Item4 = 334.59
        # Set the luggage cost with the Indian Rupee symbol
                Luggage.set(u"\u20B9" + str(Item4))
            elif var4.get() == 0:
                self.txtLuggage.configure(state=DISABLED)  
                Luggage.set(u"\u20B9" + "0")  # Set luggage cost to 0 when unchecked

 
        def Standard_Fees():
            global Item5
            if var5.get() == 1:
                self.txtStandard.configure(state=NORMAL)
        # Assuming the standard fees are 274.9
                Item5 = 274.9
        # Set the standard fees with the Indian Rupee symbol
                Standard.set(u"\u20B9" + str(Item5))
            elif var5.get() == 0:
                self.txtStandard.configure(state=DISABLED)
                Standard.set(u"\u20B9" + "0")  # Set standard fees to 0 when unchecked

 
        def Economy_Fees():
            global Item6
            if var7.get() == 1:
                self.txtEconomy.configure(state=NORMAL)
        # Assuming the economy fees are 365.5
                Item6 = 365.5
        # Set the economy fees with the Indian Rupee symbol
                Economy.set(u"\u20B9" + str(Item6))
            elif var7.get() == 0:
                self.txtEconomy.configure(state=DISABLED)
                Economy.set(u"\u20B9" + "0")  # Set economy fees to 0 when unchecked


        def FirstClass_Fees():
            global Item7
            if var9.get() == 1:
                self.txtFirstClass.configure(state=NORMAL)
        # Assuming the first class fees are 564.3
                Item7 = 564.3
        # Set the first class fees with the Indian Rupee symbol
                FirstClass.set(u"\u20B9" + str(Item7))
            elif var9.get() == 0:
                self.txtFirstClass.configure(state=DISABLED)
                FirstClass.set(u"\u20B9" + "0")  
        


    
        def Total_Paid():
                total_sum = 0

    # Calculate total sum by adding all cost components
                total_sum += float(AirportTax.get()[1:]) if var1.get() == 1 else 0
                total_sum += float(Mile.get()) if var2.get() == 1 else 0
                total_sum += float(Travel_Ins.get()[1:]) if var3.get() == 1 else 0
                total_sum += float(Luggage.get()[1:]) if var4.get() == 1 else 0
                total_sum += float(Standard.get()[1:]) if var5.get() == 1 else 0
                total_sum += float(Economy.get()[1:]) if var7.get() == 1 else 0
                total_sum += float(FirstClass.get()[1:]) if var9.get() == 1 else 0

    # Check additional conditions for specific cases
                special_case = False
                if var11.get() == "Heathrow" and var12.get() == "Paris" and var13.get() == "L":
                        special_case = True
                        total_sum += 274.90  
                elif var11.get() == "Assam" and var12.get() == "Assam" and var13.get() == "L":
                        special_case = True
                        total_sum += 365.90  

    # Calculate tax
                tax_rate = 0.09
                tax = total_sum * tax_rate

    # Calculate total cost
                total_cost = total_sum + tax

    # Set the calculated values to the corresponding StringVars
                PaidTax.set(u"\u20B9" + str('%.2f' % tax))
                SubTotal.set(u"\u20B9" + str('%.2f' % total_sum))
                TotalCost.set(u"\u20B9" + str('%.2f' % total_cost))




             
#========================================================================================================================
        MainFrame = Frame(self.root)
        MainFrame.pack(expand=True, fill='both')  

        Tops = Frame(MainFrame, bd=20, relief=RIDGE)
        Tops.pack(side=TOP, fill='both', expand=True)  

        self.lblTitle = Label(Tops, font=('arial', 70, 'bold'), text="  Travel  Management  System  ", bg='black', fg='white')
        self.lblTitle.pack(expand=True, fill='both')
  
#=========================================================================================================================
        CustomerDetailsFrame = LabelFrame(MainFrame, width=700, height=300, bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)

        FrameDetails = Frame(CustomerDetailsFrame, bd=20, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill='both', expand=True)  

        CustomerName = LabelFrame(FrameDetails, width=200, height=250, bd=20,
                          font=('arial', 16, 'bold'), text="Customer Name", relief=RIDGE) 
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(FrameDetails, bd=20, width=300, height=250,
                         font=('arial', 16, 'bold'), text="Travel Details", relief=RIDGE)
        TravelFrame.grid(row=0, column=1)

        Ticket_Frame = LabelFrame(FrameDetails, width=300, height=250, relief=RIDGE)
        Ticket_Frame.grid(row=1, column=0)

        CostFrame = LabelFrame(FrameDetails, width=200, height=250, relief=RIDGE)
        CostFrame.grid(row=1, column=1)

#==========================================================================================================================
        Receipt_ButtonFrame = Frame(CustomerDetailsFrame, bd=10, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT, fill='y')  

        ReceiptFrame = LabelFrame(Receipt_ButtonFrame, width=350, height=300,
                          font=('arial', 20, 'bold'), text="Receipt", relief=RIDGE)
        ReceiptFrame.pack(fill='both', expand=True)  

        ButtonFrame = LabelFrame(Receipt_ButtonFrame, width=350, height=100, relief=RIDGE)
        ButtonFrame.pack(fill='x')  

        
#=============================================CustomerName====================================================================
        self.lblFirstname = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "FirstName" , bd = 7)
        self.lblFirstname.grid(row = 0 , column = 0 , sticky = W)
        
        self.txtFirstname = Entry(CustomerName , font=('arial' , 14 , 'bold')  ,text="FirstName" , textvariable = Firstname
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtFirstname.grid(row = 0 , column = 1)
        
        self.lblSurname = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "SurName" , bd = 7)
        self.lblSurname.grid(row = 1 , column = 0 , sticky = W)
        
        self.txtSurname = Entry(CustomerName , font=('arial' , 14 , 'bold')  , text="SurName",textvariable = Surname
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtSurname.grid(row = 1 , column = 1)
        
        self.lblAddress = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Address" , bd = 7)
        self.lblAddress.grid(row = 2 , column = 0 , sticky = W)
        
        self.txtAddress = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Address
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtAddress.grid(row = 2 , column = 1)
        
        self.lblPostCode = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "PostCode" , bd = 7)
        self.lblPostCode.grid(row = 3 , column = 0 , sticky = W)
        
        self.txtPostCode = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = PostCode
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtPostCode.grid(row = 3 , column = 1)
        
        self.lblTelephone = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Telephone" , bd = 7)
        self.lblTelephone.grid(row = 4 , column = 0 , sticky = W)
        
        self.txtTelephone = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Telephone
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtTelephone.grid(row = 4 , column = 1)
        
        self.lblMobile = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Mobile" , bd = 7)
        self.lblMobile.grid(row = 5 , column = 0 , sticky = W)
        
        self.txtMobile = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Mobile
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtMobile.grid(row = 5 , column = 1)
        
        self.lblEmail = Label(CustomerName , font=('arial' , 14 , 'bold') , text = "Email" , bd = 7)
        self.lblEmail.grid(row = 6 , column = 0 , sticky = W)
        
        self.txtEmail = Entry(CustomerName , font=('arial' , 14 , 'bold')  , textvariable = Email
                                  , bd = 7 , insertwidth = 2 , justify = RIGHT)
        self.txtEmail.grid(row = 6 , column = 1)
#=============================================Flight Information==============================================================
        
        self.lblDeparture = Label(TravelFrame, font=('arial', 14, 'bold'), text="Departure", bd=7)
        self.lblDeparture.grid(row=0, column=0, sticky='w')

        self.cboDeparture = ttk.Combobox(TravelFrame, textvariable=var11, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboDeparture['value'] = ('', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Lakshadweep', 'Ladakh', 'Puducherry', 'Jammu and Kashmir')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row=0, column=1)

        self.lblDestination = Label(TravelFrame, font=('arial', 14, 'bold'), text="Destination", bd=7)
        self.lblDestination.grid(row=1, column=0, sticky='w')

        self.cboDestination = ttk.Combobox(TravelFrame, textvariable=var12, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboDestination['value'] = ('', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Lakshadweep', 'Ladakh', 'Puducherry', 'Jammu and Kashmir')
        self.cboDestination.current(0)
        self.cboDestination.grid(row=1, column=1)

        self.lblAccommodation = Label(TravelFrame, font=('arial', 14, 'bold'), text="Accommodation", bd=7)
        self.lblAccommodation.grid(row=2, column=0, sticky='w')

        self.cboAccommodation = ttk.Combobox(TravelFrame, textvariable=var13, state='readonly', font=('arial', 20, 'bold'), width=14)
        self.cboAccommodation['value'] = ('', '1', '2', '3', '4')
        self.cboAccommodation.current(1)
        self.cboAccommodation.grid(row=2, column=1)
#===========================================================================================================================        
        self.chkAirportTax = Checkbutton(TravelFrame , text = "Airport Tax" , variable = var1 , onvalue = 1 , offvalue = 0 ,
                                    font=('arial' , 16 , 'bold'),command=Airport_Tax).grid(row = 3 , column = 0 , sticky = W)

        
        self.txtAirportTax = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = AirportTax
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtAirportTax.grid(row = 3 , column = 1)
        
        self.chkMile = Checkbutton(TravelFrame , text = 'Air Mile' , variable = var2 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'),command=Mileage).grid(row = 4 , column = 0 , sticky = W)
        
        self.txtMile = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Mile
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtMile.grid(row = 4 , column = 1)
        
        self.txtTravelling_Insurance = Checkbutton(TravelFrame , text = 'Travelling Insurance' , variable = var3 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'),command=Travelling).grid(row = 5 , column = 0 , sticky = W)
        
        self.txtTravelling_Insurance = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Travel_Ins
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtTravelling_Insurance.grid(row = 5 , column = 1)
        
        self.chkLuggage = Checkbutton(TravelFrame , text = 'Ext.Luggage' , variable = var4, onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'),command=Lug).grid(row = 6 , column = 0 , sticky = W)
        
        self.txtLuggage = Entry(TravelFrame , font=('arial' , 14 , 'bold')  , textvariable = Luggage
                                  , bd = 7 , insertwidth = 2 , state = DISABLED , justify = RIGHT)
        self.txtLuggage.grid(row = 6 , column = 1)
#=============================================Payment Information==============================================================
        self.lblPaidTax = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "PaidTax\t\t" , bd = 7)
        self.lblPaidTax.grid(row = 0 , column = 2 , sticky = W)
        
        self.txtPaidTax = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = PaidTax
                                  , bd = 7 , width = 27 , justify = RIGHT)
        self.txtPaidTax.grid(row = 0 , column = 3)
        
        self.lblSubTotal = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "SubTotal" , bd = 7)
        self.lblSubTotal.grid(row = 1 , column = 2 , sticky = W)
        
        self.txtSubTotal = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = SubTotal
                                  , bd = 7 , width = 27 , justify = RIGHT)
        self.txtSubTotal.grid(row = 1 , column = 3)
        
        self.lblTotalCost = Label(CostFrame , font=('arial' , 14 , 'bold') , text = "TotalCost" , bd = 7)
        self.lblTotalCost.grid(row = 2 , column = 2 , sticky = W)
        
        self.txtTotalCost = Entry(CostFrame , font=('arial' , 14 , 'bold')  , textvariable = TotalCost
                                  , bd = 7 , width = 27 , justify = RIGHT)
        self.txtTotalCost.grid(row = 2 , column = 3)
#===============================================================================================================================

        self.chkStandard = Checkbutton(Ticket_Frame , text = 'Standard' , variable = var5 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=Standard_Fees).grid(row = 0 , column = 0 , sticky = W)
        
        self.txtStandard = Entry(Ticket_Frame , font=('arial' , 14 , 'bold')  , textvariable = Standard
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtStandard.grid(row = 0 , column = 1)
        
        self.chkSingle = Checkbutton(Ticket_Frame, text='Single', variable=var6, onvalue=1, offvalue=0,
                             font=('arial', 16, 'bold'),)
        self.chkSingle.grid(row=0, column=2, sticky=W)

       
        
        
        self.chkEconomy = Checkbutton(Ticket_Frame , text = 'Economy' , variable = var7 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=Economy_Fees).grid(row = 1 , column = 0 , sticky = W)
        
        self.txtEconomy = Entry(Ticket_Frame , font=('arial' , 14 , 'bold')  , textvariable = Economy
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtEconomy.grid(row = 1 , column = 1)
        
        
        self.chkReturn = Checkbutton(Ticket_Frame, text='Return', variable=var8, onvalue=1, offvalue=0,
                             font=('arial', 16, 'bold'))
        self.chkReturn.grid(row=1, column=2, sticky=W)

        

        
        self.chkFirstClass = Checkbutton(Ticket_Frame , text = 'FirstClass' , variable = var9 , onvalue = 1 , offvalue = 0 ,
                                        font=('arial' , 16 , 'bold'), command=FirstClass_Fees).grid(row = 2 , column = 0 , sticky = W)
        
        self.txtFirstClass = Entry(Ticket_Frame , font=('arial' , 14 , 'bold')  , textvariable = FirstClass
                                  , bd = 7 , width = 6 , state = DISABLED , justify = RIGHT)
        self.txtFirstClass.grid(row = 2 , column = 1)
        
        self.chkSpecialNeeds = Checkbutton(Ticket_Frame, text='SpecialNeeds', variable=var10, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'))
        self.chkSpecialNeeds.grid(row=2, column=2, sticky=W)

       

        
#================================================Receipt========================================================================
        self.txtReceipt = Text(ReceiptFrame , width = 60 , height = 21 ,font=('arial' , 12 , 'bold'), wrap='none',bg='lightgray')
        self.txtReceipt.grid(row=0,column=0)
      
#================================================Buttons======================================================================
        self.btnTotal = Button(ButtonFrame, padx=25, bd=7, font=('arial', 16, 'bold'), width=3, text='Total', command=Total_Paid, bg='black', fg='white')
        self.btnTotal.grid(row=0, column=0)

        self.btnReceipt = Button(ButtonFrame, padx=24, bd=7, font=('arial', 16, 'bold'), width=3, text='Receipt', command=Receipt, bg='black', fg='white')
        self.btnReceipt.grid(row=0, column=1)

        self.btnReset = Button(ButtonFrame, padx=24, bd=7, font=('arial', 16, 'bold'), width=3, text='Reset', command=Reset, bg='black', fg='white')
        self.btnReset.grid(row=0, column=2)

        self.btnExit = Button(ButtonFrame, padx=24, bd=7, font=('arial', 16, 'bold'), width=3, text='Logout', command=iLogout, bg='black', fg='white')
        self.btnExit.grid(row=0, column=4)

        self.btnSave = Button(ButtonFrame, padx=25, bd=7, font=('arial', 16, 'bold'), width=3, text='Save', command=save_to_text, bg='black', fg='white')
        self.btnSave.grid(row=0, column=3)

if __name__ == "__main__":
    root = Tk()
    application = Travel(root)
    root.mainloop()
   

    