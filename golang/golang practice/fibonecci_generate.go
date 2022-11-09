package main
import "fmt"

func generate_fibonecci(n int){
    init:=0
    next:=1 
    result:=[]int {}
    result=append(result,init,next)
    var neww int
    for{
        neww=init+next
        
        if neww>=n{
            break
        }else{
            result=append(result,neww)
            
        }
        init=next
        next=neww
        
        
    }
    fmt.Println(result)
    
    
}
func main(){
    var n int
    fmt.Print("Enter the number:")
    fmt.Scanln(&n)
    generate_fibonecci(n)
}