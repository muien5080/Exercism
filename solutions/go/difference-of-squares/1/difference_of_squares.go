package diffsquares

func SquareOfSum(n int) int {
	//BIG
    s:=0
    for i:=1; i<n+1; i++ {
        s=s+i
    }
    return s*s
}

func SumOfSquares(n int) int {
	s:=0
    for i:=1; i<n+1; i++{
        s=s+(i*i)
    }
    return s
}

func Difference(n int) int {
	return SquareOfSum(n)-SumOfSquares(n)
}
