from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app import forms
from first_app.forms import NewUserForm
# Create your views here.

# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records':webpages_list}
#     return render(request,'first_app/index.html',context=date_dict)

def index(request):
    content = {'name':'Hello World'}
    return render(request,'first_app/index.html',context=content)

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render (request,'first_app/relative_url_templates.html')

def table_access_records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    table_content = {'access_records':webpages_list}
    return render(request,'first_app/table.html',context=table_content)

def home(request):
    return  render(request,'first_app/home.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method =='POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATION SUCCESS")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    content = {'form':form}
    return  render(request,'first_app/form_page.html',context=content)


def store_details(request):
    form = forms.StoreDetails()

    if request.method == 'POST':
        form = forms.StoreDetails(request.POST)

        if form.is_valid():
            #CODE HERE

            print("VALIDATION SUCCESS")
            print('STORE NAME: '+form.cleaned_data['name'])
            print('STORE CODE: '+form.cleaned_data['code'])
            print('LOCATION: '+form.cleaned_data['location'])

    content = {'form_store':form}
    return render(request, 'first_app/new_store.html',context = content)

def signup(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error From Invalid')
    form_content = {'form':form}
    return render(request,'first_app/signup.html',context=form_content)
