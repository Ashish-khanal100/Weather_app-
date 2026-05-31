from tkinter import *
from tkinter import ttk
import requests

def all_data():
  city=city_name.get()
  data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f3a42a9ab11d9a38176f660471a9dc7b").json()

  climate1.config(text=data["weather"][0]["main"])
  w_dis1.config(text=data["weather"][0]["description"])
  temp1.config(text=str(int(data["main"]["temp"] -273.15)))
  press1.config(text=data["main"]["pressure"])



# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


# main window ko kam
win =Tk()
win.title("Weather Forcast")
win.config(bg="lightblue")
win.geometry("500x500")

# topic ko kam
toppic=Label(win,text="Weather Forcast",font=("arial",35,"bold"))
toppic.place(x=25,y=50,height=50,width=450)
toppic.config(bg="yellow")



# place ko name choose garne!!
list=["Kathmandu", "Pokhara", "Lalitpur", "Bhaktapur", "Biratnagar", "Chitwan", "Janakpur", "Birgunj", "Dharan", "Butwal", "Hetauda", "Nepalgunj", "Bharatpur", "Tansen", "Bardiya", "Gorkha", "Lumbini", "Namche Bazaar", "Sagarmatha National Park", "Ilam", "Palpa", "Jomsom", "Manang", "Dolpa", "Rara Lake", "Mustang", "Solukhumbu", "Syangja", "Makwanpur", "Dhangadhi"]
city_name=StringVar()
choose=ttk.Combobox(win,font=("arial",20),values=list,textvariable=city_name)
choose.place(x=25,y=120,height=50,width=450,)

# WEATHER CLIMATE
climate=Label(win,text="Weather Climate",font=("arial",17,))
climate.place(x=50,y=240,height=40,width=200,)
climate.config(bg="lightgreen")

climate1=Label(win,text="",font=("arial",17,))
climate1.place(x=270,y=240,height=40,width=200,)
climate1.config(bg="lightgreen")

# WEATHER TEMPERATURE set gare ko!!
temp=Label(win,text="Temperture",font=("arial",17,))
temp.place(x=50,y=300,height=40,width=200,)
temp.config(bg="lightgreen")

temp1=Label(win,text="",font=("arial",17,))
temp1.place(x=270,y=300,height=40,width=200,)
temp1.config(bg="lightgreen")

# pressure
press=Label(win,text="Pressure",font=("arial",17,))
press.place(x=50,y=360,height=40,width=200,)
press.config(bg="lightgreen")

press1=Label(win,text="",font=("arial",17,))
press1.place(x=270,y=360,height=40,width=200,)
press1.config(bg="lightgreen")

# weather discription
w_dis=Label(win,text="Weather Discription",font=("arial",15,))
w_dis.place(x=50,y=420,height=40,width=200,)
w_dis.config(bg="lightgreen")

w_dis1=Label(win,text="",font=("arial",15,))
w_dis1.place(x=270,y=420,height=40,width=200,)
w_dis1.config(bg="lightgreen")

# Button set gare ko!!
button_set=Button(win,text="Set",font=("arial",17),command=all_data)
button_set.place(x=200,y=180,height=40,width=100,)
button_set.config(bg= "pink")


# dev by maile
dev_by=Label(win,text="DEVELOP BY:- Ashish Khanal (PYTHON)",font=("arial",12,))
dev_by.place(x=50,y=480,height=30,width=330,)
dev_by.config(bg= "lightblue")


win.mainloop()

