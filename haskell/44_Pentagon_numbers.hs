{-# LANGUAGE TupleSections #-}

is_pent n = fromIntegral (floor sol) == sol
    where sol = (1+sqrt(24*fromIntegral n+1))/6

pent n = n*(3*n-1) `div` 2
pents = pent <$> [1..]

pairs []     = []
pairs (x:xs) = ((x,) <$> xs) ++ pairs xs

main = print $
       minimum $
       map (uncurry (flip (-))) $
       filter (\(j,k) -> all is_pent [j+k,k-j]) $
       pairs $
       take 10000 pents
