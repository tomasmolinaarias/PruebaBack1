from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    context = {
        'title': 'Inicio',
        'name': 'Victor Tomas Molina Arias',
        'description': 'Desarrollador Full-Stack.',
        'linkedin': 'https://www.linkedin.com/in/victormolinaarias/',
        'github': 'https://github.com/tomasmolinaarias'
    }
    return render(request, 'index.html', context)

def experience(request):
    experiences = [
        {
            'role': 'Desarrollador Back-end',
            'company': 'Desafío Latam',
            'period': 'Noviembre 2022 - Octubre 2023',
            'description': 'Participé en los proyectos de incubadora para desarrollar una página web centrada en Desafío. Implementé tecnologías clave como Node.js, Express, MySQL (Sequelize) y Firebase.',
            'skills': ['Node.js', 'Express', 'MySQL', 'Firebase', 'API REST'],
        },
        {
            'role': 'Desarrollador Full-stack',
            'company': 'Freelance',
            'period': 'Junio 2022 - Agosto de 2022',
            'description': 'Desarrollé un sistema con el stack de JavaScript aplicando un modelo de predicción de precios de madera mediante el método Brown, usando Node.js y Express para servicios REST.',
            'skills': ['Node.js', 'Express', 'JavaScript', 'Scraping', 'React'],
        },
        {
            'role': 'Desarrollador Full-stack',
            'company': 'SCGEEK',
            'period': 'Agosto 2024 - Septiembre 2024',
            'description': 'Actualmente, estoy trabajando agregando código para tomar datos de máquinas industriales y mostrarlos por medio de gráficos.',
            'skills': ['Typescript', 'Angular', 'node-OPC', 'Websocket', 'mysql'],
        }
    ]
    context = {
        'title': 'Experiencia',
        'name': 'Victor Tomas Molina Arias',
        'description': 'Desarrollador Full-Stack.',
        'linkedin': 'https://www.linkedin.com/in/victormolinaarias/',
        'github': 'https://github.com/tomasmolinaarias',
        'experiences': experiences
    }
    return render(request, 'experience.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        
        subject = f'Nuevo mensaje de {name}'
        message = f'Nombre: {name}\nCorreo: {email}\nTeléfono: {phone}\nMensaje:\n{comment}'
        from_email = 'tuemail@gmail.com'
        recipient_list = ['victortomasmolinaarias@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')
            return redirect('contact')
        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {e}')

    context = {
        'title': 'Contacto',
        'name': 'Victor Tomas Molina Arias',
        'description': 'Desarrollador Full-Stack.',
        'linkedin': 'https://www.linkedin.com/in/victormolinaarias/',
        'github': 'https://github.com/tomasmolinaarias'
    }
    return render(request, 'contact.html', context)
