#megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

i = 1
found_num = False

while found_num == False:
        num = i*20
        for j in range(20, 0, -1):
                if num % j != 0:
                        break
                if j == 1:
                        found_num = True
        i += 1

print(num)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))