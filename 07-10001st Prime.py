#megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

num = functions.nth_prime(10001)

print(num)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))