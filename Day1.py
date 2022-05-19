from tkinter import *
root =Tk()
root.geometry("750x450")

def getvals():
    print("Form Accepteed")

#Heading of the Things
Label(root,text="Registeratiom Form Using Python",font="ar 20 bold").grid(row=0,column=3)

#Field Name  information
name=Label(root,text="Name of Candidate")
phone=Label(root,text="Phone Number of Candidate")
gender=Label(root,text="Select Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

#Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#Values Store Here For Store Data
nameValue=StringVar
phoneValue=StringVar
GenderValue=StringVar
EmergencyValue=StringVar
PaymentMode=StringVar
checkvalue=IntVar

#Forms Field 
nameentryentry=Entry(root,textvariable=nameValue)
phoneentry=Entry(root,textvariable=phoneValue)
genderentry=Entry(root,textvariable=GenderValue)
paymententry=Entry(root,textvariable=PaymentMode)
emergencyentry=Entry(root,textvariable=EmergencyValue)

#Packing Field
nameentryentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#Checkbox Creating

checkbtn=Checkbutton(text="Remember Me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit Button

Button(text="Submit Data",command=getvals).grid(row=8,column=3)

root.mainloop()