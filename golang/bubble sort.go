package main
import "fmt"

func main(){
    var array[5] int
    var m bool=false
    fmt.Print("Enter the array:")
    for i:=0;i<5;i++{
        fmt.Scan(&array[i])
        
    }
    for j:=0;j<5;j++{
        for i:=0;i<4;i++{
            if(array[i]>array[i+1]){
            temp:=array[i+1]
            array[i+1]=array[i]
            array[i]=temp
            m=true
            }
            
            
        }
        if m==false{
            break
        }else{
            m=false
        }
        
    }
    fmt.Printf("storted array is:%v",array)
}