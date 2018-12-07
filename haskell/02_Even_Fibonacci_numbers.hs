fibs xs = rest ++ fibs [b,a,(a + b)]
    where (a:b:rest) = reverse xs

main = print $ sum $ filter (\n -> n `mod` 2 == 0) $ takeWhile (<4000000) $ fibs [1,1]
