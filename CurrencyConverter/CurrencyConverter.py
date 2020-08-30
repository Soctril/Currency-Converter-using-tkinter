import config 
from tkinter import *
from tkinter.ttk import*
import requests
root = Tk()
ChosenCurrency = 'GBP'
CurrentRatesDict = {}
BaseURL = 'https://prime.exchangerate-api.com/v5/'
FinalURL = BaseURL + config.api_key + "/latest/" + ChosenCurrency 


def ButtonClick(Country):
    global ChosenCurrency
    ChosenCurrency = Country
def GetRates():
    global CurrentRatesDict
    r = requests.get(FinalURL)
    CurrentRatesDict = r.json()
def Convert():
    global ChosenCurrency
    global CurrenrRatesDict
    Amount = int(UserCurrencyValue.get())
    InitialVal = CurrentRatesDict.get('conversion_rates', {}).get(ChosenCurrency)
    InitialVal = Amount/InitialVal
    GBPVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('GBP'),2)
    USDVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('USD'),2)
    CADVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('CAD'),2)
    EURVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('EUR'),2)
    AUDVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('AUD'),2)
    INRVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('INR'),2)
    SGDVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('SGD'),2)
    CNYVal = round(InitialVal*CurrentRatesDict.get('conversion_rates', {}).get('CNY'),2)
    GBPLabel.configure(text='£'+str(GBPVal), font =('Arial', 30))
    USDLabel.configure(text='$'+str(USDVal), font =('Arial', 30))
    CADLabel.configure(text='$'+str(CADVal), font =('Arial', 30))
    EURLabel.configure(text='€'+str(EURVal), font =('Arial', 30))
    AUDLabel.configure(text='$'+str(AUDVal), font =('Arial', 30))
    INRLabel.configure(text='₹'+str(INRVal), font =('Arial', 30))
    SGDLabel.configure(text='$'+str(SGDVal), font =('Arial', 30))
    CNYLabel.configure(text='¥'+str(CNYVal), font =('Arial', 30))
EURImage = PhotoImage(file = r"EURIcon.png")
GBPImage = PhotoImage(file = r"GBPIcon.png")
USDImage = PhotoImage(file = r"USDIcon.png")
CADImage = PhotoImage(file = r"CNDIcon.png")
AUDImage = PhotoImage(file = r"AUDIcon.png")
INRImage = PhotoImage(file = r"INRIcon.png")
SGDImage = PhotoImage(file = r"SGDIcon.png")
CNYImage = PhotoImage(file = r"CNYIcon.png")

GetRates()
GBPVal = CurrentRatesDict.get('conversion_rates', {}).get('GBP')
USDVal = CurrentRatesDict.get('conversion_rates', {}).get('USD')
CADVal = CurrentRatesDict.get('conversion_rates', {}).get('CAD')
EURVal = CurrentRatesDict.get('conversion_rates', {}).get('EUR')
AUDVal = CurrentRatesDict.get('conversion_rates', {}).get('AUD')
INRVal = CurrentRatesDict.get('conversion_rates', {}).get('INR')
SGDVal = CurrentRatesDict.get('conversion_rates', {}).get('SGD')
CNYVal = CurrentRatesDict.get('conversion_rates', {}).get('CNY')
EURResized = EURImage.subsample(4,4)
GBPResized = GBPImage.subsample(4,4)
USDResized = USDImage.subsample(4,4)
CADResized = CADImage.subsample(4,4)
AUDResized = AUDImage.subsample(4,4)
INRResized = INRImage.subsample(4,4)
SGDResized = SGDImage.subsample(4,4)
CNYResized = CNYImage.subsample(4,4)
GBPLabel = Label(root, text='£'+str(GBPVal), font =('Arial', 30))
USDLabel = Label(root, text='$'+str(USDVal), font =('Arial', 30))
CADLabel = Label(root, text='$'+str(CADVal), font =('Arial', 30))
EURLabel = Label(root, text='€'+str(EURVal), font =('Arial', 30))
AUDLabel = Label(root, text='$'+str(AUDVal), font =('Arial', 30))
INRLabel = Label(root, text='₹'+str(INRVal), font =('Arial', 30))
SGDLabel = Label(root, text='$'+str(SGDVal), font =('Arial', 30))
CNYLabel = Label(root, text='¥'+str(CNYVal), font =('Arial', 30))

UserCurrencyValue = Entry(root, width=50)
GBPButton = Button(root, image = GBPResized, command=lambda: ButtonClick('GBP'))
USDButton = Button(root, image = USDResized, command=lambda: ButtonClick('USD'))
CADButton = Button(root, image = CADResized, command=lambda: ButtonClick('CAD'))
EURButton = Button(root, image = EURResized, command=lambda: ButtonClick('EUR'))
AUDButton = Button(root, image = AUDResized, command=lambda: ButtonClick('AUD'))
INRButton = Button(root, image = INRResized, command=lambda: ButtonClick('INR'))
SGDButton = Button(root, image = SGDResized, command=lambda: ButtonClick('SGD'))
CNYButton = Button(root, image = CNYResized, command=lambda: ButtonClick('CNY'))
ConvertButton = Button(root, text='Convert', command=Convert)

GBPButton.grid(row=1, column=0)
GBPLabel.grid(row=1, column=1)
USDButton.grid(row=2, column=0)
USDLabel.grid(row=2, column=1)
EURButton.grid(row=3, column=0)
EURLabel.grid(row=3, column=1)
CADButton.grid(row=4, column=0)
CADLabel.grid(row=4, column=1)
AUDButton.grid(row=5, column=0)
AUDLabel.grid(row=5, column=1)
INRButton.grid(row=1, column=2)
INRLabel.grid(row=1, column=3)
SGDButton.grid(row=2, column=2)
SGDLabel.grid(row=2, column=3)
CNYButton.grid(row=3, column=2)
CNYLabel.grid(row=3, column=3)

UserCurrencyValue.grid(row=0, column=1)
ConvertButton.grid(row=0,column=2)


mainloop()
