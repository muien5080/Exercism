package luhn

import "unicode"

func Valid(id string) bool {
	var digits []int

	// Step 1: Clean input and validate characters
	for _, r := range id {
		if r == ' ' {
			continue
		}
		if !unicode.IsDigit(r) {
			return false
		}
		digits = append(digits, int(r-'0'))
	}

	// Must contain at least two digits
	if len(digits) <= 1 {
		return false
	}

	sum := 0
	double := false

	// Step 2: Traverse from right to left
	for i := len(digits) - 1; i >= 0; i-- {
		d := digits[i]

		if double {
			d *= 2
			if d > 9 {
				d -= 9
			}
		}

		sum += d
		double = !double
	}

	// Step 3: Check divisibility by 10
	return sum%10 == 0
}