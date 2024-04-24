from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Car,Post,CarImages,YeneUser


from django.core.paginator import Paginator
import time
import telebot
# Create your views here.

def seedSuperUser(request,username,password):
    if User.objects.filter(username = username) or User.objects.filter(email = 'yenemekina@gmail.com') :
        messages.error(request,'Username already exist ')
        return render(request,'login.html')
    try:
        user=User.objects.create_superuser(username,'yenemekina@gmail.com',password)
        try:
            yeneuser=YeneUser.objects.create(user=user)
        except:
            user.delete()
            
            return HttpResponse('Super User Creation Failed')


        messages.success(request,'Super User with the provided username and password has been created...')
        messages.success(request,'Login')
        return render(request,'login.html')
    except:
        messages.success(request,'username or password incorrect or username or email exist')
        return render(request,'login.html')





def home(request):
    posts=Post.objects.all().order_by('-postedAt')
    paginator = Paginator(posts, 12)  # Set the desired number of items per page
    page_number = request.GET.get('page')
    paginated_queryset = paginator.get_page(page_number)
 
   
    context={
        'posts':posts,
        'paginated_queryset':paginated_queryset
    }
   
    
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        result=authenticate(request=request,username=username,password=password)
        
   
        if(result):
            login(request,result)
            messages.success(request,'You\'ve successfully logged in !')
    
            return redirect('post')
        else:
     
            messages.error(request,'Your Username or password is Incorrect !')
            return redirect('login')
            


        

    return render(request,'login.html')

    
def logoutUser(request):
    logout(request)
    messages.info(request,'You\'r successfully logged out !')
    return  redirect('home')
def post(request):
    if request.method == 'POST' and request.user.is_authenticated :
        name=request.POST.get('name')
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        condition=request.POST.get('condition')
        color=request.POST.get('color')
        price=request.POST.get('price')
        plate=request.POST.get('plate')
        telegram=request.POST.get('telegram')
        image1=request.FILES.get('image1')
        multipleImages=request.FILES.getlist('multipleImages')
    

        try:
            savedCar=Car.objects.create(name=name,brand=brand,image=image1,model=model,condition=condition,color=color,plate=plate,price=price,telegram=telegram)
        except :
                messages.error(request,'something went wrong, Pleas try again !' )
                return redirect('post')
        
        if savedCar :
            try:
                posted=Post.objects.create(yeneuser=request.user.yeneuser,car=savedCar)
            except:
         
                savedCar.delete()
                messages.error(request,'something went wrong, Pleas try again !')
                return redirect('post')
            
            
            if posted:
                try:
                    print("trying to post into telegram channel")
                    CarImages.objects.create(car=savedCar,image=image1)
                    
                    # media_group = []
                    
                   
                    for image in multipleImages:
                        CarImages.objects.create(car=savedCar,image=image)
                    #     media_group.append({"type": "photo", "media": CarImages.image})
                    # message=send_data_to_telegram_channel(media_group)
                    messages.success(request,"Posted Successfully !")
                    return redirect('home')
                
                except:
                    messages.error(request,"something went wrong, But Posted the Car!")
                    # message=send_data_to_telegram_channel(media_group)
                    return redirect('home')

                
                    

                
        


       
        return redirect('post')
    elif request.user.is_authenticated :
        return render(request,'post.html')
    else:
        messages.error(request,'Please, Login first !')
        return render(request,'login.html')
bot_token = "5658908983:AAEslZbdmd8FjTcke0xf28x6OGNPI9w9CeU"
bot = telebot.TeleBot(bot_token)
def send_data_to_telegram_channel(multipleImages):
    chat_id = "@test09177"  # Replace with your channel ID
    text="testing the post"
    bot.send_media_group(chat_id, media=multipleImages)


    # for image_url in multipleImages:
    #     time.sleep(5)
    #     bot.send_photo(chat_id, image_url, caption=text)

def carDetail(request,id):
    post=Post.objects.get(pk=id)
    carImages=post.car.cars.all()

    context={
        "post":post,
        "carImages":carImages


    }
    
    return render(request,'postDetail.html',context)

def sold(request,id):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=id)
        post.status = False
        post.save()
        messages.info(request,'Successfully changed the post status!')
        return redirect('home')
        
    
    else:
        messages.error(request,"Please, Login First")
        return render(request,'login.html')
def editPost(request,id):
    if request.user.is_authenticated and request.method == 'GET':
        post=Post.objects.get(pk=id)
        context={
          'post':post,  
        }
        return render(request,'editPost.html',context)
    elif request.user.is_authenticated and request.method == 'GET':
        ...
    else:
        messages.error(request,'please, Login First !')
        return render(request,'login.html')
def soldCars(request):
    if request.user.is_authenticated:
        posts=Post.objects.filter(status=False).order_by('-postedAt')
        paginator = Paginator(posts, 12)  # Set the desired number of items per page
        page_number = request.GET.get('page')
        paginated_queryset = paginator.get_page(page_number)
        context={
        'posts':posts,
        'paginated_queryset':paginated_queryset
    }
        return render(request,'soldCars.html',context)
    else:
        messages.error(request,'Please, Login First !')
        return render(request,'login.html')
