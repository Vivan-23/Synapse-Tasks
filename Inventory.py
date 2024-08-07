import pandas as pd
import csv

df = pd.read_csv('Inventory.csv')


class Product:
    def showinventory(self, category):
        self.category = category
        print(df.loc[df['Sub-category'] == category])

    def ShowAllCategories(self):
        print(df)


class Cart:
    def __init__(self, name, price, sub_category):
        self.name = name
        self.price = price
        self.sub_category = sub_category
        self.List = []
        self.Product = []

    def AddItem(self):
        j = int(input('Enter item number: '))
        Quantity = int(input(f'How many of {df.iloc[j, 0]} do you want to add?'))
        for i in range(Quantity):
            self.List.append(Cart(df.iloc[j, 0], df.iloc[j, 1], df.iloc[j, 2]))

    def ShowPrice(self):
        x = 0
        for cart in range(len(self.List)):
            x = x + self.List[cart].price
        return x

    def RemoveItem(self, Name):
        self.List.remove(self.List[Name])

    def ShowCart(self):
        for cart in range(len(self.List)):
            print(cart, self.List[cart].name, self.List[cart].price, self.List[cart].sub_category, sep=',')
