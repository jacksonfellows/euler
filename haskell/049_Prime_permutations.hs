import           Data.List
import           Data.Maybe

isPrime :: Int -> Bool
isPrime 1 = False
isPrime n = not $ any ((==0) . (mod n)) [2..floor(sqrt(fromIntegral n))]

perms :: Int -> [Int]
perms = map read . permutations . show

primePerms :: Int -> Maybe [Int]
primePerms n
  | not (isPrime n) = Nothing
  | null incs = Nothing
  | otherwise = Just [n,n+inc,n+2*inc]
  where ps = filter (>n) . filter isPrime $ perms n
        subs = map (subtract n) ps
        incs = filter ((`elem` subs) . (*2)) subs
        inc = head incs

main :: IO ()
main = mapM_ putStrLn . map (concatMap show) . catMaybes $ map primePerms [1000..9999]
