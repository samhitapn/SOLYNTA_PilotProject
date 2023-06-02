"""
Defining the various model classes used in the app

Created_by : Samhita

Created_Date : 02.June.2023
"""

# Import necessary modules
from django.db import models
import xml.etree.ElementTree as ET

# Class to define the various fields and functions necessary for usage in the app
class genomeClass(models.Model):
    genome_Id = models.CharField(max_length=200)
    project_Title = models.CharField(max_length=500)
    run_Id = models.CharField(max_length=200)
    published_Date = models.DateField()
    sequencing_Platform = models.TextField()
    publication_Link = models.URLField()
    
    # FUNCTIONS
    #1. To parse and retrieve the child information given the parent from Entrez xml results
    def get_xml_parentChild(data, parentKey, childKey):
        for k in data.findall(parentKey):
            value = k.get(childKey)
        return(value)
    
    #2. Extracts the value given the key from Entrez results
    def get_attribute(data,term):
        value = data[term]
        return(value)
    
    #3. To generate a proper xml structure from the initial Entrez results for further parsing
    def get_xml(xmlData):
        att = '<data>' + xmlData + '</data>'
        att = ET.fromstring(att)
        return(att)
    
    #4. To parse and retrieve the text information given the parent from Entrez xml results
    def get_xml_parentText(data,parentKey):
        value = data.find(parentKey).text
        return(value)