isPalindrome n = let s = show n in s == reverse s

main = print $ maximum $ filter isPalindrome [ x*y | x <- [100..999], y <- [100..999] ]
