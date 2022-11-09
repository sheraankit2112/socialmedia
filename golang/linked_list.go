package main
import "fmt"

type node struct {
    
    data int
    nextval *node
    
}
var n=node{}
func insert(){
    var val int
    fmt.Print("Enter the value:")
    fmt.Scanln(&val)
    
    
    if n.data==0{
        n.data=val
        n.nextval=&node{nextval:nil}
        
    }else{
        
        for n.nextval!=nil{
            n=*n.nextval
        }
        n.data=val
        n.nextval=&node{nextval:nil}
    }
    fmt.Println(n)
}
func display(){
    
    fmt.Println(n.data)
    for n.nextval!=nil{
        n=*n.nextval
        fmt.Println(n.data)
    }
}
func main(){
    fmt.Println("1.insert\n2.display")
    var c int
    
    for{
        fmt.Print("Enter your choice:")
        fmt.Scanln(&c)
        switch c{
            case 1:
                insert()
            case 2:
                display()
        }
        if c==3{
            break
        }
    }
    
}