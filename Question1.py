import pickle 

class Admin:
    __adminid=1
    def __init__(self,name):
        self.__Name=name
        self.__id=Admin.__adminid
        Admin.__adminid=Admin.__adminid+1

    def getName(self):
        return self.__Name

    def setName(self,name):
        self.__Name=name

    def ViewProducts(self):
        print "######### Products #########"
        try:
            with open("Product","rb") as file:
                while True:
                    try:
                        p = pickle.load(file)
                        print str(p.getId())+"\t"+p.getName()+"\t"+p.getGroup()+"\t"+p.getSubGroup()+"\t"+str(p.getPrice())
                    except EOFError:
                        break
        except:
            print "No products yet... :("

    def AddProducts(self,name,group,subgroup,price):
        new_prod = Product(name,group,subgroup,price)
        with open("Product","a+b") as file:
            pickle.dump(new_prod,file) 

    def DeleteProducts(self,id):
        plist = []
        with open("Product","rb") as file:
            while True:
                try:
                    p = pickle.load(file)
                    if p.getId()!=id:
                        plist.append(p)        
                except EOFError:
                    break

        with open("Product","wb") as file:
            for p in plist:
                pickle.dump(p,file) 

    def ModifyProducts(self,id,name=None,group=None,subgroup=None,price=None):
        plist = []
        with open("Product","rb") as file:
            while True:
                try:
                    p = pickle.load(file)
                    if p.getId()==id:
                        if name!=None:
                            p.setName(name)
                        if group!=None:
                            p.setGroup(group)
                        if subgroup!=None:
                            p.setSubGroup(subgroup)
                        if price!=None:
                            p.setPrice(price)

                    plist.append(p)        
                except EOFError:
                    break

        with open("Product","wb") as file:
            for p in plist:
                pickle.dump(p,file) 

    def MakeShipment(self):
        pass

    def ConfirmDelivery(self):
        pass

class Product:
    __Productid=1
    def __init__(self,name,group,subgroup,price):
        self._Name=name
        self._Group=group
        self._Subgroup=subgroup
        self._Price=price
        id=-1
        try:    
            with open("Product","rb") as file:
                  while True:
                    try:
                        p = pickle.load(file)
                        if p.getId()>=id:
                            id=p.getId()+1
                    except EOFError:
                        break
        except:
            id=1
        self.__id=id

    def getId(self):
        return self.__id

    def getName(self):
        return self._Name

    def setName(self,name):
        self._Name=name

    def getPrice(self):
        return self._Price

    def setPrice(self,price):
        self._Price=price

    def getGroup(self):
        return self._Group

    def setGroup(self,group):
        self._Group=group

    def getSubGroup(self):
        return self._Subgroup

    def setSubGroup(self,subgroup):
        self._Subgroup=subgroup

class Guest:
    __guestnum=1
    def __init__(self):
        self.__guestNumber=Guest.__guestnum
        Guest.__guestnum=Guest.__guestnum+1

    def getGuestNumber(self):
        return self.__guestNumber

    def setGuestNumber(self,number):
        self.__guestNumber=number

    def ViewProducts(self):
        print "######### Products #########"
        try:
            with open("Product","rb") as file:
                while True:
                    try:
                        p = pickle.load(file)
                        print str(p.getId())+"\t"+p.getName()+"\t"+p.getGroup()+"\t"+p.getSubGroup()+"\t"+str(p.getPrice())
                    except EOFError:
                        break
        except:
            print "No products yet... :("

    def GetRegistered(self):
        name = raw_input("Enter your name:")
        address = raw_input("Enter your address:")
        phno = raw_input("Enter your phone no:")
        cust = Customer(name,address,phno)

        with open("Customer","a+b") as file:
            pickle.dump(cust,file)

