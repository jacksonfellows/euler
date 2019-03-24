isPent :: Int -> Bool
isPent p = fromIntegral (floor n) == n
  where n = (sqrt (24 * fromIntegral p + 1) + 1) / 6

isHex :: Int -> Bool
isHex h = fromIntegral (floor n) == n
  where n = (sqrt (8 * fromIntegral h + 1) + 1) / 4

tris :: [Int]
tris = t_n <$> [285+1..]
  where t_n n = n * (n+1) `div` 2


main :: IO ()
main = print $ head $ filter (\n -> isPent n && isHex n) tris
