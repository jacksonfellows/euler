getDigits n base
    | q == 0 = [r]
    | otherwise = r : getDigits q base
    where (q,r) = n `quotRem` base

isPalindrome n base = let xs = getDigits n base in xs == reverse xs

main = print $ sum $ filter (\n -> isPalindrome n 2 && isPalindrome n 10) [1..999999]
