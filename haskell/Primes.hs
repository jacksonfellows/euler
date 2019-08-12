module Primes
    ( primes
    , primeFactors
    ) where

primes [] = []
primes (x:xs) = x : primes (filter (\n -> n `mod` x /= 0) xs)

primeFactors 1 = []
primeFactors n = f : primeFactors (n `div` f)
    where (f:_) = filter (\p -> n `mod` p == 0) $ primes [2..n]

