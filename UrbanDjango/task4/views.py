from django.shortcuts import render


# Create your views here.
def platform_page(request):
    return render(request, 'fourth_task/platform.html')


def books_page(request):
    title = 'Книги'
    name = 'Книги'
    books_all = ['Жюль Верн "Таинственный остров"',
                 'Г.Ф. Лавкрасфт "Хребты безумия"',
                 'Теодор Драйзер "Трилогия желаний"']
    context = {
        'title': title,
        'name': name,
        'books_all': books_all,
    }
    return render(request, 'fourth_task/books.html', context)


def cart_page(request):
    return render(request, 'fourth_task/cart.html')

# Create your views here.
