import           Data.List

splitsN :: Int -> [a] -> [[[a]]]
splitsN 1 xs = [[xs]]
splitsN n xs = concat $ zipWith
    (\a b -> if null a || null b then []
             else (a:) <$> splitsN (n-1) b)
    (inits xs) (tails xs)

maxDigit = 9
digits = concatMap show [1..maxDigit]
perms = permutations digits
ids = splitsN 3 `concatMap` perms
valids = filter (\[a,b,c] -> read a == read b * read c) ids
uniqProds = nub $ head <$> valids

main = print $ sum $ read <$> uniqProds
