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
    sum $ zipWith (\a b -> abs(a - b)) list1 list2

main :: IO ()
main = do
    result <- processFile "input.txt"
    print $ differenceScore result
    