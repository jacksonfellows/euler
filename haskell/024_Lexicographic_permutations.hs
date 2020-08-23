import           Data.List (delete)

factorial n = product [1..n]

startingDigit :: Int -> Int -> Int -> (Int,Int)
startingDigit n lexNum numDigits =
    if a > lexNum then (n,lexNum)
    else startingDigit (n+1) (lexNum-a) numDigits
    where a = factorial (numDigits - 1)

lexPerm :: Int -> String -> String
lexPerm lexNum digits
    | 0 <= i && i < length digits = digit : lexPerm newNum (delete digit digits)
    | otherwise = ""
    where (i,newNum) = startingDigit 0 lexNum (length digits)
          digit = digits !! i

main = putStrLn $ lexPerm (1000000 - 1) "0123456789"
