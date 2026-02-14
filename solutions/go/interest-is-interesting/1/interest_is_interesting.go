package interest

// InterestRate returns the interest rate for the provided balance.
// InterestRate returns the interest rate for the provided balance.
func InterestRate(balance float64) float32 {
	if balance < 0 {
		return 3.213
	} else if balance < 1000 {
		return 0.5
	} else if balance < 5000 {
		return 1.621
	}
	return 2.475
}

// Interest calculates the interest for the provided balance.
// Interest calculates the yearly interest for the provided balance.
func Interest(balance float64) float64 {
	rate := float64(InterestRate(balance))
	return balance * rate / 100
}


// AnnualBalanceUpdate calculates the annual balance update, taking into account the interest rate.
// AnnualBalanceUpdate returns the balance after one year.
func AnnualBalanceUpdate(balance float64) float64 {
	return balance + Interest(balance)
}


// YearsBeforeDesiredBalance calculates the minimum number of years required to reach the desired balance.
// YearsBeforeDesiredBalance calculates the minimum years to reach the target balance.
func YearsBeforeDesiredBalance(balance, targetBalance float64) int {
	years := 0

	for balance < targetBalance {
		balance = AnnualBalanceUpdate(balance)
		years++
	}

	return years
}

