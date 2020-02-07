factorial 0 = 1
factorial 1 = 1
factorial 2 = 2
factorial 3 = 6
factorial 4 = 24
factorial 5 = 120
factorial 6 = 720
factorial 7 = 5040
factorial 8 = 40320
factorial 9 = 362880
factorial _ = error "factorial only defined for digits 0-9"
-- factorial = product . enumFromTo 1

digitFactorialSum = go 0
  where go acc n = case n `divMod` 10 of
                     (0,r) -> acc + factorial r
                     (q,r) -> go (acc + factorial r) q

chainLength = go 0
  where go acc n = case n of
                     1 -> acc + 1
                     2 -> acc + 1
                     145 -> acc + 1
                     169 -> acc + 3
                     363601 -> acc + 3
                     1454 -> acc + 3
                     871 -> acc + 2
                     45361 -> acc + 2
                     872 -> acc + 2
                     45362 -> acc + 2
                     40585 -> acc + 1
                     otherwise -> go (acc + 1) $ digitFactorialSum n

chains = [ n | n <- [1..1000000], chainLength n == 60 ]

main = print $ length chains
