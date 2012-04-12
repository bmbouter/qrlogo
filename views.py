from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
from django.views.static import serve
from django.conf import settings

from forms import ImageForm
from models import Image
from lazy import reverse


class HomeView(TemplateView):
    template_name = "home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)

class MakeView(TemplateView):
    template_name = "make.html"
    success_url = reverse("MakeView")

    def get_context_data(self, **kwargs):
        context = super(MakeView, self).get_context_data(**kwargs)
        images = Image.objects.filter(user=self.request.user)
        context.update({"images": images})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MakeView, self).dispatch(*args, **kwargs)

class ImagesView(CreateView):
    template_name = "images.html"
    form_class = ImageForm
    success_url = reverse("ImagesView")

    def get_context_data(self, **kwargs):
        context = super(ImagesView, self).get_context_data(**kwargs)
        images = Image.objects.filter(user=self.request.user)
        context.update({"images": images})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ImagesView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Image
        user = request.user
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = user
            self.object.save()
            return HttpResponseRedirect(reverse('images_url'))
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_initial(self):
        initial = super(ImagesView, self).get_initial()
        initial = initial.copy()
        initial.update({"images": Image.objects.filter(user=self.request.user)})
        return initial

def ServeImage(request, path, document_root=settings.MEDIA_ROOT, show_indexes=False):
    if request.user.is_authenticated() and not request.user.is_anonymous():
        return serve(request, path, document_root, show_indexes)
    else:
        return HttpResponseForbidden()

@login_required
def DeleteImage(request):
    user = request.user
    image_pk = int(request.POST.get("pk"))
    image = Image.objects.filter(pk=image_pk)
    image.delete()
    return HttpResponse()

@login_required
def PassReset(request):
    if request.method == "GET":
        return render_to_response("passreset.html", {}, context_instance=RequestContext(request))
    else:
        user = request.user
        current_pass = request.POST.get("current")
        new_pass1 = request.POST.get("new1")
        new_pass2 = request.POST.get("new2")
        context = {"success": False, "current_error": False, "new_error": False}

        if user.check_password(current_pass):
            if new_pass1 == new_pass2:
                user.set_password(new_pass1)
                user.save()
                context["success"] = True
            else:
                context["new_error"] = True
        else:
            context["current_error"] = True

        return render_to_response("passreset.html", context, context_instance=RequestContext(request))
