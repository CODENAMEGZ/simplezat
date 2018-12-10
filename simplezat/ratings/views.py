from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import RatingForm


class RatingView(TemplateView):
    template = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class CommentView(TemplateView):
    template = 'comments.html'

    def get(self, request, rating):
        initial = {
            'sentiment': rating
        }
        form = RatingForm(initial=initial)

        return render(
            request,
            self.template,
            {
                'rating': rating,
                'form': form
            }
        )

    def post(self, request, rating):
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('thanks'))
        return render(
            request,
            self.template,
            {
                'rating': rating,
                'form': form
            }
        )


class ThankView(TemplateView):
    template = 'thank.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
