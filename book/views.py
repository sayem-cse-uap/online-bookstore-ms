from django.shortcuts import render
from .models import Book
# Create your views here.

def book_details(request, pk):
  book_detail = Book.objects.get(id=pk)
  return render(request, 'book_details.html', {'book_detail':book_detail})

  
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