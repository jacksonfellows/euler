digits :: Int -> [Int]
digits n
  | q == 0 = [r]
  | otherwise = r : digits q
  where (q,r) = n `quotRem` 10

chain :: Int -> [Int]
chain = iterate (\n -> sum ((^2) <$> digits n))

find89 :: [Int] -> Bool
find89 (x:xs)
  | x == 1 = False
  | x == 89 = True
  | otherwise = find89 xs

main :: IO ()
main = print $ length $ filter (find89 . chain) [1..9999999]
