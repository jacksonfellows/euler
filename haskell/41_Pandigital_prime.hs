import           Data.List (permutations)

isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = not $ any divN [2..floor $ sqrt $ fromIntegral n]
  where divN x = n `mod` x == 0

pandigitals :: Int -> [Int]
pandigitals n = read <$> (permutations $ concatMap show [1..n])

main :: IO ()
main = print $ maximum $ filter isPrime $ concatMap pandigitals [1..9]
