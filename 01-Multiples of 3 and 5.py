# megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

total3 = functions.multiples_under_limit(3, 1000)
total5 = functions.multiples_under_limit(5, 1000)
total15 = functions.multiples_under_limit(15, 1000)

total = total3 + total5 - total15

print(total)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))