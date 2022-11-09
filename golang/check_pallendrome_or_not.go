package main
import "fmt"

func check_pallen(s string){
    arr:=[]rune(s)
    var raw string
    for i:=len(arr)-1;i>=0;i--{
        raw=raw + string(arr[i])
        
    }
    if raw==s{
        fmt.Println("String is pallendrome")
    }else{
        fmt.Println("String is not pallendrome")
    }
}

func main(){
    var s string
    fmt.Print("Enter a string:")
    fmt.Scanln(&s)
    check_pallen(s)
}