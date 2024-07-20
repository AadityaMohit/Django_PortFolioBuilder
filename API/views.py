import json
from mailbox import Message
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from .forms import PortfolioForm, SkillFormSet, ProjectImageFormSet, TemplateChoiceForm
from .models import PortfolioImage
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout  # Rename the import
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def portfolio_form(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        skill_formset = SkillFormSet(request.POST, prefix='skills')
        project_image_formset = ProjectImageFormSet(request.POST, request.FILES, prefix='project_images')
        template_form = TemplateChoiceForm(request.POST)
        
        if form.is_valid() and skill_formset.is_valid() and project_image_formset.is_valid() and template_form.is_valid():
            name = form.cleaned_data['name']
            experience = form.cleaned_data['experience']
            image = form.cleaned_data['image']
            achievements = form.cleaned_data['achievements']
            contact_number = form.cleaned_data['contact_number']
            contact_email = form.cleaned_data['contact_email']
            linkedin = form.cleaned_data['linkedin']
            github = form.cleaned_data['github']
            
            skills = [skill_form.cleaned_data['skill'] for skill_form in skill_formset]
            project_images = [
                {
                    'project_image': project_image_form.cleaned_data['project_image'],
                    'project_url': project_image_form.cleaned_data['project_url']
                }
                for project_image_form in project_image_formset
            ]
            
            template_choice = template_form.cleaned_data['template_choice']
            
            # Save the portfolio image
            image_instance = PortfolioImage(image=image)
            image_instance.save()
            image_url = image_instance.image.url
            
            # Save project images and get URLs
            project_image_urls = []
            for project in project_images:
                project_image_instance = PortfolioImage(image=project['project_image'])
                project_image_instance.save()
                project_image_urls.append({
                    'project_image_url': project_image_instance.image.url,
                    'project_url': project['project_url']
                })
            
            # Encode skills and project images as JSON strings
            skills_json = json.dumps(skills)
            project_images_json = json.dumps(project_image_urls)
            
            # Create the redirect URL with URL-encoded query parameters
            query_params = urlencode({
                'name': name,
                'experience': experience,
                'achievements': achievements,
                'skills': skills_json,
                'project_images': project_images_json,
                'image_url': image_url,
                'contact_number': contact_number,
                'contact_email': contact_email,
                'linkedin': linkedin,
                'github': github,
            })
            redirect_url = f"{reverse(template_choice)}?{query_params}"
            return redirect(redirect_url)
    else:
        form = PortfolioForm()
        skill_formset = SkillFormSet(prefix='skills')
        project_image_formset = ProjectImageFormSet(prefix='project_images')
        template_form = TemplateChoiceForm()
    
    return render(request, 'portfolio_form.html', {
        'form': form,
        'skill_formset': skill_formset,
        'project_image_formset': project_image_formset,
        'template_form': template_form
    })

def template1(request):
    name = request.GET.get('name', '')
    experience = request.GET.get('experience', '')
    achievements = request.GET.get('achievements', '')
    skills_json = request.GET.get('skills', '[]')
    skills = json.loads(skills_json)
    project_images_json = request.GET.get('project_images', '[]')
    project_images = json.loads(project_images_json)
    image_url = request.GET.get('image_url', '')
    contact_number = request.GET.get('contact_number', '')
    contact_email = request.GET.get('contact_email', '')
    linkedin = request.GET.get('linkedin', '')
    github = request.GET.get('github', '')
    
    return render(request, 'template1.html', {
        'name': name,
        'experience': experience,
        'achievements': achievements,
        'skills': skills,
        'project_images': project_images,
        'image_url': image_url,
        'contact_number': contact_number,
        'contact_email': contact_email,
        'linkedin': linkedin,
        'github': github
    })

def template2(request):
    name = request.GET.get('name', '')
    experience = request.GET.get('experience', '')
    achievements = request.GET.get('achievements', '')
    skills_json = request.GET.get('skills', '[]')
    skills = json.loads(skills_json)
    project_images_json = request.GET.get('project_images', '[]')
    project_images = json.loads(project_images_json)
    image_url = request.GET.get('image_url', '')
    contact_number = request.GET.get('contact_number', '')
    contact_email = request.GET.get('contact_email', '')
    
    return render(request, 'template2.html', {
        'name': name,
        'experience': experience,
        'achievements': achievements,
        'skills': skills,
        'project_images': project_images,
        'image_url': image_url,
        'contact_number': contact_number,
        'contact_email': contact_email
    })
def template3(request):
    name = request.GET.get('name', '')
    experience = request.GET.get('experience', '')
    achievements = request.GET.get('achievements', '')
    skills_json = request.GET.get('skills', '[]')
    skills = json.loads(skills_json)
    project_images_json = request.GET.get('project_images', '[]')
    project_images = json.loads(project_images_json)
    image_url = request.GET.get('image_url', '')
    contact_number = request.GET.get('contact_number', '')
    contact_email = request.GET.get('contact_email', '')
    
    return render(request, 'template3.html', {
        'name': name,
        'experience': experience,
        'achievements': achievements,
        'skills': skills,
        'project_images': project_images,
        'image_url': image_url,
        'contact_number': contact_number,
        'contact_email': contact_email
    })

def home(request):
    return render(request, 'home.html')

def collections(request):
    return render(request, 'collections.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Replace 'home' with your home page URL name
    else:
        form = AuthenticationForm()
    print("Login")
    return render(request, 'login.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Replace 'home' with your home page URL name
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})

def logout(request):  # Rename the logout view function
    auth_logout(request)
    return redirect('home')  # Replace 'home' with your home page URL name

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST['email']
        message = request.POST['message']

        # Save the data to the database
        new_message = Message(name=name, email=email, message=message)
        new_message.save()

        print('The data has been written to the db')
        print(name, email, message)

        return HttpResponse("Your message has been sent successfully!")

    return render(request, "contact.html")

def features(request):
    return render(request,'features.html')
def pricing(request):
    return render(request,'pricing.html')