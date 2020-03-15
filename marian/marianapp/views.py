from django.shortcuts import render

# Create your views here.

#index
def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)

#about
def about(request):
    datas = {
        
    }
    return render(request, 'about.html', datas)

#blog
def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)

#contact
def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)

#elements
def elements(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)

#main
def main(request):
    datas = {
        
    }
    return render(request, 'main.html', datas)

#rooms
def rooms(request):
    datas = {
        
    }
    return render(request, 'rooms.html', datas)

#services
def services(request):
    datas = {
        
    }
    return render(request, 'services.html', datas)

#single
def single(request):
    datas = {
        
    }
    return render(request, 'single-blog.html', datas)
