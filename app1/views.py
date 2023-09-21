from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

# Create your views here.

def product(request):
    productdata=Product.objects.all()
    
    # cartdata=Cart.objects.all()
    # print("data:",cartdata)
    # quantity=0

    # for i in cartdata:
    #     quantity=quantity + i.TotalQantity
    # print("quantity:",quantity)
    return render(request,'product1.html',{'Result':productdata})

def logout_view(request):
    request.session.flush()
    return redirect('/')

def login(request):
    return render(request,'login.html')

def signup(request):
    data=Customers.objects.all()
    return render(request,'login.html')

def signup_detail(request):
    Name=(request.POST['name'])
    Email=(request.POST['email'])
    Mobile=(request.POST['mobile'])
    Password=make_password(request.POST['password'])

    lower_email=Email.lower()

    print("Email value: ",Email)

    data={
        "Name":Name,
        "Email":lower_email,
        "Mobile":Mobile,
        "Password":Password,
    }

    a=Customers(Name=Name,Email=lower_email,Mobile=Mobile,Password=Password)

    if Customers.objects.filter(Email=lower_email).exists():

        messages.error(request,'Email Already Exist!')
        return render(request,'login.html')
    
    else:
        a.save()

        request.session['Name']=a.Name
        request.session['Mobile']=a.Mobile
        request.session['Email']=a.Email
        request.session['Password']=a.Password 
        request.session['id']=a.id

        request.session['is_logged']=True
        # messages.success(request,'Signup Success.')
        return redirect('/')
    
    
def login_detail(request):
    Email=(request.POST["email"])
    Password=(request.POST["password"])
    lower_email=Email.lower()
    print("Email Login & Password:",Email,Password)
    print(Email)

    try:
        context=Customers.objects.get(Email=lower_email)

        
         
        print("Name: ",context.Name)
        request.session['id']=context.id

        if Customers.objects.get(Email=lower_email) and check_password(Password,context.Password):

            request.session['Name']=context.Name
            request.session['Mobile']=context.Mobile
            request.session['Email']=context.Email
            request.session['id']=context.id

            request.session['is_logged']=True
            # messages.success(request,'Sign In Success.')
            return redirect('/')
        
        else:
            messages.error(request,'Invalid Password !')
            return render(request,'login.html')
        
    except:

        messages.error(request,'Invalid Email !')
        return render(request,'login.html')

# def product1(request):
#     return render(request,'product.html')

def clearcart(request):
    cartdata=Cart.objects.all()
    cartdata.delete()
    return redirect('/')



def navbar(request):
    return render(request,'navbar.html')

def footer(request):
    return render(request,'footer.html')

def layout(request):
    return render(request,'layout.html')

def home(request):
    return render(request,'home.html')


