package main
import "fmt"

func main(){
    var m int=4
    var n int=4
    for i:=0;i<4;i++{
        for j:=0;j<9;j++{
            if (j<m || j>n){
                fmt.Print(" ")
                
            }else{
                fmt.Print("*")
            }
        }
        fmt.Print("\n")
        m=m-1
        n=n+1
        
    }
    
}