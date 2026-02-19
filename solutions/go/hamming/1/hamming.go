package hamming

import "errors"

func Distance(a, b string) (int, error) {
	if len(a)!=len(b){
        return 0, errors.New("Strands must be equal length")
    }
    d := 0
    for i:=0;i<len(a);i++{
        if a[i] != b[i]{
            d=d+1
        }
    }
    return d, nil
}
