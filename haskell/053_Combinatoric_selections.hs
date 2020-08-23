factorial = product . enumFromTo 1
c n r = factorial n / (factorial r * factorial (n-r))

main = print . length $ filter (>1000000) [ c n r | n <- [1..100], r <- [1..n] ]
