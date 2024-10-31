from django.shortcuts import render
from .models import Book
# Create your views here.
def search(request):

  if request.method == 'POST':
    searchInput = request.POST['searchInput']
    books = Book.objects.filter(title__contains=searchInput)

    context = {
      'searchInput':searchInput,
      'books':books
    }

    return render(request, 'search.html', context)
  else:
    return render(request, 'search.html')