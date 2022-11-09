package main
import "fmt"

func check_even_odd(n int){
    if n%2==0{
        fmt.Printf("The number %d is even",n)
    }else{
        fmt.Printf("The number %d is odd",n)
    }
}
func main(){
    var n int
    fmt.Print("Enter the number:")
    fmt.Scanln(&n)
    check_even_odd(n)
}