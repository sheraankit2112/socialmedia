package main
import (
    "fmt"
    "strconv"
    
    
    )
    
func main(){
    var(
        size1 int
        size2 int
       
        p string
        n string
        
        )
        
    fmt.Print("Enter the size of array1:")
    fmt.Scanln(&size1)
    var arr1=make([]int,size1)
    for i:=0;i<size1;i++{
        fmt.Scan(&arr1[i])
        p=p + strconv.Itoa(arr1[i])
        
    }
    fmt.Print("Enter the size of array2:")
    fmt.Scanln(&size2)
    
    var arr2=make([]int,size2)
    for i:=0;i<size2;i++{
        fmt.Scan(&arr2[i])
        n=n + strconv.Itoa(arr2[i])
        
        
    }
    
    
    o,err:=strconv.Atoi(p)
    m,err:=strconv.Atoi(n)
    if err==nil{
        fmt.Printf("The joint result of these two array is:%v",o+m)
        
    }
    
}