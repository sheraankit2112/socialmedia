package main

import "fmt"

type student struct {
	name string
	age  int
}

var arr = student{}

func main() {
	fmt.Println(student{name: "Ankit", age: 21})
}
