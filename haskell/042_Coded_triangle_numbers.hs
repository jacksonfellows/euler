import           Data.Void
import           Text.Megaparsec
import           Text.Megaparsec.Char

type Parser = Parsec Void String

word :: Parser String
word = char '"' *> many letterChar <* char '"'

wordList :: Parser [String]
wordList = word `sepBy` (char ',')

wordValue w = sum $ (\c -> fromEnum c - fromEnum 'A' + 1) <$> w

isTri n = fromIntegral (floor i) == i
    where i = (-1 + sqrt (1 + 8*(fromIntegral n)))/2

main = do
    (Just words) <- parseMaybe wordList <$> readFile "../p042_words.txt"
    print $ length $ filter isTri $ wordValue <$> words
