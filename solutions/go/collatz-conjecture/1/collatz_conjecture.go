package collatzconjecture

import "errors"

func CollatzConjecture(n int) (int, error) {
    t:=0
    if n==1 {
        t=0
        return t , nil
    }
    if n <= 0 {
    return 0, errors.New("number must be positive")
    }else{
		for n!=1 {
        	if n%2 == 0{
            	n=n/2
            	t=t+1
        	}else {
            	n= (n*3)+1
            	t=t+1
        	}
    	}
	}
    return t , nil
}
