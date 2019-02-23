{-# LANGUAGE ScopedTypeVariables #-}

import           Data.List   (elemIndex)
import           Data.Maybe  (fromJust)
import           Text.Printf (printf)

cycleLen n = go [] n 1
    where go rs n d
            | ind /= Nothing = length rs - (fromJust ind)
            | r == 0 = 0
            | otherwise = go (rs ++ [r]) n (r*10)
            where (q,r) = d `quotRem` n
                  ind = elemIndex r rs

main = putStrLn $ printf "found a cycle of length %d for %d" len n
    where (len,n) :: (Int,Int) = maximum $ zip (map cycleLen [1..999]) [1..]
