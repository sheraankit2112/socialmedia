package main
import "fmt"

func find_largest(arr[] int)(largest int){
    largest=arr[0]
    for i:=1;i<len(arr);i++{
        if arr[i]>largest{
            largest=arr[i]
        }
        
    }
    return
}
func main(){
    var size int
    fmt.Print("Enter the size of array:")
    fmt.Scanln(&size)
    var arr=make([]int,size)
    fmt.Print("Enter the elements:")
    for i:=0;i<size;i++{
        el:=0
        fmt.Scan(&el)
        arr=append(arr,el)
        
    }
    fmt.Printf("The largest in array %v is:%v",arr,find_largest(arr))
    
}