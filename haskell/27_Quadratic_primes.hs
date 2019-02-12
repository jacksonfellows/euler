import qualified Primes      as P
import           Text.Printf (printf)

isPrime :: Int -> Bool
isPrime n = if n > 1 then not $ any (\x -> n `rem` x == 0) [2..lim]
            else False
     where lim = floor $ sqrt $ fromIntegral n

evalQuad :: Int -> Int -> Int -> Int
evalQuad n a b = n^2 + a*n + b

tryAll = do
    a <- [-999..999]
    b <- P.primes [2..1000]
    return $ go 0 a b
    where go n a b = if isPrime (evalQuad n a b) then go (n+1) a b
                     else (n,a,b)

main = putStrLn $ printf "got a prime sequence %d long with a=%d and b=%d.\na*b = %d" n a b (a*b)
    where (n,a,b) = maximum tryAll
