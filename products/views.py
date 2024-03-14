from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {'image': '/static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '369,00р.',
             'desription': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'
             },
            {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face',
             'price': '653,00р.',
             'desription': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
             },
            {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '275,00р.',
             'desription': 'Материал с плюшевой текстурой. Удобный и мягкий.'
             },
            {'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': '174,00р.',
             'desription': 'Плотная ткань. Легкий материал.'
             },
            {'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '679,00р.',
             'desription': 'Гладкий кожаный верх. Натуральный материал.'
             },
            {'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '199,00р.',
             'desription': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
             },

        ]
    }
    return render(request, 'products/products.html', context)
