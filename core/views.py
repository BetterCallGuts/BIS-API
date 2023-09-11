from django.shortcuts import render
from django.http import JsonResponse
# Create your views heredef 
from .models   import Account, Parent


def  getallstudent(req):
    empty_final = []

    for i in Account.objects.all():
        the_data    = {
           
            "name"             : i.name,
            "gender"           : i.gender,
            "age"              : i.age,
            "mother"           : i.mother.name,
            "father"           : i.father.name,
            "state_of_marrieg" : i.state_of_marrieg,
            
            
        }
        empty_final.append(the_data)

    
    
    
    return JsonResponse(
       empty_final,
       safe=False
    )
    

    
    
    






def getallparent(req):
    
    
    
    empty_final = []
    
    for i in Parent.objects.all():
        the_data    = {
            
            "name"             : i.name,
            "gender"           : i.gender,
            "age"              : i.age,
            "the_job"           : i.the_job,
            "work_where"           : i.work_where,
            "state_of_marrieg" : i.state_of_mariege,
            "married_to"        : i.married_to.name
            
        }
        empty_final.append(the_data)
  
    
    print(empty_final)

    return JsonResponse(
        empty_final, safe=False 
        )

def getalldata(req):
    allparentlist    = []
    allstudentlist   = []

    for i in Parent.objects.all():
        the_data    = {
            
            "name"             : i.name,
            "gender"           : i.gender,
            "age"              : i.age,
            "the_job"           : i.the_job,
            "work_where"           : i.work_where,
            "state_of_marrieg" : i.state_of_mariege,
            "married_to"        : i.married_to.name
            
        }
        allparentlist.append(the_data)


    for i in Account.objects.all():
        the_data    = {
           
            "name"             : i.name,
            "gender"           : i.gender,
            "age"              : i.age,
            "mother"           : i.mother.name,
            "father"           : i.father.name,
            "state_of_marrieg" : i.state_of_marrieg,
            
            
        }
        allstudentlist.append(the_data)
    
    
    
    return JsonResponse(
        {
        "Parents":    allparentlist,
        "Students" :    allstudentlist
        }



        , safe=False)