class Customer:
    def __init__(self,name,address,phno):
        self._Name=name
        self._Address=address
        self._PhNo=phno
        id=-1
        try:    
            with open("Customer","rb") as file:
                while True:
                    try:
                        cust = pickle.load(file)
                        if cust.getId()>=id:
                            id=cust.getId()+1
                    except EOFError:
                        break
        except:
            id=1
        self.__id=id

    def getId(self):
        return self.__id

    def getName(self):
        return self._Name

    def BuyProducts(self):
        with open("Bought","rb") as file:
            bl = pickle.load(file)
            l = bl[self.getId()]
            for p in l:
                print p.getName(), p.getPrice()

    def ViewProducts(self):
        print "######### Products #########"
        try:
            with open("Product","rb") as file:
                while True:
                    try:
                        p = pickle.load(file)
                        print str(p.getId())+"\t"+p.getName()+"\t"+p.getGroup()+"\t"+p.getSubGroup()+"\t"+str(p.getPrice())
                    except EOFError:
                        break
        except:
            print "No products yet... :("

    def MakePayment(self):
        c=None
        cart=None
        cartlist = []
        try:
            with open("Cart","rb") as file:
                while True:
                    try:
                        cart = pickle.load(file)
                        if cart.getId()==self.getId():
                            c=cart
                        else:
                            cartlist.append(cart)
                    except EOFError:
                        break
        except:
            c=None

        if c==None:
            print "No items in cart"
            return

        bought_products = c.getProductList()
        bp = c.getProductList()
        available_prod = []
        with open("Product","rb") as file:
            while True:
                try:
                    p = pickle.load(file)
                    available_prod.append(p.getId())
                except EOFError:
                    break

        av_cart = [x for x in bought_products if x.getId() in available_prod]
        bought_products = av_cart

        print "After removing unavailable products, your cart looks like:"
        for i in bought_products:
            print i.getName(),i.getPrice()
        

        bl = {}
        try:
            with open("Bought","rb") as file:
                try:
                    bl = pickle.load(file)
                except:
                    print "couldn't load"
        except:
            pass

        with open("Bought","wb") as file:
            try:
                if self.getId() in bl.keys():
                    l = bl[self.getId()]
                    l = l+bought_products
                    bl[self.getId()]=l
                    pickle.dump(bl,file)
                else:
                    bl[self.getId()]=bought_products
                    pickle.dump(bl,file)
            except:
                bl[self.getId()]=bought_products
                pickle.dump(bl,file)

        cardtype = raw_input("Enter card type:")
        cardno = raw_input("Card number:")
        payment = Payment(self.getName(),cardtype,cardno,self.getId())
    
        with open("Payment","a+b") as file:
            pickle.dump(payment,file)

        with open("Cart","wb") as file:
            for i in cartlist:
                pickle.dump(i,file)

    def ViewCart(self):
        with open("Cart","rb") as file:
            while True:
                try:
                    c = pickle.load(file)
                    print c.getNumberOfProducts()
                    ls = c.getProductList()
                    for l in ls:
                        print l.getName(),l.getPrice()
                    print c.getTotal()
                except EOFError:
                    break
        print

    def AddToCart(self,prodid):
        p=None
        with open("Product","rb") as file:
            while True:
                try:
                    p = pickle.load(file)
                    if p.getId()==prodid:
                        break
                except EOFError:
                    p=None
                    break

        if p==None:
            print "No such product"
            return

        c=None
        cart=None
        cartlist=[]
        try:
            with open("Cart","rb") as file:
                while True:
                    try:
                        cart = pickle.load(file)
                        if cart.getId()==self.getId():
                            c=cart
                        else:
                            cartlist.append(cart)
                    except EOFError:
                        break
        except:
            c=None

        if c==None:
            c=Cart(self.getId(),1,[p],p.getPrice())
        else:
            c.setNumberOfProducts(c.getNumberOfProducts()+1)
            l = c.getProductList()
            l.append(p)
            c.setProductList(l)
            c.setTotal(c.getTotal()+p.getPrice())

        cartlist.append(c)
        
        with open("Cart","wb") as file:
            for i in cartlist:
                pickle.dump(i,file)

    def DeleteFromCart(self,prodid):
        c=None
        cart=None
        cartlist=[]
        try:
            with open("Cart","rb") as file:
                while True:
                    try:
                        cart = pickle.load(file)
                        if cart.getId()==self.getId():
                            c=cart
                        else:
                            cartlist.append(cart)
                    except EOFError:
                        break
        except:
            c=None

        if c==None:
            print "Cart empty"
            return

        l = c.getProductList()
        r = None
        for i in l:
            if i.getId() == prodid:
                r=i

        if r==None:
            return

        l.remove(r)
        c.setNumberOfProducts(c.getNumberOfProducts()-1)
        c.setProductList(l)
        c.setTotal(c.getTotal()-r.getPrice())
        cartlist.append(c)

        with open("Cart","wb") as file:
            for i in cartlist:
                pickle.dump(i,file)

class Cart:
    def __init__(self,id,numberOfProducts,productList,total):
        self._NumberOfProducts=numberOfProducts
        self._ProductList=productList
        self._Total=total
        self.__id=id

    def getId(self):
        return self.__id

    def getNumberOfProducts(self):
        return self._NumberOfProducts

    def setNumberOfProducts(self,numberOfProducts):
        self._NumberOfProducts=numberOfProducts
    
    def getProductList(self):
        return self._ProductList

    def setProductList(self,productList):
        self._ProductList=productList

    def getTotal(self):
        return self._Total

    def setTotal(self,total):
        self._Total=total

class Payment:
    def __init__(self,name,cardtype,cardno,cid):
        self.Name=name
        self.__CardType=cardtype
        self.__CardNo=cardno
        self._Customerid=cid

    def getName(self):
        return self.Name

    def setName(self,name):
        self.Name=name

    def getCardType(self):
        return self.__CardType
    
    def setCardType(self,cardtype):
        self.__CardType=cardtype

    def getCardNo(self):
        return self.__CardNo
    
    def setCardNo(self,cardno):
        self.__CardNo=cardno


