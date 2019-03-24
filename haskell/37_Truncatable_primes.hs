import Data.BitArray.IO
import Data.BitArray
import Control.Monad (when)

truncs :: Int -> [Int]
truncs n = go (0,0) n
  where go (prev,l) n
          | q == 0 = []
          | otherwise = q : new : go (new,l+1) q
          where (q,r) = n `quotRem` 10
                new = r * 10^l + prev

firstPrime :: IOBitArray -> Int -> IO Int
firstPrime primes i = do
  isPrime <- unsafeReadBit primes i
  if isPrime then
    return i
  else firstPrime primes (i+1)

markAllMults :: IOBitArray -> Int -> Int -> IO ()
markAllMults primes n lim = mapM_ (\n -> unsafeWriteBit primes n False) [n*2,n*3..lim]

erat :: Int -> IO BitArray
erat lim = do
  primes <- newBitArray (0,lim) True
  unsafeWriteBit primes 0 False
  unsafeWriteBit primes 1 False
  go primes 2
  freezeBitArray primes
  where root = floor (sqrt (fromIntegral lim))
        go ps n = when (n < root) $ do
          fstTrue <- firstPrime ps n
          markAllMults ps fstTrue lim
          go ps (n+1)


-- use this function to check our sieve against https://primes.utm.edu/howmany.html
primesUnder :: Int -> IO Int
primesUnder lim = do
  primes <- erat lim
  return $ length $ filter id $ bits primes

sieveLim :: Int
sieveLim = 1000000

main :: IO ()
main = do
  primes <- erat sieveLim
  let isPrime = lookupBit primes
      truncPrimes = filter (\n -> n > 10 && isPrime n && all isPrime (truncs n)) [1..sieveLim]
  when (length truncPrimes < 11) $ error "not enough truncatable primes"
  print $ sum $ take 11 $ truncPrimes
