fibs :: [Integer]
fibs = go [1,1]
    where go xs = let (a:b:rest) = reverse xs
                  in rest ++ go [b,a,(a + b)]

main = print $ snd $ head $ dropWhile ((<10^999) . fst) $ zip fibs [1..]
