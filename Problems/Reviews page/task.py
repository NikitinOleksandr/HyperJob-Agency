from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = []  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        self.reviews.append(request)
        return render(request, 'book/reviews.html', context={'reviews': self.reviews})
