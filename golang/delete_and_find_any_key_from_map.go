package main

import "fmt"

var a = make(map[string]int)

func deletee(key string) {
	el, ok := a[key]
	if ok == true {
		delete(a, key)
		fmt.Printf("The key %s with value %d was deleted", el, a[key])
	} else {
		fmt.Printf("The key %s not found", key)

	}

}
func find(key string) {
	var j bool = false
	for i, v := range a {
		if key == i {
			j = true
			fmt.Printf("Yes the %s is find and its value is:%d", key, v)
		}
	}
	if j == false {
		fmt.Println("Sorry the key is not found")
	}

}
func main() {
	a["ankit"] = 21
	a["sahil"] = 20

	var c int
	fmt.Println("1.find\n2.delete")
	for {
		fmt.Print("Enter your choice:")
		fmt.Scanln(&c)
		switch c {
		case 1:
			var s string
			fmt.Print("Enter the key which you want to find:")
			fmt.Scanln(&s)
			find(s)
		case 2:
			var d string
			fmt.Print("Enter the key which you want to delete:")
			fmt.Scanln(&d)
			deletee(d)

		}
	}
}
