a = int(input("Enter a"))    
b = int(input("Enter b"))  
try:  
    c = a/b  
    print("a/b = ", c)    
except Exception:    
    print("can't divide by zero") 
else:    
    print("Hi I am else block")  
