import sqlite3

class bd:

    def __init__(self):
        self.conection = sqlite3.connect('/home/igor/Área de trabalho/Artigo Almir/SalesDataBaseTemp.db')
        self.cur = self.conection.cursor()

    def registerProduct(self, name, barCode, amount, purchasePrice, ValueSell, profit):
        #inserir dados do produto na tabela
        product = 'INSERT INTO product (name, barCode, amount, purchasePrice, valueSell, profit) VALUES("{}", "{}", {}, {}, {}, {})'.format(name, barCode, amount, purchasePrice, ValueSell, profit)
        
        self.cur.execute(product)
        self.conection.commit()

