#covinfo app
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

dfTN=pd.read_csv("chennai2.csv")
dfM=pd.read_csv("Mumbai2.csv")
dfW=pd.read_csv("Kolkata2.csv")
dfT=pd.read_csv("hyderabad3.csv")
dfH=pd.read_csv("haryana3.csv")



print("WELCOME TO COVINFO APP!")


HEIGHT=500
WIDTH=600

def test_function(entry):
    print("Hey ", entry,"!")
root=tk.Tk()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image=tk.PhotoImage(file="bgimg.png")
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame=tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry=tk.Entry(frame, font=40)
entry.place (relwidth=0.65, relheight=1)
    
button =tk.Button(frame, text="Enter", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame=tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5,rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(lower_frame, text="PLEASE ENTER YOUR NAME", bg='yellow')
label.place(relwidth=1, relheight=1)
root.mainloop()
HEIGHT=500
WIDTH=600

def test_function(entry):
    print("Logged in with ", entry)
root=tk.Tk()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image=tk.PhotoImage(file="bgimg.png")
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame=tk.Frame(root, bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry=tk.Entry(frame, font=40)
entry.place (relwidth=0.65, relheight=1)
    
button =tk.Button(frame, text="Enter", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame=tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5,rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label=tk.Label(lower_frame, text="PLEASE ENTER YOUR PHONE NUMBER", bg='yellow')
label.place(relwidth=1, relheight=1)

root.mainloop()
print()
print()
print()
print("Select the State")
print()
print()
print("Press 1 to select Tamil Nadu")
print("Press 2 to select Maharastra")
print("Press 3 to select West Bengal")
print("Press 4 to select Telangana")
print("Press 5 to select Haryana")
print()     
print()
print()
x=np.arange(10)
numberentry=int(input("Enter the number: "))
if numberentry == 1:
    pop=78000000
    print("Tamil nadu population is:", pop)
    vac=52379870
    print(vac, "have been vaccinated")
    unvac=pop-vac
    col=[vac,unvac]
    Sec=['vaccinated', 'unvaccinated']
    plt.pie(col,autopct='%1.1f%%', labels=Sec)
    plt.show()
    print()
    print()
    if vac>pop/2:
        print("Tamil Nadu is safe")
    print()
    print()
    print()
    
    print(dfTN)
    print()
    print()
    print()
    print("Press 5 to see the months where the Active cases were greater than 1000")    
    print("Press 6 to see the line graph")
    print("Press 7 to see double bar graph")
    print("Press 8 to see both the graphs")
    print()
    print()
    y=int(input("Enter the number:"))
    if y==5:
        dfTN=pd.read_csv("chennai2.csv")
        print(dfTN[dfTN["Active"]>1000])
        
        
            
    elif y==6:
        dfTN.plot(kind="line",x="Months",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()
    elif y==7:
        dfTN.plot(kind="bar",x="Months")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    elif y==8:
        dfTN.plot(kind="line",x="Months",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()

        dfTN.plot(kind="bar",x="Months")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    else:
        print("Invalid Entry")
    

        
    
    print()
    print()
    print()
    print("THANK YOU FOR USING COVINFO. ALWAYS WEAR A MASK, KEEP SANITISING YOUR HANDS AND MAINTAIN SOCIAL DISTANCING :)")
        
    
        
    
elif numberentry==2:
    pop=12500000
    print("Maharastra population is:", pop)
    vac=10000000
    print(vac, "have been vaccinated")
    if vac>pop/2:
        print("Maharastra is safe")
    unvac=pop-vac
    col=[vac,unvac]
    Sec=["vaccinated", "unvaccinated"]
    plt.pie(col,autopct='%1.1f%%',labels=Sec)
    plt.show()
    
    
    print(dfM)
    print()
    print("Press 5 to see the months where the Active cases were greater than 1000")  
    
    print("Press 6 to see the line graph")
    print("Press 7 to see double bar graph")
    print("Press 8 to see both the graphs")
    print()
    print()
    y=int(input("Enter the number:"))
    if y==5:
        dfM=pd.read_csv("Mumbai2.csv")
        print(dfM[dfM["Active"]>1000])
    elif y==6:
        dfM.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()
    elif y==7:
        dfM.plot(kind="bar",x="Month")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    elif y==8:
        dfM.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()

        dfM.plot(kind="bar")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
        print()
        print()
    else:
        print("invalid Entry")
    print("THANK YOU FOR USING COVINFO. ALWAYS WEAR A MASK, KEEP SANITISING YOUR HANDS AND MAINTAIN SOCIAL DISTANCING :)")
elif numberentry==3:
    pop=101900000
    print("WestBengal population is:", pop)
    vac=64927930
    print(vac, "have been vaccinated")
    if vac>pop/2:
        print("West Bengal is safe")
    unvac=pop-vac
    col=[vac,unvac]
    Sec=['vaccinated', 'unvaccinated']
    plt.pie(col,autopct='%1.1f%%', labels=Sec)
    plt.show()
    print(dfW)
    print()
    print()
    print("Press 5 to see the months where the Active cases were greater than 1000")
    print("Press 6 to see the line graph")
    print("Press 7 to see double bar graph")
    print("Press 8 to see both the graphs")
    print()
    print()
    y=int(input("Enter the number:"))
    print()
    print()
    if y==5:
        dfW=pd.read_csv("Kolkata2.csv")
        print(dfW[dfW["Active"]>1000])
    
    
    elif y==6:
        dfW.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()
    elif y==7:
        dfW.plot(kind="bar",x="Month")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    elif y==8:
        dfW.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()

        dfW.plot(kind="bar")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
        print()
        print()
    else:
        print("Invalid Entry")
        print()
        print()
    print("THANK YOU FOR USING COVINFO. ALWAYS WEAR A MASK, KEEP SANITISING YOUR HANDS AND MAINTAIN SOCIAL DISTANCING :)")
elif numberentry==4:
    pop=40000000
    print("Telangana population is:", pop)
    vac=28072820
    print(vac, "have been vaccinated")
    
    if vac>pop/2:
        print("Telangana is safe")
    unvac=pop-vac
    col=[vac,unvac]
    Sec=['vaccinated', 'unvaccinated']
    plt.pie(col,autopct='%1.1f%%', labels=Sec)
    plt.show()
    print(dfT)
    print()
    print()
    print("Press 5 to see the months where the Active cases were greater than 1000")
    print("Press 6 to see the line graph")
    print("Press 7 to see double bar graph")
    print("Press 8 to see both the graphs")
    print()
    print()
    y=int(input("Enter the number:"))
    print()
    print()
    if y==5:
        dfT=pd.read_csv("hyderabad3.csv")
        print(dfT[dfT["Active"]>1000])
    
    elif y==6:
        dfT.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()
    elif y==7:
        dfT.plot(kind="bar",x="Month")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    elif y==8:
        dfT.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()

        dfT.plot(kind="bar")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
        print()
        print()
    else:
        print("Invalid Entry")
        print()
        print()
    print("THANK YOU FOR USING COVINFO. ALWAYS WEAR A MASK, KEEP SANITISING YOUR HANDS AND MAINTAIN SOCIAL DISTANCING :)")
elif numberentry==5:
    pop=27388008
    print("Haryana population is:", pop)
    vac=24267967
    print(vac, "have been vaccinated")
    
    if vac>pop/2:
        print("Haryana is safe")
    unvac=pop-vac
    col=[vac,unvac]
    Sec=['vaccinated', 'unvaccinated']
    plt.pie(col,autopct='%1.1f%%', labels=Sec)
    plt.show()
    print(dfH)
    print()
    print()
    print("Press 5 to see the months where the Active cases were greater than 1000")
    print("Press 6 to see the line graph")
    print("Press 7 to see double bar graph")
    print("Press 8 to see both the graphs")
    print()
    print()
    y=int(input("Enter the number:"))
    print()
    print()
    if y==5:
        df=pd.read_csv("haryana3.csv")
        print(dfH[dfH["Active"]>1000])
    
    elif y==6:
        dfH.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()
    elif y==7:
        dfH.plot(kind="bar",x="Month")
        plt.xticks(x,["Jan", "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
    elif y==8:
        dfH.plot(kind="line",x="Month",  marker="d", markeredgecolor='k')
        plt.xticks(x,["Jan", "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.show()

        dfH.plot(kind="bar")
        plt.xticks(x,['Jan', "Feb", "March", "April","May", "June", "July", "Aug", "Sept","Oct"])
        plt.ylabel("Number of Cases")
        plt.xlabel("Months")
        plt.show()
        print()
        print()
    else:
        print("Invalid Entry")
        print()
        print()
    print("THANK YOU FOR USING COVINFO. ALWAYS WEAR A MASK, KEEP SANITISING YOUR HANDS AND MAINTAIN SOCIAL DISTANCING :)")
else:
    print("Invalid Entry")
    
    

        
    
        
    

   

    
    

                

    






