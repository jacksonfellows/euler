module CircularPrimes

let erat n : bool array =
    let (primes : bool array) = Array.create (n+1) true
    primes.[0] <- false
    primes.[1] <- false
    let mutable p = 2
    while p < int (sqrt (double n)) + 1 do
        for i in p+p..p..n do
            primes.[i] <- false
        p <- p+1
    primes

// use this function to check our sieve against https://primes.utm.edu/howmany.html
let primesUnder n = Array.filter id (erat n) |> Array.length

let ps = erat 1000000
let isPrime n = ps.[n]

let rots n =
    let len i = double i |> log10 |> floor |> int
    let rec go (x,l) =
        // TODO: combine into one expression (like divRem in Haskell)
        let lsd = x % 10
        let rest = x / 10
        let next = lsd * (pown 10 l) + rest
        if next <> n then
            next :: go (next,l)
        else []
    n :: go (n,len n)

let isCirc n = rots n |> List.forall isPrime
let numCircs =
    [1..1000000]
    |> List.filter isCirc
    |> List.length

printf "number of circular primes below one million:\n"
numCircs |> printf "%d\n"
