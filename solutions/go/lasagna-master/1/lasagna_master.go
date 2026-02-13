package lasagna


// TODO: define the 'PreparationTime()' function
func PreparationTime (layers []string, AvgPrepTime int)int {
    if AvgPrepTime == 0{
        AvgPrepTime =2
    }
    return len(layers) * AvgPrepTime
}
// TODO: define the 'Quantities()' function
func Quantities (layers []string,) (int, float64) {
    var noodles int
    var sauce float64
    noodles = 0
    sauce = 0.0
    for _, layer:= range layers {
        switch layer {
            case "noodles":
            	noodles+=50
            case "sauce":
            	sauce+= 0.2
        }
    }
    return noodles, sauce
}
// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList, myList []string) {
    if len(friendsList) == 0 || len(myList) == 0 {
        return
    }

    secretIngredient := friendsList[len(friendsList)-1]
    myList[len(myList)-1] = secretIngredient
}
// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64,portions int) []float64 {
     factor := float64(portions) / 2

    // Create a new slice to avoid modifying the original
    scaled := make([]float64, len(quantities))

    for i, quantity := range quantities {
        scaled[i] = quantity * factor
    }

    return scaled
}
// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
