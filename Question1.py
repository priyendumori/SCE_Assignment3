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
        with open("Product","rb") as file:
            while True:
                try:
                    p = pickle.load(file)
                    print str(p.getId())+"\t"+p.getName()+"\t"+p.getGroup()+"\t"+p.getSubGroup()+"\t"+str(p.getPrice())
                except EOFError:
                    break

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
        self.__id=Product.__Productid
        Product.__Productid=Product.__Productid+1

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
    def __init__(self,number):
        self.__guestNumber=number

    def getGuestNumber(self):
        return self.__guestNumber

    def setGuestNumber(self,number):
        self.__guestNumber=number

    def ViewProducts(self):
        pass

    def GetRegistered(self):
        pass

class Customer:
    __Customerid=1
    def __init__(self,name,address,phno):
        self._Name=name
        self._Address=address
        self._PhNo=phno
        self.__id=Customer.__Customerid
        Customer.__Customerid=Customer.__Customerid+1

    def BuyProducts(self):
        pass

    def ViewProducts(self):
        pass

    def MakePayment(self):
        pass

    def AddToCart(self):
        pass

    def DeleteFromCart(self):
        pass

class Cart:
    __Cartid=1
    def __init__(self,numberOfProducts,productList,total):
        self._NumberOfProducts=numberOfProducts
        self._ProductList=productList
        self._Total=total
        self.__id=Cart.__Cartid
        Cart.__Cartid=Cart.__Cartid+1

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


a = Admin("admin")
a.AddProducts("Pen","stationary","writing",5)
a.AddProducts("Pencil","stationary","writing",2)
a.AddProducts("Apsara Pencil","stationary","writing",2)
a.ViewProducts()
a.DeleteProducts(2)
a.ViewProducts()
a.ModifyProducts(1,price=40)
a.ViewProducts()