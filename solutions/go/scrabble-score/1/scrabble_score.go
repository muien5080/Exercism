package scrabble

import "strings"

func Score(word string) int {
    c:=0
    a:= strings.ToUpper(string(word))  
	for i:=0; i<len(a); i++ {
        if a[i] == 'A' || a[i] == 'E' || a[i] == 'I' ||a[i] == 'O' ||a[i] == 'U' ||a[i] == 'L' ||a[i] == 'N' ||a[i] == 'R' ||a[i] == 'S' ||a[i] == 'T'{
            c=c+1
        }else if a[i] == 'D' || a[i]=='G'{
            c=c+2
        }else if a[i] == 'B' ||a[i] == 'C' ||a[i] == 'M' ||a[i] == 'P' {
            c=c+3
        }else if a[i] == 'F' ||a[i] == 'H' ||a[i] == 'V' ||a[i] == 'W' ||a[i] == 'Y' {
            c=c+4
        }else if a[i] == 'K' {
            c=c+5
        }else if a[i] == 'J' ||a[i] == 'X' {
            c=c+8
        }else {
            c=c+10
        }
    }
    return c
}
