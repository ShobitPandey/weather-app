from tkinter import *
from tkinter import ttk
import requests 

def data_get():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6844bc7649290119bc658fccffc1a3f1").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)))
    pre_label1.config(text=data["main"]["pressure"])
win = Tk()
win.title("Pandey's Weather Forecast App")
win.config(bg="light blue")
win.geometry("500x500")
                                                                                                                                                                                 

name_label = Label(win,text="Pandey's Weather Forecast App",
                  font=("Time New Roman",23,"bold"))
name_label.place(x=20,y=20,height=40,width=450)

city_name = StringVar()
list_name = ("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
com = ttk.Combobox(win,text="Pandey's Weather Forecast App",values=list_name,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=46,y=78,height=50,width=400)


w_label = Label(win,text="Weather Climate",
                  font=("Time New Roman",23,))
w_label.place(x=25,y=210,height=40,width=200)
w_label1 = Label(win,text="",
                  font=("Time New Roman",23,))
w_label1.place(x=250,y=210,height=40,width=200)

wd_label = Label(win,text="Weather Description",
                  font=("Time New Roman",20,))
wd_label.place(x=24,y=265,height=43,width=200)
wd_label1 = Label(win,text="",
                  font=("Time New Roman",20,))
wd_label1.place(x=250,y=265,height=43,width=200)

temp_label = Label(win,text="Temperature",
                  font=("Time New Roman",20,))
temp_label.place(x=24,y=320,height=43,width=200)
temp_label1 = Label(win,text="",
              font=("Time New Roman",20,))
temp_label1.place(x=250,y=320,height=43,width=200)

pre_label = Label(win,text="Pressure",
                 font=("Time New Roman",20,))
pre_label.place(x=24,y=378,height=43,width=200)
pre_label1 = Label(win,text="",
                  font=("Time New Roman",20,))
pre_label1.place(x=250,y=378,height=43,width=200)




done_button = Button(win,text="Done",
                 font=("Time New Roman",23,"bold"),command=data_get)
done_button.place(x=200,y=145,height=50,width=100)



win.mainloop()
