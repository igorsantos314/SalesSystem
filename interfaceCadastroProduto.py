from tkinter import *
from classDataBase import bd

class interfaceProduct(Frame):

    def __init__(self):

        defaultFont = 'Arial 12'

        #objeto de banco de dados
        self.dataBase = bd()

        self.window = Tk()
        self.window.geometry('640x200+260+100')
        self.window.title('Product Register')

        #labels information
        lblName = Label(text='Product Name:', font=defaultFont)
        lblName.place(x=10, y=20)

        lblCode = Label(text='Product Code:', font=defaultFont)
        lblCode.place(x=220, y=20)

        lblQuant = Label(text='Amount:', font=defaultFont)
        lblQuant.place(x=430, y=20)

        lblPurchasePrice = Label(text='Purchase Price:', font=defaultFont)
        lblPurchasePrice.place(x=10, y=100)

        lblValueSell = Label(text='Value Sell:', font=defaultFont)
        lblValueSell.place(x=220, y=100)

        #entrys
        self.etName = Entry(font=defaultFont)
        self.etName.place(x=10, y=50)

        self.etCode = Entry(font=defaultFont)
        self.etCode.place(x=220, y=50)

        self.etAmount = Entry(font=defaultFont)
        self.etAmount.place(x=430, y=50)

        self.etPurchasePrice = Entry(font=defaultFont)
        self.etPurchasePrice.place(x=10, y=130)

        self.etValueSell = Entry(font=defaultFont)
        self.etValueSell.place(x=220, y=130)

        #Menu
        myMenu = Menu(self.window, tearoff=0)
        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Save Product', command=self.setProduct)
        fileMenu.add_command(label='Clear', command=self.clearEts)
        myMenu.add_cascade(label='File', menu=fileMenu)

        self.window.config(menu=myMenu)
        self.window.mainloop()

    #gets
    def getEtName(self):
        return self.etName.get().upper()

    def getEtCode(self):
        return self.etCode.get()
    
    def getEtAmount(self):
        return self.etAmount.get()

    def getEtPurchasePrice(self):
        return self.etPurchasePrice.get()

    def getEtValueSell(self):
        return self.etValueSell.get()

    def getProfit(self):

        try:
            profit = float(self.getEtValueSell()) - float(self.getEtPurchasePrice())
            return profit

        except:
            print('Incorrect Values')

    #cadastrar produto
    def setProduct(self):
        self.dataBase.registerProduct(self.getEtName(), self.getEtCode(), self.getEtAmount(), self.getEtPurchasePrice(), self.getEtValueSell(), self.getProfit())
        #self.dataBase.registerProduct("TECLADO MULTILASER", '1234567891011', 5, 120.25, 150.50, 30.25)

        #limpar campos
        self.clearEts()

    #limpar campos
    def clearEts(self):
        self.etName.delete(0, END)
        self.etCode.delete(0, END)
        self.etAmount.delete(0, END)
        self.etPurchasePrice.delete(0, END)
        self.etValueSell.delete(0, END)

interfaceProduct()