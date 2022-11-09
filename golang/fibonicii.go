package main
import "fmt"

func main(){
    var(
        a int=0
        b int=1
        next int
        n int
        
        
        )
    fmt.Print("Enter the number by which you want to print fibonicii:")
    fmt.Scanln(&n)
    fmt.Print(a,b," ") 
    for{
        
        
        next=a+b
        if (next>=n){
            break
        }
        a=b
        b=next
        fmt.Print(next," ")
    }
}