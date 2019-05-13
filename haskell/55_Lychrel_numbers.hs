revN = read . reverse . show

isPalindrome n = n == revN n
isLychrel = not . any isPalindrome . tail . take 50 . iterate (\n -> n + revN n)

main = print . length $ filter isLychrel [1..10000]
