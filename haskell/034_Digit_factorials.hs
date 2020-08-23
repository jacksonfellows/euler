import           Data.Char (digitToInt)

fact n = product [1..n]
isDigitFact n = n == (sum $ (fact . digitToInt) <$> show n)

main = print $ (-3) + (sum $ filter isDigitFact [1..10^5])

