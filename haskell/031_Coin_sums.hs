posSums :: Int -> [Int] -> Int
posSums n [x] = if n `rem` x == 0 then 1 else 0
posSums n (x:xs) = sum $ map (`posSums` xs) [ n - d*x | d <- [0..n `quot` x] ]

main = print $ posSums 200 [1,2,5,10,20,50,100,200]
