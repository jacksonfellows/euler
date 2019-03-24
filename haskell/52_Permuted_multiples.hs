import Data.List (sort)

sameDigits :: Int -> Int -> Bool
sameDigits a b = ss a == ss b
  where ss = sort . show

same6 :: Int -> Bool
same6 x = foldl1 (&&) $ sameDigits x <$> (*x) <$> [2..6]

main :: IO ()
main = print $ head $ filter same6 [1..]
