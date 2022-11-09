package main
import "fmt"

var front int=-1
var rear int=-1
var queue=[5]int {}

func insert(val int){
    if(rear>=4)||(front>=4){
        fmt.Println("queue overflow")
    }else{
        rear=rear+1
        if (rear==1){
            front=front+1
        }else{
            queue[rear]=val
            
        }
    }
}

func delete(){
    if(front<=-1)||(front>=4){
        fmt.Println("queue underflow")
    }else{
        front=front+1
    }
}

func main(){
    
    var val int
    var c int
    fmt.Println("1.insert\n2.delete\n3.display\n4.exit")
    for{
        fmt.Print("Enter your choice:")
        fmt.Scanln(&c)
        switch c{
            case 1:
                fmt.Print("Enter the value:")
                fmt.Scanln(&val)
                insert(val)
                
            case 2:
                delete()
            
            case 3:
                for i:=front;i<=rear;i++{
                    fmt.Print(queue[i])
                }
                fmt.Println("\n")
                
            case 4:
                break
                
            
                
        }
        if c==4{
            break
        }
    }
    
}