package main
import "fmt"
var array=[]int {}


func appendf(){
    var el int
    
    fmt.Print("Enter the value:")
    fmt.Scanln(&el)
    array=append(array,el)
    fmt.Println("ok append it")
    
}
func sort(){
    array1:=array
    for i:=0;i<len(array1)-1;i++{
        for j:=0;j<len(array1)-1;j++{
            if array1[j]>array1[j+1]{
                temp:=array1[j]
                array1[j]=array1[j+1]
                array1[j+1]=temp
            }
        }
    }
    fmt.Printf("The sorted array is:%v",array1)
    
}
func delete(){
    var pos int
    fmt.Print("Enter the position from where you delete the element:")
    fmt.Scanln(&pos)
    array[pos]=0
    fmt.Println("Successfully deleted")
    
}
func min(){
    array1:=array
    for i:=1;i<=len(array1)-1;i++{
        min:=array1[0]
        if array1[i]<min{
            min=array1[i]
        }
    }
    fmt.Printf("The minimum from array %v is:%d",array1,min)
    
    
}
func max(){
    array1:=array
    for i:=1;i<=len(array1)-1;i++{
        max:=array1[0]
        if array1[i]>max{
            max=array1[i]
        }
    }
    fmt.Printf("The maximum from array %v is:%d",array1,max)
    
}

func main(){
    var c int
    fmt.Println("1.append\n2.delete\n3.sort\n4.min\n5.max\n6.swap\n7.exit")
    for{
        fmt.Print("Enter your choice:")
        fmt.Scanln(&c)
        switch c{
            case 1:
                appendf()
            
            case 2:
                delete()
                
            case 3:
                sort()
                
            case 4:
                min()
                
            case 5:
                max()
        }
        if c==6{
            break
        }
    }
    
}