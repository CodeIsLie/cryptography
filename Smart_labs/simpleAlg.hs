{-
    Basic algebra algs
-}

thirdDouble (x, y, z) = (x, y, z*2)

twoDegree :: Int -> Int -> (Int, Int, Int)
twoDegree x y
    | mod x 2 == 0 && mod y 2 == 0 = thirdDouble $ twoDegree (x `div` 2) (y `div` 2)  
    | otherwise = (x, y, 1)

euclidStep :: Int -> Int -> Int
euclidStep x y
    | x == 1 || y == 1 = 1
    | x == y = x
    | mod x 2 == 0 = euclidStep (div x 2) y
    | mod y 2 == 0 = euclidStep x (div y 2)
    | otherwise = euclidStep (abs(x-y) `div` 2) $ min x y

--binary euclid algoritm
euclid :: Int -> Int -> Int
euclid a b = (trd $ twoDegInfo) * (euclidStep (fstM twoDegInfo) (sndM twoDegInfo) )
    where
        fstM (x, y, z) = x
        sndM (x, y, z) = y
        trd (x, y, z) = z        
        twoDegInfo = twoDegree a b
        
        