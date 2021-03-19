package main

import (
	"fmt"
	"math"
)

const zeeEpsilonDen float64 = 19630128.89
const zmumuEpsilonDen float64 = 19631161.45

func main() {
	var N_Selected float64 = 5383098
	var N_background float64 = 2.176e4 + 2.494e4 + 5.271e4 // Wminus_2lep, Wplus_2lep, ttbar_2lep
	var epsilonNum float64 = 4.705e6

	epsilonDen := zeeEpsilonDen
	//epsilonDen := zmumuEpsilonDen

	var epsilon float64 = epsilonNum / epsilonDen
	var intL float64 = 10.064 * math.Pow(10, 15)

	fmt.Printf("epsilon: %v\n", epsilon)
	cross := (N_Selected - N_background) / (epsilon * intL)
	fmt.Printf("Cross Section: %v\n", cross)
}

func uncerts() {

}
//
//N^{background}_{t\Bar{t}} &= 236276
//\\
//N^{background}_{W^+} &= 2247
//\\
//N^{background}_{W-} &= 1785