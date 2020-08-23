import Data.Array.Unboxed
import Data.Array.Base (unsafeAt)

facts :: UArray Int Int
facts = array (0,9) [(0,1), (1,1), (2,2), (3,6), (4,24), (5,120), (6,720), (7,5040), (8,40320), (9,362880)]

factorial :: Int -> Int
factorial = unsafeAt facts

digitFactorialSum :: Int -> Int
digitFactorialSum = go 0
  where go acc n = case n `divMod` 10 of
                     (0,r) -> acc + factorial r
                     (q,r) -> go (acc + factorial r) q

chainLength :: Int -> Int
chainLength = go 0
  where go acc n = case n of
                     1 -> acc + 1
                     2 -> acc + 1
                     145 -> acc + 1
                     169 -> acc + 3
                     363601 -> acc + 3
                     1454 -> acc + 3
                     871 -> acc + 2
                     45361 -> acc + 2
                     872 -> acc + 2
                     45362 -> acc + 2
                     40585 -> acc + 1
                     otherwise -> go (acc + 1) $ digitFactorialSum n

chains :: [Int]
chains = [ n | n <- [1..1000000], chainLength n == 60 ]

main :: IO ()
main = print $ length chains
