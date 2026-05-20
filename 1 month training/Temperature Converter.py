import time

def Temperature_Converter():
    while True:
      print("Temperature cnverter: \n")
      print("[1] celsius    - fahrenheit\n")
      print("[2] fahrenheit - celsius\n")
      print("[0] exit\n")

      option = int(input("choose the conversion: "))

      if option == 1:
          celsius = float(input("celsius = "))
          celsius = (celsius * 9/5 + 32) 
          print(f"fahrenheit = {celsius}\n")
     
      elif option == 2:
          fahrenheit = float(input("fahrenheit = "))
          fahrenheit = (fahrenheit - 32 * 5/9)
          print(f"celsius = {fahrenheit}\n")
      
      elif option == 0:
          print("exiting program...")
          time.sleep(3)
          break
         
      
      else:
          print("INVALID OPTION")

      


Temperature_Converter()
        

	


         
    