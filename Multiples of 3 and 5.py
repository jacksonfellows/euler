# megatheriumNinja
import Functions as functions

total3 = functions.multiples_under_limit(3, 1000)
total5 = functions.multiples_under_limit(5, 1000)
total15 = functions.multiples_under_limit(15, 1000)

total = total3 + total5 - total15

print(total)