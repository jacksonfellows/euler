import Data.List (permutations)

digits :: String
digits = concatMap show [0..9]

pandigitals :: [String]
pandigitals = permutations digits

divProp :: String -> Bool
divProp xs = foldl1 (&&)
  [ subXs (2,4) `divBy` 2
  , subXs (3,5) `divBy` 3
  , subXs (4,6) `divBy` 5
  , subXs (5,7) `divBy` 7
  , subXs (6,8) `divBy` 11
  , subXs (7,9) `divBy` 13
  , subXs (8,10) `divBy` 17
  ]
  where subXs se = sub se xs

sub (start,end) = take (end-start+1) . drop (start-1)
s `divBy` n = read s `mod` n == 0

main = print $ sum $ read <$> filter divProp pandigitals
