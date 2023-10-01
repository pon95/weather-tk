from tkinter import *
from tkinter import messagebox
import requests as r

def findInfoCoord():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat.get()}&lon={long.get()}&appid=4c363f1db3cf16d9720078314b15bf57&lang=ru'
    resp = r.post(url).json()
    try:
        weather = resp['weather'][0]['description']
        temp = {'temp': float(resp['main']['temp'] - 273.15).__round__(3), 'feels': float(resp['main']['feels_like'] - 273.15).__round__(1)}
        wind = {'speed': resp['wind']['speed'], 'degrees': resp['wind']['deg']}
        place = resp['name'] if resp['name'] != '' else 'неизвестно'

        mes = f"Погода: \nТемпература: {temp['temp']}\n\tОщущается как: {temp['feels']}\n\tОбщее описание: {weather}\nВетер:\n\tСкорость: {wind['speed']}\n\tНаправление: {wind['degrees']}\n\nМесто: {place} \n\nссылка: {url}"
        messagebox.showinfo(title='Погода получена', message=mes)
    except KeyError:
        messagebox.showerror(title='Место не найдено!', message=f'Места по координатам, которые вы указали в первом (долгота) и во втором (широта) не существует\nпроверьте, что координаты написаны в десятичных градусах через ТОЧКУ (не запятую) и попробуйте ещё раз')

def findInfoCity():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.get()}&appid=4c363f1db3cf16d9720078314b15bf57&lang=ru'
    resp = r.post(url).json()
    try:
        weather = resp['weather'][0]['description']
        temp = {'temp': float(resp['main']['temp'] - 273.15).__round__(3), 'feels': float(resp['main']['feels_like'] - 273.15).__round__(1)}
        wind = {'speed': resp['wind']['speed'], 'degrees': resp['wind']['deg']}

        mes = f"Погода: \nТемпература: {temp['temp']}\n\tОщущается как: {temp['feels']}\n\tОбщее описание: {weather}\nВетер:\n\tСкорость: {wind['speed']}\n\tНаправление: {wind['degrees']}\nДолгота: {resp['coord']['lon']}\nШирота: {resp['coord']['lat']}\n\nссылка: {url}"
        messagebox.showinfo(title='Погода получена', message=mes)
    except KeyError:
        messagebox.showerror(title='город не найден!', message='Города, который вы указалив соответствующем (третьем) поле для ввода не существует\nпроверьте правильность написания и попробуйте снова')

root = Tk()
root.geometry('450x320+150+300')
root['bg'] = '#2881FF'
root.title('ПОГОДА ОНЛАЙН')
root.resizable(width=False, height=True)

frame = Frame(root, bg='#0069FF')

otstup_2 = Label(frame, font=10, bg=frame['bg'])

longH = Label(frame, bg=root['bg'], text='Долгота: ')

long = Entry(frame, bg='#004BB4')

latH = Label(frame, bg=root['bg'], text='Широта: ')

lat = Entry(frame, bg='#004BB4')

otstup = Label(frame, bg=frame['bg'])

otstup_3 = Label(frame, bg=frame['bg'])

getinfoCoord = Button(frame, text='узнать погоду (координаты)', bg='#00B487', command=findInfoCoord)
getinfoCity = Button(frame, text='узнать погоду (город)', bg='#00B487', command=findInfoCity)

hintC = Label(frame, bg=root['bg'], text='Город: ')

city = Entry(frame, bg=long['bg'])

frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
otstup_2.pack()
longH.pack()
long.pack()
latH.pack()
lat.pack()
otstup.pack()
getinfoCoord.pack()
otstup_3.pack()
hintC.pack()
city.pack()
getinfoCity.pack()

root.mainloop()