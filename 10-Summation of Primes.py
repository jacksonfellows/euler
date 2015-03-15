import Functions as functions, datetime

start_time = datetime.datetime.now()

ans = functions.sum_of_primes_under(2000000)

print(ans)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))