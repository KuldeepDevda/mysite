from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "core/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "core/signup.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class HomeView(CreateView):
    model = Post
    template_name = 'core/home.html'
    form_class = DocumentForm111
    

    def get(self, request, *args, **kwargs):
        form = DocumentForm
        return render(request,'core/home.html', {'form': form})
  
    def post(self, request, *args, **kwargs):
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResonseRedirect(reverse('list-view'))
        else:
            return render(request, 'core/home.html', {'img':img,'form': form})




# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'core/images.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'core/images.html')


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
