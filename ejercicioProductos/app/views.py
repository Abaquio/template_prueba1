from django.shortcuts import render


# Create your views here.
def index(request):
    return  render(request,'app/index.html')

def productos(request,categoria=None):
    electronica = [
        {
            'id':1,
            'nombre':'Audifonos',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/audifonos.jpg',

        },
        {
            'id':2,
            'nombre':'Mouse',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/mouse.webp'
        },
        {
            'id':3,
            'nombre':'Teclado',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/teclado.png'
        }
    ]

    juguete= [
         {
            'id':1,
            'nombre':'Spider-man',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/spiderman.jpg'
        },
        {
            'id':2,
            'nombre':'Venom',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/venom.webp'
        },
        {
            'id':3,
            'nombre':'ironman',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/ironman.jpg'
        }
    ]

    ropa = [
        {
            'id':1,
            'nombre':'Pantalon',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/jeans.jpeg'
        },
        {
            'id':2,
            'nombre':'Polera',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/polera.webp'
        },
        {
            'id':2,
            'nombre':'Gorra',
            'descrip':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, corrupti rerum? Nobis blanditiis nulla consequatur culpa explicabo laudantium tenetur ullam ipsum aspernatur atque, pariatur voluptatem sint deleniti cum corporis dicta?',
            'imagen':'images/gorro.jpeg'
        },
    ]

    if categoria == 'electronica':
        productos = electronica
    elif categoria == 'juguete':
        productos = juguete
    elif categoria == 'ropa':
        productos = ropa

    else:
        productos=[]


   
    return render(request,'app/productos.html',{'categoria': categoria, 'productos': productos})
