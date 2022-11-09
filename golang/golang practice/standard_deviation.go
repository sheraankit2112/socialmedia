package main
import "fmt"
import "math"


func standard_deviation(arr[] int)(result float64){
    mean:=0
    
    for i:=0;i<len(arr);i++{
        mean=mean+arr[i]
        
    }
    mean=mean/len(arr)
    sum:=0
    for i:=0;i<len(arr);i++{
        sum=sum+((arr[i]-mean)*(arr[i]-mean))
    }
    result=math.Sqrt(float64(sum/len(arr)))
    return
}

func main(){
    var arr=[]int {}
    var size int
    fmt.Print("Enter the size of array:")
    fmt.Scanln(&size)
    fmt.Print("Enter the elements:")
    for i:=0;i<size;i++{
        el:=0
        fmt.Scan(&el)
        fmt.Println(el)
        arr=append(arr,el)
    }
    fmt.Println(standard_deviation(arr))
    
    
    
}