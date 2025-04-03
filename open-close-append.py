with open("output.txt", "r") as names:
    what_is_in_output_txt = names.read()
    print(what_is_in_output_txt)
    
with open("output.txt", "w") as output_file:
    output_file.write("Eqarus, Mosa's Delights, Divine")
    print("File written successfully")
    output_file.close()
    print("File closed successfully")
    
with open("output.txt", "a") as file:
    print("File opened successfully")
    file.write(", Peter, Jasper, Phalanetsholo")
    print("File appended successfully")
    file.close() 
    print("File closed successfully") 

with open("output.txt", "r") as file:
    data1 = file.read()
    print(data1)    
    file.close()