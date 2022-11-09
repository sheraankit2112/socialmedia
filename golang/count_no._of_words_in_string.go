package main

import "fmt"

func count(s string) (result map[string]int) {
	result = make(map[string]int)
	str := []rune(s)
	for i := 0; i < len(str); i++ {
		el := result[string(str[i])]
		if el != 0 {
			result[string(str[i])] = result[string(str[i])] + 1
		} else {
			result[string(str[i])] = 1
		}
	}
	return

}

func main() {
	var s string
	fmt.Print("Enter the string:")
	fmt.Scanln(&s)
	fmt.Println(count(s))
}
