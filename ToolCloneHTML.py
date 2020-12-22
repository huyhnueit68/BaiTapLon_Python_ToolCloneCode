import pyodbc
import base64
import sys
from tkinter import*
import urllib.request
from bs4 import BeautifulSoup
import requests

# Import name of server
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-E5TVMPK\MSSQLSERVER01;'
    'Database=Web;'
    'Trusted_Connection=yes;')

# function download html to folder


def cloneUrlLV1():
    # get all link leve 1 in website
    url = ment.get()
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    titels = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # get title of url
    for item in urls:
        try:
            request2 = requests.get(item)
            soup2 = BeautifulSoup(request2.text, 'html.parser')
            for title in soup2.find_all('title'):
                temp = ''.join(e for e in title.get_text() if e.isalnum())
                titels.append(temp)
                print(temp)
        except:
            print("Error Url")
    print("\n")
    # clone html
    for items in urls:
        try:
            mtext = items
            ment1 = titels.pop(0)
            urllib.request.urlretrieve(
                mtext, 'C:/Users/Administrator/Downloads/HTML/%s.html' % (ment1))
            file = open('C:/Users/Administrator/Downloads/HTML/%s.html' %
                        ment1, 'r')
            data = file.read()
            mtext1 = ment1
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Web.dbo.DB')
            SqlCommand = ("INSERT INTO Web.dbo.DB (Name, Code) VALUES (?,?)")
            Value = [mtext1, data]
            cursor.execute(SqlCommand, Value)
            conn.commit()
            print('THANH CONG!!!')
        except:
            print("Clone Error With Url")
    print('CHUONG TRINH KET THUC!!!')
    return


def mdownload():
    try:
        mtext = ment.get()
        urllib.request.urlretrieve(
            mtext, 'C:/Users/Administrator/Downloads/HTML/%s.html' % (ment1.get()))
        file = open('C:/Users/Administrator/Downloads/HTML/%s.html' %
                    ment1.get(), 'r')
        data = file.read()
        mtext1 = ment1.get()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Web.dbo.DB')
        SqlCommand = ("INSERT INTO Web.dbo.DB (Name, Code) VALUES (?,?)")
        Value = [mtext1, data]
        cursor.execute(SqlCommand, Value)
        conn.commit()
    except:
        print("Clone Error With Url")
    print('DONE!!!')
    cloneUrlLV1()
    return


# create form input data
mGui = Tk()
ment = StringVar()
ment1 = StringVar()
mGui.geometry('420x240')
mGui.title('Tool Clone HTML')
mlabel = Label(mGui, text='Enter Url ').pack()
mEntry = Entry(mGui, textvariable=ment).pack()
mlabel = Label(mGui, text='Enter Name file ').pack()
mEntry1 = Entry(mGui, textvariable=ment1).pack()
mbutton = Button(mGui, text='Download Now', command=mdownload, ).pack()
