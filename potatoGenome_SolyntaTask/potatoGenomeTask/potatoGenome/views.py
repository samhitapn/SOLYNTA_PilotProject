"""
Defining the Django view, rendering a pre-defined html tempate to display the potato Genome database collected

Created_by : Samhita

Created_Date : 02.June.2023
"""

from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
from potatoGenome.models import genomeClass
from potatoGenome.management.commands.getGenomes import Command

def index(request):
    
    # Get all the genome objects (data) created in the run
    genomes = genomeClass.objects.all()
    
    # Get the pre-defined html template to display on the app
    template = loader.get_template("potatoGenome/index.html")
    
    # Define and collect various objects in the run to pass to the html template
    data = {
        # Genome records
        "genomes": genomes,
        
        # Additional variables to avoid hard coding on the html page
        "pTitle_p1" : "https://www.ncbi.nlm.nih.gov/Traces/index.html?view=run_browser&acc=",
        "pTitle_p2" : "&display=data-access"
    }

    return HttpResponse(template.render(data, request))

