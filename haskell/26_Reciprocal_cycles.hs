{-# LANGUAGE ScopedTypeVariables #-}

import           Data.List   (elemIndex)
import           Data.Maybe  (fromJust, isJust)
import           Text.Printf (printf)

cycleLen n = go [] n 1
    where go rs n d
            | isJust ind = length rs - fromJust ind
            | r == 0 = 0
            | otherwise = go (rs ++ [r]) n (r*10)
            where (q,r) = d `quotRem` n
                  ind = elemIndex r rs

main = do
    putStrLn $ printf "found a cycle of length %d for %d" len n
    print n
    where (len,n) :: (Int,Int) = maximum $ zip (map cycleLen [1..999]) [1..]
