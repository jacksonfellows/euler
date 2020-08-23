import qualified Data.Set as Set

properDivisors :: Int -> [Int]
properDivisors n = 1 : concatMap
               (\x -> let (q,r) = n `quotRem` x
                   in if r == 0 then
                          if x == q then [x]
                          else [x,q]
                      else []) [2..floor$sqrt$fromIntegral n]

isAbundant :: Int -> Bool
isAbundant n = sum (properDivisors n) > n

maxNotSum :: Int
maxNotSum = 28123

abundants :: Set.Set Int
abundants = Set.fromList $ filter isAbundant [1..maxNotSum]

abundant x = Set.member x abundants

posSums :: Int -> [(Int,Int)]
posSums n = zip [1..n `div` 2] [n-1,n-2..]

notAbundantSums :: Int -> [Int]
notAbundantSums lim = filter
    (\n -> not $ any
        (\(a,b) -> abundant a && abundant b)
        $ posSums n)
    [1..lim]

main = print $ sum $ notAbundantSums maxNotSum
