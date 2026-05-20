import time 

def MultiplicationTable():

    print("Multiplication Table: \n")
    print("type exit to leave\n")
   
    while True:

       num = (input("Enter a number = "))
      
       if num.lower() == "exit":
           print("exiting program..")
           time.sleep(1)
           break

       num = int(num)

       for i in range(1, 11):
           print(num , "x" , i , "=" , num*i)

      
MultiplicationTable()

    


         