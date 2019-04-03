import           Data.List.Extra (maximumOn)

b n a = fromIntegral (n * (n - 2*a)) / fromIntegral (2 * (n - a))
isWhole x = x - fromIntegral (floor x) == 0

sols n = filter isWhole $ (b n) <$> [1..n`div`4]

main = print $ maximumOn (length . sols) $ [1..1000]
