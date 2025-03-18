# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

even = []
odd = []

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i) 
    else:
        odd.append(i)
    
divisible_by_4_6_8_10_3_5_7_9 = []


for i in even:
    if i % 4 == 0 and i % 6 == 0 and i % 8 == 0 and i % 10 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 9 == 0:
        divisible_by_4_6_8_10_3_5_7_9.append(i)

for i in odd:
    if i % 4 == 0 and i % 6 == 0 and i % 8 == 0 and i % 10 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 9 == 0:
        divisible_by_4_6_8_10_3_5_7_9.append(i)