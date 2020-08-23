import           Data.Char (digitToInt)

main = print $ product $ map (digitToInt . (frac !!) . (10^)) [0..6]
    where frac = concatMap show [0..]
