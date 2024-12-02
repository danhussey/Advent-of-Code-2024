import System.IO

isGradual :: [Int] -> Bool
isGradual xs = all (\(a, b) -> abs (a-b) >= 1 && abs(a-b) <= 3) $ zip xs (tail xs)

isDirectional :: [Int] -> Bool
isDirectional xs = all (\(a,b) -> a>b || a<b) $ zip xs (tail xs)

main :: IO ()
main = do
    contents <- readFile "input.txt"
    let sets :: [[Int]] = map (map read. words) $ lines contents
    let result :: Int = length $ filter (\x -> isDirectional x && isGradual x) sets
    print result

