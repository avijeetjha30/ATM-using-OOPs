class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.eamil = email
        self.address = address
    
    def change_address(self,new_name,new_city,new_pincode, new_state):
        self.name = new_name
        self.address.new_address(new_city,new_pincode,new_state)

class CustomerAddress:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def new_address(self,new_city,new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state


add = CustomerAddress("patna",847408,"Bihar")
cust = Customer("avi","123",add)
print(cust.address.city)
cust.change_address("avi","delhi",2020202,"delhi")
print(cust.address.city)
