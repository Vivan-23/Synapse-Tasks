from itertools import combinations as comb

Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray",
         "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West",
          "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar",
       "Isabel LaRosa", "Shawn Mendes", "Coldplay", "Lauv"}
Edith = {"Metallica", "Billie Ellish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj",
         "Kanye West", "Coldplay"}
list = [Stuart, Bob, Edith, Kevin]
people = 'Kevin', 'Stuart', 'Bob', 'Edith '
x = comb(people, 2)
y = [' & '.join(i) for i in x]
count = []
final = []
for item1, item2 in comb(list, 2):
    m = item1 & item2
    count.append(len(m)*10)
tuple = [(y[0],count[0]),(y[1],count[1]),(y[2],count[2]),(y[3],count[3]),(y[4],count[4]),(y[5],count[5])]
final = (sorted(tuple, key = lambda x: x[1], reverse=True))
final.pop()
print( '   DJ DUO,  Music Overlap %')
for i in range(len(final)):
    print(i+1,'.',final[i])

# OUTPUT
#    DJ DUO,  Music Overlap %
# 1 . ('Kevin & Stuart', 40)
# 2 . ('Kevin & Bob', 40)
# 3 . ('Stuart & Bob', 40)
# 4 . ('Stuart & Edith ', 40)
# 5 . ('Bob & Edith ', 30)
