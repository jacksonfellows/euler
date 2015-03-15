# megatheriumNinja
import Functions as functions, datetime

start_time = datetime.datetime.now()

seq = functions.fibonacci(4000000)
seq = functions.return_evens(seq)
total = functions.sum_up_list(seq)

print(total)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print("It took " + str(total_time))