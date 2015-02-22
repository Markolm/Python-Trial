import random
import time
order = []
print("The script will generate ten random numbers from 1 to 10")
time.sleep(2)
for number in range(10):
    order.append(random.randint(1,9))
print(order)
time.sleep(1)
print("And now will list them in order, from smallest to largest")
time.sleep(2)
proceed = True
while proceed is True:
    proceed = False
    for intval in range(9):
        if order[intval]>order[intval+1]:
            proceed = True
            num1 = order[intval]
            num2 = order [intval+1]
            order[intval] = num2
            order [intval+1] = num1
print(order)

