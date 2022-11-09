package main
import "fmt"

func str_pallen(s string) (raw string){
    r:=[]rune(s)
    
    for i:=len(r)-1;i>=0;i--{
        raw=raw+string(r[i])
        
    }
    return
}

func main(){
    var s string
    fmt.Print("Enter the string:")
    fmt.Scanln(&s)
    fmt.Println(str_pallen(s))
}