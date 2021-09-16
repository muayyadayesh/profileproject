from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
import json
from .models import *
from .forms import ProfileForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    form = ProfileForm()
    if request.method == 'POST':
        #Fetch the POST data
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            print('received!')

            form.save()

            return redirect("app:index")
    return render(request, 'app/index.html', {'form': form})


#POST-GET requests
@method_decorator(csrf_exempt, name='dispatch')
class ProfileObject(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        First_name = data.get('First_name')
        Father_name = data.get('Father_name')
        Middle_name = data.get('Middle_name')
        Last_name = data.get('Last_name')
        Full_address = data.get('Full_address')
        Birthdate = data.get('Birthdate')
        Bio = data.get('Bio')
        Gender = data.get('Gender')
        Country_Birth = data.get('Country_Birth')
        Country_Residence = data.get('Country_Residence')
        Linkedin_URL = data.get('Linkedin_URL')
        Mobile_Number = data.get('Mobile_Number')
        # Languages_List = data.get('Languages_List')

        profile_data = {
            'First_name': First_name,
            'Father_name': Father_name,
            'Middle_name': Middle_name,
            'Last_name': Last_name,
            'Full_address': Full_address,
            'Birthdate': Birthdate,
            'Bio': Bio,
            'Gender': Gender,
            'Country_Birth': Country_Birth,
            'Country_Residence': Country_Residence,
            'Linkedin_URL': Linkedin_URL,
            'Mobile_Number': Mobile_Number,
            # 'Languages_List': Languages_List,
        }

        profile_item = ProfileModel.objects.create(**profile_data)

        data = {
            "message": f"New profile created with id: {profile_item.id}"
        }

        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = ProfileModel.objects.count()
        items = ProfileModel.objects.all()

        items_data = []
        for item in items:
            items_data.append({
            'First_name': item.First_name,
            'Father_name': item.Father_name,
            'Middle_name': item.Middle_name,
            'Last_name': item.Last_name,
            'Full_address': item.Full_address,
            'Birthdate': item.Birthdate,
            'Bio': item.Bio,
            'Gender': item.Gender,
            'Country_Birth': item.Country_Birth,
            'Country_Residence': item.Country_Residence,
            'Linkedin_URL': item.Linkedin_URL,
            'Mobile_Number': item.Mobile_Number,
            # 'Languages_List': item.Languages_List,
            })

        data = {
            'profiles': items_data,
            'count': items_count,
        }

        return JsonResponse(data, status=201)



#Update methods (update-Delete)
@method_decorator(csrf_exempt, name='dispatch')
class ProfileObjectUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = ProfileModel.objects.get(id=item_id)


        item.First_name = data['First_name']
        item.Father_name = data['Father_name']
        item.Middle_name = data['Middle_name']
        item.Last_name = data['Last_name']
        item.Full_address = data['Full_address']
        item.Birthdate = data['Birthdate']
        item.Bio = data['Bio']
        item.Gender = data['Gender']
        item.Country_Birth = data['Country_Birth']
        item.Country_Residence = data['Country_Residence']
        item.Linkedin_URL = data['Linkedin_URL']
        item.Mobile_Number = data['Mobile_Number']
        # item.Languages_List = data['Languages_List']

        item.save()

        data = {
            'message': f'Profile {item_id} has been updated'
        }

        return JsonResponse(data)

    def delete(self, request, item_id):
        item = ProfileModel.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Profile {item_id} has been deleted'
        }

        return JsonResponse(data)
