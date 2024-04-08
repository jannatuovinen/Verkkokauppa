from django.views.generic import ListView

from kauppa.models import Tuote

class TuoteListaNäkymä(ListView):
    model = Tuote

# Create your views here.
