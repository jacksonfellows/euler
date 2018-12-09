import Data.List ((\\))

import           Primes

main = print $ product $ foldl1 (\acc x -> acc ++ (x \\ acc)) $ map primeFactors [1..20]
