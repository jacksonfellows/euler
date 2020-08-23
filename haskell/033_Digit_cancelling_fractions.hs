{-# LANGUAGE ScopedTypeVariables #-}

import           Data.List  ((\\))
import           Data.Maybe (fromMaybe)
import           Text.Read  (readMaybe)

fracs = do
    d <- [10..99]
    n <- [10..d]
    return (n,d)

isCurious (n,d) = fromMaybe False $ do
    n' <- readMaybe n_canceled
    d' <- readMaybe d_canceled
    return $ foldl1 (&&)
        [ length n_canceled < length n_str
        , length d_canceled < length d_str
        , n' / d' == fromIntegral n / fromIntegral d
        , n `mod` 10 /= 0
        , d `mod` 10 /= 0
        ]
    where n_str = show n
          d_str = show d
          n_canceled = n_str \\ d_str
          d_canceled = d_str \\ n_str

main = print $ d `div` gcd n d
    where (n::Int,d::Int) = foldl1 (\(a,b) (x,y) -> (a*x,b*y)) $ filter isCurious fracs
