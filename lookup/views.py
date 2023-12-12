from django.shortcuts import render

def home(request):
    import json
    import requests
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode +"&distance=5&API_KEY=FF7CF77C-76EE-42A5-8BEB-5A6E911591CC")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."
            
            
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
            
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable."
            category_color = "mpderate"
        elif api[0]['Category']['Name'] == "USG":
            category_description = "(101 - 150) People having disease are at greater risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) People may begin to experience health effects.."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: Everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions."
            category_color = "hazardous"
        
        return render(request, 'home.html', {'api': api, 
                                            'category_description': category_description, 
                                            'category_color': category_color})
        
    else:    
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=FF7CF77C-76EE-42A5-8BEB-5A6E911591CC")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."
            
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
            
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable."
            category_color = "mpderate"
        elif api[0]['Category']['Name'] == "USG":
            category_description = "(101 - 150) People having disease are at greater risk."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) People may begin to experience health effects.."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: Everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions."
            category_color = "hazardous"
        
        return render(request, 'home.html', {'api': api, 
                                            'category_description': category_description, 
                                            'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})

