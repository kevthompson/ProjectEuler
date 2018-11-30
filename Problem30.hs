import Data.List

main :: IO ()
main = do
    let arrangements = chooseWithRepeats
    let ans = map (fst) $ filter ((==True).snd) $ zip arrangements (map sumPowers arrangements)
    print ans
    print $ sum $ map digitstoint ans 

sumPowers :: [Int] -> Bool
sumPowers arr = arr == (digits $ sum [ [ product $ replicate 5 b | b <-[0..9] ] !! a | a <- arr])

-- Probably a more concise way to do this
chooseWithRepeats :: [[Int]]
chooseWithRepeats = map(dropWhile (==0)) [ [a, b, c, d, e, f] | a <- [0..9], b <- [0..9], c <- [0..9], d <- [0..9], e <- [0..9], f <- [0..9]]

digits :: Integer -> [Int]
digits n = map (\x -> read [x] :: Int) (show n)

digitstoint :: [Int] -> Int
digitstoint n = (read (concatMap (show) n) :: Int)
-- filter ((10000 >)) $ filter ((999 <)) $ 