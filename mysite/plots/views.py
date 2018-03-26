from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from plots.forms import CreateNewPlotForm

class CreateNewPlotView(TemplateView):
    template_name = 'plots/new_plot.html'

    def get(self, request):
        form = CreateNewPlotForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateNewPlotForm(request.POST)
        if form.is_valid():
            plot = form.save(commit=False)
            plot.user = request.user
            form.save()
            return redirect('/plots/create')

        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)

class PlotView(TemplateView):
    template_name = 'accounts/home.html'