# a = Admin("admin")
# a.AddProducts("Pen","stationary","writing",5)
# a.AddProducts("Pencil","stationary","writing",2)
# a.AddProducts("Apsara Pencil","stationary","writing",2)
# a.AddProducts("Pilot Pen","stationary","writing",200)
# a.ViewProducts()
# a.DeleteProducts(2)
# a.ViewProducts()
# a.ModifyProducts(1,price=40)
# a.ViewProducts()

# c = Customer("ruchu","d 215 pn",886600000)
# print "add 1"
# c.AddToCart(1)
# c.ViewCart()

# print "#############################################"
# print "add 2"
# c.AddToCart(2)
# c.ViewCart()
# print "#############################################"
# print "add 3"
# c.AddToCart(3)
# c.ViewCart()
# print "#############################################"
# print "add 4"
# c.AddToCart(4)
# c.ViewCart()
# print "#############################################"
# a.DeleteProducts(4)
# c.MakePayment()
# c.ViewCart()

# c.BuyProducts()
# c.AddToCart(1)
# c.MakePayment()
# c.BuyProducts()

# c.ViewCart()

def adminOptions():
    a=Admin("admin")
    while True:
        optString = "Press 1 to ViewProducts:\nPress 2 to AddProducts:\nPress 3 to DeleteProducts:\nPress 4 to MofidyProducts:\nPress anything else to exit:\n"
        option = int(raw_input(optString))
        
        if option==1:
            a.ViewProducts()
        elif option==2:
            name=raw_input("Enter details of product:\nName: ")
            group=raw_input("Group: ")
            subgroup=raw_input("Subgroup: ")
            price=int(raw_input("Price: "))
            a.AddProducts(name,group,subgroup,price)
        elif option==3:
            prodid=int(raw_input("Enter product id to delete: "))
            a.DeleteProducts(prodid)
        elif option==4:
            prodid=int(raw_input("Enter product id to modify: "))
            name=None
            group=None
            subgroup=None
            price=None

            choice=raw_input("Do you want to change name? y/n : ")
            if choice=='y':
                name=raw_input("Enter new name: ")
            
            choice=raw_input("Do you want to change group? y/n : ")
            if choice=='y':
                group=raw_input("Enter new group: ")
            
            choice=raw_input("Do you want to change subgroup? y/n : ")
            if choice=='y':
                subgroup=raw_input("Enter new subgroup: ")
            
            choice=raw_input("Do you want to change price? y/n : ")
            if choice=='y':
                price=raw_input("Enter new price: ")
            
            a.ModifyProducts(prodid,name,group,subgroup,price)
        else:
            return 
    print

def customerOptions():
    name=raw_input("Enter your name: ")
    customer=None
    try:    
        with open("Customer","rb") as file:
            while True:
                try:
                    cust = pickle.load(file)
                    if cust.getName()==name:
                        customer=cust
                        break                        
                except EOFError:
                    break
    except:
        customer=None

    if customer==None:
        print "You are not registered. Press r to get registered and e to continue"
        choice=raw_input()
        if choice=='r':
            g=Guest()
            g.GetRegistered()
            return
        else:
            return
    
    print "Welcome ",customer.getName()
    while True:
        optString = "Press 1 to ViewProducts:\nPress 2 to AddToCart:\nPress 3 to DeleteFromCart:\nPress 4 to ViewCart:\nPress 5 to MakePayment:\nPress 6 to ViewBoughtProducts:\nPress anything else to exit:\n"
        option = int(raw_input(optString))

        if option==1:
            customer.ViewProducts()
        elif option==2:
            prodid=int(raw_input("Enter product id to add to cart: "))
            customer.AddToCart(prodid)
        elif option==3:
            prodid=int(raw_input("Enter product id to delete to cart: "))
            customer.DeleteFromCart(prodid)
        elif option==4:
            customer.ViewCart()
        elif option==5:
            customer.MakePayment()
        elif option==6:
            customer.BuyProducts()
        else:
            return


def guestOptions():
    g=Guest()
    while True:
        optString = "Press 1 to ViewProducts:\nPress 2 to get registered:\nPress anything else to exit:\n"
        option = int(raw_input(optString))

        if option==1:
            g.ViewProducts()
        elif option==2:
            g.GetRegistered()
            return    
        else:
            return

while True:
    print "Press 1 for Admin"
    print "Press 2 for Customer"
    print "Press 3 for Guest"
    print "Press 4 to exit"
    choice = int(raw_input())
    if choice==1:
        adminOptions()
    elif choice==2:
        customerOptions()
    elif choice==3:
        guestOptions()
    elif choice==4:
        exit()
    else:
        print "Not a proper option" 