def serve_chai():
    chai_type= "Masala" #local_scope
    print(f"Inside Function {chai_type}")

chai_type ="Ginger"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order ="Masala"
    def print_order():
        chai_order = "Ginger"
        print("Inner", chai_order)
    print_order()
    print("Outer" , chai_order)
chai_order  = "Tulsi"
chai_counter()
print("Global", chai_order)


        