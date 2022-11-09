package main

import "fmt"

func factorial(n int) (fact int) {
	fact = 1
	for i := n; i > 0; i-- {
		fact = fact * i

	}
	return
}
func main() {
	var n int
	fmt.Print("Enter the number:")
	fmt.Scanln(&n)
	fmt.Printf("The factorial of number %d is:%d", n, factorial(n))
}
