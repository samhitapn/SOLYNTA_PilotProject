"""
Python function to retrieve the necessary potato genome data from SRA run selector using Entrez from biopython

Created_by : Samhita

Created_Date : 02.June.2023
"""

from Bio import Entrez
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from potatoGenome.models import genomeClass
from potatoGenome.models import genomeClass as gc
from datetime import datetime

def getGenomeData():
    Entrez.email="example@gmail.com" # Please change your email id here
    
    # Get the list of all potato whole genomes submitted after 2018
    query = '"Solanum tuberosum"[Organism] AND "wgs"[Strategy] AND "genomic"[Source] AND "2018"[Publication Date]:"3000"[Publication Date]'
    potatoGenomes_list = Entrez.esearch(db = "sra",
                                        term = query)
    potatoGenomes_dataAll = Entrez.read(potatoGenomes_list)
    
    # Initialise array to collect all the genomes
    GENOMES_LIST = []

    # Get all the necessary data for all the resulting genomes filtered 
    for i in potatoGenomes_dataAll['IdList']:
         summary = Entrez.esummary(db = "sra",id = i)
         data = Entrez.parse(summary)
         for d in data:

                # Genome ID
                ID = i

                # Extract required metadata information from attributes associated with the genome ID (function call) 
                CREATED_DATE = gc.get_attribute(d,"CreateDate")
                CREATED_DATE = CREATED_DATE.replace("/","-")

                # Extract the sequencing platform details
                expData = gc.get_attribute(d,"ExpXml")
                expTree = gc.get_xml(expData)
                SUBMITTER_ACC = gc.get_xml_parentChild(expTree,"Submitter","acc")
                PLATFORM = gc.get_xml_parentChild(expTree,"./Summary/Platform","instrument_model")
                TITLE = gc.get_xml_parentText(expTree,"./Summary/Title")
                PROJECT_ID = gc.get_xml_parentText(expTree,"Bioproject")

                # Check and extract if there is any associated publication to the genome ID via the associated project
                extLinks = Entrez.elink(id = PROJECT_ID,dbfrom = "pubmed",db = "bioproject")
                readLinks = Entrez.read(extLinks)
                if(len(readLinks[0]["LinkSetDb"]) == 0):
                    EXTERNAL_LINK = "Not Available"
                else:
                    EXTERNAL_LINK = [link["Id"] for link in readLinks[0]["LinkSetDb"][0]["Link"]]

                # Extract the run accession for sequence
                runData = gc.get_attribute(d,"Runs")
                runTree = gc.get_xml(runData)
                RUN_ACC = gc.get_xml_parentChild(runTree,"Run","acc")

                # Save the necessary information collected above to the genomeClass object  
                # This adds new records, if any, to the existing database. Distinct records are identified by genome_Id
                if not gc.objects.filter(genome_Id=ID).exists():
                    # Create a new record
                   
                    gc.objects.create(
                        genome_Id = ID,
                        project_Title = TITLE,
                        run_Id = RUN_ACC,
                        published_Date = CREATED_DATE,
                        sequencing_Platform = PLATFORM,
                        publication_Link = EXTERNAL_LINK
                    )
    return()

