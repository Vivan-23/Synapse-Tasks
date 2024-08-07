import pandas as pd
import numpy as np
import csv
from datetime import date, timedelta

df = pd.read_csv('library.csv')
mb = pd.read_csv('Members.csv')
rd = pd.read_csv('RentData.csv')


class Library:
    def Print_Library(self):
        print(df)

    def Print_Books(self, Genre):
        new_df = df[df['Type'] == 'Books']
        print(new_df.loc[df['Genre'] == Genre])

    def Print_Dvds(self, Genre):
        new_df = df[df['Type'] == 'DVDs']
        print(new_df.loc[df['Genre'] == Genre])

    def Print_Magazines(self, Genre):
        new_df = df[df['Type'] == 'Magazines']
        print(new_df.loc[df['Genre'] == Genre])

    def Search_Library(self, name):
        print(df[df['Name'] == name])

    def Book_Available(self, book_id):
        try:
            available = df.loc[df['Book ID'] == book_id, 'Availability'].values[0]
            return True
        except (IndexError, KeyError):
            print(f"Book with ID '{book_id}' not found in the library.")
            return False


class Members:

    def __init__(self, Name, Age, Contacts):
        self.Name = Name
        self.Age = Age
        self.Contacts = Contacts
        self.MemberList = []

    def add_Member(self):
        data = [[input('Enter Name: '), input('Enter Age: '), input('Enter Contact: ')]]
        try:
            with open("Members.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"Member added successfully.")
        except Exception as e:
            print(f"Error adding member: {e}")

    def check_Members(self, Name):

        out = mb['Name'].eq(Name).any()
        if out == True:
            print(f"Welcome {Name}")
        else:
            print("Member Not Found")


class Loan():
    def __init__(self):
        self.RentList = []

    def Book_Rent(self, book_id, member_name, today=date.today()):
        DueDate = today + timedelta(days=7)
        if library.Book_Available(book_id):
            self.RentList.append((book_id, member_name, today))
            # Update library data (assuming a writable DataFrame)
            df.loc[df['Book ID'] == book_id, 'Availability'] = False
            df.to_csv('Library.csv', index=False)

            print(f"Book '{book_id}' rented successfully by {member_name}.Due Date: {DueDate}")
            BookName = df.loc[df['Book ID'] == book_id, 'Book Name'].values[0]
            data = [[book_id, BookName, member_name, today, DueDate]]
            try:
                with open("RentData.csv", "a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                    file.close()

            except Exception as e:
                print(f"Error adding member: {e}")
        else:
            print(f"Book '{book_id}' is not currently available.")

    def Book_Returned(self, BookID):
        df.loc[df['Book ID'] == BookID, 'Availability'] = True
        df.to_csv('Library.csv', index=False)

    def Your_History(self, Name):
        print(rd.loc[rd['Taken By'] == Name])


member = Members("<NAME>", 30, ["<NAME>", "<NAME>", "<NAME>"])
#member.add_Member()
#member.check_Members("Vivan")
library = Library()

loan = Loan()
#loan.Book_Rent('BK002', 'Vivan', date.today())
loan.Book_Returned('BK002')
