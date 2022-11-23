from django.shortcuts import render

def review(request):
    if(request.method=="POST"):
        username=request.POST['username']
        print(username)
        return render(request,"reviews/thank_you.html")
    else:
        return render(request,"reviews/review.html")
