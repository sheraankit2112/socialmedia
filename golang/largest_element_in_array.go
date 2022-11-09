package main
import "fmt"

func main(){
    var size int
    fmt.Print("Enter the size of array:")
    fmt.Scanln(&size)
    
    var arr=make([]int,size)
    var max int=arr[0]
    fmt.Print("Enter the elements:")
    for i:=0;i<size;i++{
        
        fmt.Scan(&arr[i])
    }
    for i:=1;i<size;i++{
        if (max<arr[i]){
            max=arr[i]
        }
        
        
    }
    fmt.Printf("The largest among %v elements is:%d",arr,max)
    
}