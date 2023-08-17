from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1b67a76bb4fce66dc2ab46d2c406813e").json()
    wlabel1.config(text=data["weather"][0]["main"])
    wdlabel1.config(text=data["weather"][0]["description"])
    wtlabel1.config(text=str(int(data["main"]["temp"]-273.15)))
    plabel1.config(text=data["main"]["pressure"])

win =Tk()
win.title("Sky project")
win.config(bg="blue")
win.geometry("500x500")

label1 = Label(win, text="***Weather App***", font=("calibri",40, "bold"))          
label1.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list1=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com= ttk.Combobox(win, text="***Sky Project***",value=list1, font=("calibri",30, "bold"), textvariable=city_name)
com.place(x=50,y=130,height=50,width=400)

wlabel = Label(win, text="Weather Climate",font=("calibri",20, "bold"))           
wlabel.place(x=25,y=250,height=30,width=250)

wlabel1= Label(win, text=" ", font=("calibri",15, "bold"))           
wlabel1.place(x=300,y=250,height=30,width=160)


wdlabel = Label(win, text="Weather Description", font=("calibri",20, "bold"))
wdlabel.place(x=25,y=300,height=30,width=250)

wdlabel1 = Label(win, text=" ", font=("calibri",15, "bold"))
wdlabel1.place(x=300,y=300,height=30,width=160)


wtlabel = Label(win, text="Weather Temprature", font=("calibri",20, "bold"))           
wtlabel.place(x=25,y=350,height=30,width=250)

wtlabel1 = Label(win, text=" ", font=("calibri",15, "bold"))           
wtlabel1.place(x=300,y=350,height=30,width=160)


plabel = Label(win, text="Weather Pressure", font=("calibri",20, "bold"))           
plabel.place(x=25,y=400,height=30,width=250)

plabel1 = Label(win, text=" ", font=("calibri",15, "bold"))           
plabel1.place(x=300,y=400,height=30,width=160)

button= Button(win, text="Done", font=("calibri",20, "bold"),command=data_get)
button.place(x=200,y=200,height=30,width=100)

win.mainloop()
