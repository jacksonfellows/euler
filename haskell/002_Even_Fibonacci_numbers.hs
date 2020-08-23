fibs = 1 : 1 : zipWith (+) fibs (tail fibs)
prob2 = sum $ filter even $ takeWhile (<4000000) fibs

main = print prob2
