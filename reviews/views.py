from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

class ThankYouView(TemplateView):
    template_name= "reviews/thank_you.html"

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["message"]="This works"
        return context
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        loaded_review=self.object  # type: ignore
        request=self.request
        fav_id=request.session.get("favorite_review")
        context["is_fav"]= (fav_id==str(loaded_review.id))
        return context
    
class AddFavView(View):
    def post(self,request):
        review_id=request.POST["review_id"]
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect("/reviews/"+review_id)




