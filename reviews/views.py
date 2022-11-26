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


