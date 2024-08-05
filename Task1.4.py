from statistics import mean

customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
waitlist = []
time = customers[0][0]
for i in range(4):
    came = customers[i][0]
    wait = customers[i][1]
    m = time - came
    if m <= 0:
        waitlist.append(wait)
        time += wait
    elif m > 0:
        waitlist.append(m + wait)
        time += wait

mean = mean(waitlist)
print(f"Average Waiting Time is {mean}")
# OUTPUT
# Average Waiting Time is 3.25
