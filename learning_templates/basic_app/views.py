from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html',
                    {'text':'hello world','number':100})

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    relative_dict = {}
    relative_dict: {'reltext':'hello relative world','relnumber':900}
#    return render(request,'basic_app/relative_url_templates.html',relative_dict)
    return render(request,'basic_app/relative_url_templates.html',{'relative_dict':{'reltext':'hello relative world','relnumber':900}})