def message(request):
    return render(request,'messages.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def success(request,UserID):
    user=User.objects.get(UserID=UserID)
    cart=Cart.objects.all()
    TotalCartPrice=0
    TotalCartQuantity=0
    for i in cart:
        TotalCartPrice=TotalCartPrice+i.TotalPrice
        TotalCartQuantity=TotalCartQuantity+i.TotalQantity

    x=Order(TotalPrice=TotalCartPrice,TotalQuantity=TotalCartQuantity,UserID_id=UserID)
    x.save()

    request.session['TotalQuantity']=x.TotalQuantity

    
    # request.session['ProductID']=data.ProductID_id
    cart.delete()
    return render(request,'success.html',{'OrderData':x,'UserData':user})

def confirmorder(request,UserID):
    Customerss=User.objects.get(UserID=UserID)
    
    print('ressult:',Customerss.UserID)
    return render(request,'confirmorder.html',{'Result':Customerss})

def productremove(request,ProductID):
    data=Product.objects.get(ProductId=ProductID)
    data.delete()

    return render(request,'cart.html')

def showcart(request):
    return render(request,'cart.html')

def cart(request,action,ProductID):
    productdetails=Product.objects.get(ProductID=ProductID)
    cart_item = Cart.objects.filter(ProductID_id=productdetails.ProductID)
    print('cartitem:',cart_item)

#comment if action==add => add ka code
#comment if action==remove => add ka code with minus sign
#comment if action==new => add new obj

    if action=='add':
        if cart_item:
        # Increment the quantity of the existing cart item
            cart_item[0].TotalQantity +=1
            if productdetails.ProductOffer==True:
                cart_item[0].TotalPrice=cart_item[0].TotalPrice+productdetails.OfferPrice

            else:
                cart_item[0].TotalPrice=cart_item[0].TotalPrice+productdetails.ProductPrice
            cart_item[0].save()
            request.session['TotalQantity']=cart_item[0].TotalQantity
            request.session['TotalPrice']=cart_item[0].TotalPrice
           

    elif action=='remove':
        if cart_item:
            if cart_item[0].TotalQantity > 1:  
                cart_item[0].TotalQantity -=1
                if productdetails.ProductOffer==True:
                    cart_item[0].TotalPrice=cart_item[0].TotalPrice-productdetails.OfferPrice

                else:
                    cart_item[0].TotalPrice=cart_item[0].TotalPrice-productdetails.ProductPrice
                cart_item[0].save()
                request.session['TotalQantity']=cart_item[0].TotalQantity
                request.session['TotalPrice']=cart_item[0].TotalPrice

            else:
                if cart_item[0].TotalQantity==1:
                    cart_item.delete()
                    print("lenght",len(Cart.objects.all()))
                    if Cart.objects.filter(ProductID_id=productdetails.ProductID):
                        return redirect('/')
                    
                    else: 
                        if len(Cart.objects.all())==0:
                            return redirect('/')
                        
    elif action=="productremove":
        cartremove1=Cart.objects.get(ProductID_id=productdetails.ProductID)
        cartremove1.delete()
        if Cart.objects.filter(ProductID_id=productdetails.ProductID):
            return render(request,'cart.html',{'productremove1':cartremove1})
        else: 
            if len(Cart.objects.all())==0:
                return redirect('/')

    else:
        if Cart.objects.filter(ProductID_id=productdetails.ProductID).exists():
            if productdetails.ProductOffer==True:
                    newitem=Cart(TotalQantity=1,TotalPrice=productdetails.OfferPrice,ProductID_id=productdetails.ProductID)
            else:
                newitem=Cart(TotalQantity=1,TotalPrice=productdetails.ProductPrice,ProductID_id=productdetails.ProductID)
        # if action=='new':
        else:
            if action=='new':
                if productdetails.ProductOffer==True:
                    newitem=Cart(TotalQantity=1,TotalPrice=productdetails.OfferPrice,ProductID_id=productdetails.ProductID)
                else:
                    newitem=Cart(TotalQantity=1,TotalPrice=productdetails.ProductPrice,ProductID_id=productdetails.ProductID)
                newitem.save()


    cartdetail=Cart.objects.all()
    productdetail=Product.objects.all()
    AllCartDetails=[]
    TotalCartPrice=0
    for i in cartdetail:
        data=Product.objects.filter(ProductID=i.ProductID_id)
        TotalCartPrice=TotalCartPrice+i.TotalPrice
        
        AllCartDetails.append( 
                        {
                        "ProductName":data[0].ProductName,
                        'ProductImage':data[0].ProductImage,
                        'ProductPrice':data[0].ProductPrice,
                        'OfferPrice':data[0].OfferPrice,
                        'ProductOffer':data[0].ProductOffer,
                        'TotalPrice':i.TotalPrice,
                        'TotalQantity':i.TotalQantity,
                        'ProductID':data[0].ProductID,
                        'ProductID_id':i.ProductID_id
                        }
        )
    print("AllCartDetails:",AllCartDetails)

    print("values",productdetails.ProductName,productdetails.OfferPrice,productdetails.ProductPrice)
    return render(request,'cart.html',{'Result':productdetails,'Cartitems':cart_item,'AllCartDetails':AllCartDetails,'TotalCartPrice':TotalCartPrice})





def checkout(request):
    if request.session.has_key('is_logged'):
        return render(request,'checkout.html')
    messages.warning(request,'Please Login !')
    return redirect('/')

def UserDetails(request):
    if request.session.has_key('is_logged'):
        UserName=request.POST['username']
        UserEmail=(request.POST['useremail'])
        UserMobile=(request.POST['usermobile'])
        Address=(request.POST['useraddress'])
        PaymentMethod=(request.POST['userpaymentmethod'])
        lower_email=UserEmail.lower()

        UserData={
                'UserName':UserName,
                'UserEmail':lower_email,
                'UserMobile':UserMobile,
                'Address':Address,
                'PaymentMethod':PaymentMethod,

        }

        x=User(UserName=UserName,UserEmail=lower_email,UserMobile=UserMobile,Address=Address,PaymentMethod=PaymentMethod)
        
        x.save()

        request.session['UserName']=x.UserName
        request.session['UserEmail']=x.UserEmail
        request.session['UserMobile']=x.UserMobile
        request.session['Address']=x.Address

        cartdetail=Cart.objects.all()
        productdetail=Product.objects.all()
        AllCartDetails=[]
        TotalCartPrice=0
        for i in cartdetail:
            data=Product.objects.filter(ProductID=i.ProductID_id)
            TotalCartPrice=TotalCartPrice+i.TotalPrice
            
            AllCartDetails.append( 
                            {
                            "ProductName":data[0].ProductName,
                            'ProductImage':data[0].ProductImage,
                            'ProductPrice':data[0].ProductPrice,
                            'OfferPrice':data[0].OfferPrice,
                            'ProductOffer':data[0].ProductOffer,
                            'TotalPrice':i.TotalPrice,
                            'TotalQantity':i.TotalQantity,
                            'ProductID':data[0].ProductID
                            }
            )

        return render(request,'confirmorder.html',{'Result':x,'AllCartDetails':AllCartDetails,'TotalCartPrice':TotalCartPrice})
    
    messages.warning(request,'Please Login !')
    return redirect('/')

def carosel(request):
    return render(request,'carosel.html')

def about(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')

def profile(request):
    if request.session.has_key('is_logged'):
        return render(request,'profile.html')
    return redirect('/')

def delete(request,id):
    deleteaccount=Customers.objects.get(id=id)
    data=deleteaccount.delete()
    request.session.flush()
    return redirect('/')



   









