int_sqrt = floor . sqrt . fromIntegral

prime_factors n = case filter (\x -> n `mod` x == 0) [2..int_sqrt n] of
    []    -> [n]
    (x:_) -> x : prime_factors (n `div` x)

test_lim = 10000
test = all (\n -> product (prime_factors n) == n) [1..test_lim]

conseq_uniqs (x:y:xs)
    | x == y = conseq_uniqs (y:xs)
    | otherwise = x : conseq_uniqs (y:xs)
conseq_uniqs other = other

four_uniq_factors = (==4) . length . conseq_uniqs . prime_factors

main = print $ head $ filter (\x -> all four_uniq_factors [x..x+3]) [1..]
