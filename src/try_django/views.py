from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm 
from blog.models import BlogPost

def home_page(request):
	my_title = "Welcome to My Blog"
	qs = BlogPost.objects.all()[:5]
	return render(request, "home.html" , {"title": my_title,"blog_list": qs})


def about_page(request):
	return render(request, "about.html" , {"title": "About Us"})


def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm(None)
	context = {
		"title": "Contact Us",
		"form" : form 
	}
	return render(request, "form.html" , context)


#showing rendering in HttpResponse method
def example_page(request):
	context = {"title": "Example"}
	template_name = "base.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context) 
	return HttpResponse(rendered_item)