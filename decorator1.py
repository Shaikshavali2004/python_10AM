from login import login_req

def home_page(name,status):
    print("Home Page")

@login_req
def order_page(name,status):
    print("Order Page")

@login_req
def product_page(name,status):
    print("Product Page")

def contact_page(name,status):
    print("Contact Page")

home_page("RG",True)
order_page("RG",False)
product_page("RG",False)
contact_page("RG",False)