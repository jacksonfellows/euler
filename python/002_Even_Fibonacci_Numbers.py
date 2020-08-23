# megatheriumNinja
import Functions as functions, datetime

seq = functions.fibonacci(4000000)
seq = functions.return_evens(seq)
total = functions.sum_up_list(seq)

print(total)