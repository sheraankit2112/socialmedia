package main
import "fmt"

func main(){
    k:=2 
    l:=4
    for i:=1;i<=3;i++{
        for j:=1;j<=5;j++{
            if j>k && j<l{
                fmt.Print("*")
            }else{
                fmt.Print(" ")
            }
            
            
        }
        fmt.Print("\n")
        k=k-1
        l=l+1
        
        
    }
}