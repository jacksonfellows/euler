module SquareRootConvergents

let numDigits n = 1 + (System.Numerics.BigInteger.Log10 n |> int)

type Rational(n:bigint, d:bigint) =
    member this.n = n
    member this.d = d

    static member (+) (a, r:Rational) =
        Rational(a,1I) + r
    static member (+) (r:Rational, a) =
        r + Rational(a,1I)
    // not removing common factors (for now)
    static member (+) (r1:Rational, r2:Rational) =
        Rational(r1.n * r2.d + r2.n * r1.d, r1.d * r2.d)

    member this.Inv () =
        Rational(this.d,this.n)

    override this.ToString () =
        sprintf "%A/%A" this.n this.d

let root2 iters =
    let rec go iters =
        match iters with
            | 1 -> Rational(1I,2I)
            | _ -> (2I + go (iters-1)).Inv()
    1I + go iters

let numMoreNumeratorDigits =
    [1..1000]
    |> List.map root2
    |> List.filter (fun r -> numDigits r.n > numDigits r.d)
    |> List.length

[<EntryPoint>]
let main argv =
    numMoreNumeratorDigits
    |> printf "in the first 1000 expansions of the square root of 2, there are %d cases where the numerator has more digits than the denominator\n"
    0
