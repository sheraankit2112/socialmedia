package main
import "fmt"

func main(){
	var n int
	fmt.Print("Enter a number:")
	fmt.Scanln(&n)
	if (n%2==0){
		fmt.Printf("The %d is an even number",n)
	}else{
		fmt.Printf("The %d is an odd number",n)
	}
}