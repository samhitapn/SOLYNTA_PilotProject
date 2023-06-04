"""
Defining a Django custom command to call the getPotatoGenomes.py to fetch the requred potato genome data

Created_by : Samhita

Created_Date : 02.June.2023
"""

# Import necessary modules

from django.core.management.base import BaseCommand
from potatoGenome.models import genomeClass
from potatoGenome.getPotatoGenomes import getGenomeData

from datetime import datetime

#import logging

#logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Fetches the potato whole genomes and their (meta)data posted after 2018"
        
    def handle(self, *args, **kwargs):
        
        #start = datetime.now()
        #logger.info("\n################# RUN getGenomes Command #################\n")
        #logger.info(f"The Run Started at : {start}")
        
        getGenomeData()
        
        #end = datetime.now()
        #logger.info(f"The Run Ended at : {end}")
        
        #rt = end - start
        #run_time = rt.total_seconds()
        
        #logger.info(f"The Run took : {run_time} seconds to extract the data")
        #logger.info("\n#################\n")

            
            
