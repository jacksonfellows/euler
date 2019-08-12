import Data.List (inits, permutations)

isConcatProd :: String -> Bool
isConcatProd digits = any works (tail $ inits $ digits)
  where works i = any (== digits) $ takeWhile
          (\ds -> length ds <= length digits) $
          concat <$> (flip take) prods <$> [2..]
          where prods = (\n -> show (n * read i)) <$> [1..]

pandigitals :: [String]
pandigitals = permutations $ concatMap show [1..9]

main :: IO ()
main = putStrLn $ maximum $ filter isConcatProd pandigitals
