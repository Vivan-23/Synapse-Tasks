import pandas as pd
from Library import Library, Loan, Members
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 2000)
df = pd.read_csv('RentData.csv')
library = Library()
members = Members("<NAME>", 30, ["<NAME>", "<NAME>", "<NAME>"])
loans = Loan()

if __name__ == '__main__':
    ANSWER = input('Are you a Member of the Library?')

    if ANSWER == "Yes" or ANSWER == "yes" or ANSWER == "Y" or ANSWER == "y":
        Namee = input('Enter Your Name:')
        members.check_Members(Namee)
    elif ANSWER == "No" or ANSWER == "no" or ANSWER == "N" or ANSWER == "n":
        members.add_Member()
    #print(Name)
    i = 0
    count =  0
    while True:
        i = int(input('Enter number:\n1.See Catalogue \n2.Rent\n3.Your History\n4.Return\n5.Exit '))
        match i:
            case 1:
                Type = input('Enter number:\n1.BOOKS \n2.DVDs\n3.Magazines ')
                if Type == "1":
                    library.Print_Books(input('''***ENTER GENRE FROM THESE***\nFantasy\nScience Fiction\nRomance\nHistorical Fiction\nFiction\nMagical Realism\nGothic Fiction\nComing-of-Age\nAdventure\nDystopian Fiction\nSatire\nSocial Realism\nBildungsroman'''))
                elif Type == "2":
                    library.Print_Dvds(input('''***ENTER GENRE FROM THESE***\nFantasy\nDrama\nRomance\nWar\nScience Fiction\nAction \nCrime Drama\nThriller'''))
                elif Type == "3":
                    library.Print_Magazines(input('''***ENTER GENRE FROM THESE***\nScience\nGeography\nFiction\nCulture\nNews\nWorld Affairs\nBusiness\nTravel'''))
                else:
                    break

            case 2:
                loans.Book_Rent(input('Enter ID OF item you wanna Add:'), Namee)
                count +=1

            case 3:
                loans.Your_History(Namee)

            case 4:
                loans.Book_Returned(input('Enter Item ID'))

            case 5:
                break
print('your rented books are:')
print(df.head(count))