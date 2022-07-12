from django.shortcuts import render


air_description = {

'green' : ['Good', '0 to 50',  'Air quality is satisfactory, and air pollution poses little or no risk'],
'yellow': ['Moderate', '51 to 100','Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution'],
'orange':['Unhealthy for Sensitive Groups','101 to 150', 'Members of sensitive groups may experience health affects. The general public is less likely to be affected'],
'red':['Unhealthy','151 to 200','Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects'],
'purple':['Very Unhealthy','201 to 300','Health alert: The risk of health effects is increased for everyone'],
'maroon':['Hazardous','301 and higher','Health warning of emergency conditions: everyone is more liekly to be affected']



}

type_check = {

        'Good':  '#0C0',
        'Moderate':  '#FFFF00',
        'Unhealthy For Sensitive Groups':'#FF9900',
        'Unhealthy':  '#FF0000',
        'Very Unhealthy' : '#990066',
        'Hazardous':  '#660000'

}


# Create your views here.
def index(request):
    import json
    import requests
    
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90016&distance=25&API_KEY=1877A952-CAFC-48F6-AC99-DFDA862BCCDB')
    # print(api_request)
    # print(api_request.content)
    try:
        api = json.loads(api_request.content)
        print(api)
    
    except Exception as e:

        api = "something went wrong"

   


    return render(request, 'index.html',{'api':api, 'air_description':air_description,'color':type_check[api[0]['Category']['Name']]})

def air_app(request):
    return render(request, 'air_app.html',{'app':'App'})