import           Data.Char (digitToInt)

digitSum = sum . map digitToInt . show

main = print $ maximum [ digitSum (a^b) | a <- [1..100], b <- [1..100] ]
