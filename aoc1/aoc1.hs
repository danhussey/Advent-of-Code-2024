import System.IO
import Data.List (sort)

readline :: String -> (Int, Int)
readline line =
    let [num1, num2] = map read (words line)
    in (num1, num2)

processFile :: FilePath -> IO ([Int], [Int])
processFile filename = do
    contents <- lines <$> readFile filename
    let tuples = map readline contents
    let (list1, list2) = unzip tuples
    pure (sort list1, sort list2)

differenceScore :: ([Int], [Int]) -> Int
differenceScore (list1, list2) =
    sum $ zipWith (\a b -> abs (a - b)) list1 list2

similarityScore :: ([Int], [Int]) -> Int
similarityScore (list1, list2) =
    sum [a * countIn a list2 | a <- list1]

countIn :: Int -> [Int] -> Int
countIn x xs = length (filter (== x) xs)

main :: IO ()
main = do
    result <- processFile "input.txt"
    print $ differenceScore result
    print $ similarityScore result
