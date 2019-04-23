int_sqrt = floor . sqrt . fromIntegral

is_prime 1 = False
is_prime n = not $ any (\x -> n `mod` x == 0) [2..int_sqrt n]

goldbach n = any (\x -> is_prime (n-x)) $ takeWhile (<n) [2*x^2 | x <- [1..]]

odd_comps = filter (not.is_prime) [3,5..]

main = print $ head $ filter (not.goldbach) odd_comps
