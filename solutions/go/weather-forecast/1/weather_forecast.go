// Package weather provides functionality to store and report
// the current weather conditions for cities in Goblinocus.
package weather

var (
	// CurrentCondition stores the current weather condition
	// (e.g., sunny, rainy, cloudy) for the tracked location.
	CurrentCondition string

	// CurrentLocation stores the name of the city for which
	// the current weather condition is reported.
	CurrentLocation string
)

// Forecast updates the current location and its weather condition
// and returns a formatted string describing the current weather
// for the specified city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
