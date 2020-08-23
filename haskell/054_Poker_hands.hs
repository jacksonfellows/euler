import           Control.Monad
import           Data.Char            (digitToInt)
import           Data.List
import           Data.List.Extra      (allSame)
import           Data.Maybe
import           Data.Tuple           (swap)
import           Data.Void
import           Text.Megaparsec
import           Text.Megaparsec.Char

data Value = Num Int | Jack | Queen | King | Ace
  deriving (Eq,Show,Ord)

instance Enum Value where
  fromEnum (Num n) = n
  fromEnum face    = lookupFrom faceEnums face

  toEnum n
    | n <= 10 = Num n
    | otherwise = lookupFrom (map swap faceEnums) n

faceEnums = [(Jack,11), (Queen,12), (King,13), (Ace,14)]

data Suit = Clubs | Diamonds | Hearts | Spades
  deriving (Eq,Show)

instance Ord Suit where
  _ `compare` _ = EQ

type Card = (Value,Suit)

faceNames = [('T', Num 10), ('J',Jack), ('Q',Queen), ('K',King), ('A',Ace)]
suitNames = [('C',Clubs), ('D',Diamonds), ('H',Hearts), ('S',Spades)]

lookupFrom :: Eq a => [(a,b)] -> a -> b
lookupFrom = (fromJust .) . flip lookup

type Parser = Parsec Void String

readValue :: Parser Value
readValue = readNum <|> readFace
  where readNum = Num
          <$> digitToInt <$> satisfy (`elem` "23456789")
        readFace = lookupFrom faceNames <$> letterChar

readSuit :: Parser Suit
readSuit = lookupFrom suitNames <$> letterChar

readCard :: Parser Card
readCard = (,) <$> readValue <*> readSuit

parseCard :: String -> Card
parseCard str = case parse readCard "" str of
  Right res -> res
  Left err  -> error $ errorBundlePretty err

type Hand = [Card]
type Game = (Hand,Hand)

parseHand :: String -> Hand
parseHand = map parseCard . words

parseLine :: String -> Game
parseLine = splitAt 5 . parseHand

parseFile :: String -> [Game]
parseFile = map parseLine . lines

getSameN :: Int -> Hand -> Maybe Hand
getSameN n = listToMaybe . filter ((==n).length) . groupBy valEq . sort
  where a `valEq` b = fst a == fst b

data Rank = HighCard Hand
          | OnePair Hand Hand
          | TwoPairs Hand Hand Hand
          | ThreeOfAKind Hand Hand
          | Straight Hand
          | Flush Hand
          | FullHouse Hand Hand
          | FourOfAKind Hand Hand
          | StraightFlush Hand
          | RoyalFlush
          deriving (Eq,Show,Ord)

type Ranker = Hand -> Maybe Rank

rsort = reverse . sort

getHighCard :: Ranker
getHighCard = return . HighCard . rsort

getOnePair :: Ranker
getOnePair hand = do
  pair <- getSameN 2 hand
  return . OnePair pair . rsort $ hand \\ pair

getTwoPairs :: Ranker
getTwoPairs hand = do
  pair1 <- getSameN 2 hand
  let rest = hand \\ pair1
  pair2 <- getSameN 2 rest
  return . TwoPairs (max pair1 pair2) (min pair1 pair2) . rsort $ rest \\ pair2

getThreeOfAKind :: Ranker
getThreeOfAKind hand = do
  three <- getSameN 3 hand
  return . ThreeOfAKind three . rsort $ hand \\ three

ifTrue :: a -> Bool -> Maybe a
ifTrue a True  = Just a
ifTrue a False = Nothing

isStraight :: Hand -> Bool
isStraight = all (uncurry ((==).succ)) . ap zip tail . sort . map fst

getStraight :: Ranker
getStraight hand = Straight (rsort hand) `ifTrue` isStraight hand

isFlush :: Hand -> Bool
isFlush = allSame . map snd

getFlush :: Ranker
getFlush hand = Flush (rsort hand) `ifTrue` isFlush hand

getFullHouse :: Ranker
getFullHouse hand = do
  three <- getSameN 3 hand
  pair <- getSameN 2 hand
  return $ FullHouse three pair

getFourOfAKind :: Ranker
getFourOfAKind hand = do
  four <- getSameN 4 hand
  return . FourOfAKind four . rsort $ hand \\ four

getStraightFlush :: Ranker
getStraightFlush hand = StraightFlush (rsort hand) `ifTrue` (isStraight hand && isFlush hand)

getRoyalFlush :: Ranker
getRoyalFlush hand = do
  StraightFlush hand' <- getStraightFlush hand
  RoyalFlush `ifTrue` (map fst hand' == enumFromThenTo Ace King (Num 10))

rankers :: [Ranker]
rankers = [
  getRoyalFlush,
  getStraightFlush,
  getFourOfAKind,
  getFullHouse,
  getFlush,
  getStraight,
  getThreeOfAKind,
  getTwoPairs,
  getOnePair,
  getHighCard
  ]

rankHand :: Ranker
rankHand = head . filter (/=Nothing) . ap rankers . return

player1Wins :: Game -> Bool
player1Wins (a,b) = rankHand a > rankHand b

main :: IO ()
main = do
  f <- readFile "../p054_poker.txt"
  print . length . filter player1Wins $ parseFile f
