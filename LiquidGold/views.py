from django.shortcuts import render
from .models import DeiselReport, Site, SiteReport
from .forms import NewRequestForm

# Create your views here.
# def goldrequest(request):
#     diesels = DeiselReport.objects.all()
#     context = {'diesels':diesels}
#     return render(request, 'goldrequest.html', context)

# -------------------------------  View for the NewRequestForm------------------------------------------------------
def newRequestFormView(request, pk):
    request_form_instance = Site.objects.get(id=pk)
    form = NewRequestForm(instance=request_form_instance) # pre-fill data from the database

    #--------------------other necessary form logic below------------------------------------------------
    context = {'form': form}
    return render(request, 'goldrequest.html', context)


def goldForm_view(request, id=0):
    form = NewRequestForm()
    r1=Site.objects.all() #getting all the Sites from Database
    r2 = SiteReport.objects.all() #getti ng all the Site reports from Database
    r3 = DeiselReport.objects.all() #getting all the Diesel report from Database
    return render(request, 'goldrequest.html', {
        "form":form,
        "r1":r1})
    
    # if request.method == 'POST':
    #     if id==0:
    #         form = RequestForm(request.POST)
    #     else:
    #         req = DeiselReport.objects.get(pk=id)
    #         form = RequestForm(request.POST, instance=req)
    #     if form.is_valid():
        
    #         form.save() 
    #         return render(request, 'goldrequest.html')
    
    # else:
    #     if id==0:
    #         form = RequestForm()
            
    #     else:
    #         req = DeiselReport.objects.get(pk=id)    
    #         form = RequestForm(instance=req)
        
    #     return render(request, 'goldrequest.html', {'form':form})