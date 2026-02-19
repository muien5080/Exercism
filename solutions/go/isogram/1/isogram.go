package isogram

import "strings"

func IsIsogram(word string) bool {
    word=strings.ToLower(word)
    if word==""{
        return true
    }
    c:=0
	for i:=0; i<len(word);i++{
        for j:=i+1;j<len(word);j++{
            if word[i]==word[j]{
                if word[i]==' ' || word[i]=='-'{
                    continue
                }
                c++
            }
        }
    }
    if c !=0{
        return false
    }else {
        return true
    }
}
