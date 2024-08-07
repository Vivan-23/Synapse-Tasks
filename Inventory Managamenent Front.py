from Inventory import Product
from Inventory import Cart
import csv
import pandas as pd
import time

pd = pd.read_csv('Inventory.csv')
product = Product()

if __name__ == '__main__':
    list = ['a', 'b', 'c', 'd']
    carte = Cart(0, 0, 0)
    i = 0
    while True:
        i = int(input('Enter number:\n1.Shop Inventory \n2.Add to Cart\n3.See Cart\n4.Remove from Cart\n5.Exit '))
        match i:
            case 1:
                product.ShowAllCategories()

                print('\n')
            case 2:
                carte.AddItem()
                c = 'y'
                while c != 'n':
                    c = input('Want to  Add more:y/n')
                    if c == 'y':
                        carte.AddItem()
                print("Processing...")
                time.sleep(3)
                print('\n')

            case 3:
                print('\n')
                print("YOUR CART:")
                carte.ShowCart()
                print('Total Cart Price is:', '$', carte.ShowPrice())
                print('\n')
                print("Processing...")

                time.sleep(3)

            case 4:
                print('\n')
                j = int(input('Enter item Number:'))
                carte.RemoveItem(j)
                print('\n')
                print("YOUR CART:")
                carte.ShowCart()
                print('Total Cart Price is:', '$', carte.ShowPrice())
                print('\n')

            case 5:
                break
