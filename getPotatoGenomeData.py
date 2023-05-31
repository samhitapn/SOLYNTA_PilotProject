from Bio import Entrez
import xml.etree.ElementTree as ET

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_xml_parentChild(data, parentKey, childKey):
    for k in data.findall(parentKey):
        value = k.get(childKey)
    return(value)

def get_attribute(data,term):
    value = data[term]
    return(value)

def get_xml_parentText(data,parentKey):
    value = data.find(parentKey).text
    return(value)

Entrez.email="samhitapn.96@gmail.com"

potatoGenomes_list = Entrez.esearch(db="sra", term='"Solanum tuberosum"[Organism] AND "wgs"[Strategy] AND "genomic"[Source] AND "2015"[Publication Date]:"3000"[Publication Date]')

potatoGenomes_dataAll = Entrez.read(potatoGenomes_list)

GENOMES_LIST = []
for i in potatoGenomes_dataAll['IdList']:
     summary = Entrez.esummary(db = "sra",id = i)
     data = Entrez.parse(summary)
     for d in data:
            
            # Genome ID
            ID = i
            
            # Extract information from attributes associated with the genome ID (function call) 
            CREATED_DATE = get_attribute(d,"CreateDate")
            expData = get_attribute(d,"ExpXml")
    
            # Read the XML data and extract necessary data (function call(s)) from Xml attribute extracted above
            expData = '<data>' + expData + '</data>'
            expTree = ET.fromstring(expData)
            SUBMITTER_ACC = get_xml_parentChild(expTree,"Submitter","acc")
            PLATFORM = get_xml_parentChild(expTree,"./Summary/Platform","instrument_model")
            PROJECT_ID = get_xml_parentText(expTree,"Bioproject")
            
            # Check and extract if there is any associated publication to the genome ID via the associated project
            extLinks = Entrez.elink(id = PROJECT_ID,dbfrom = "pubmed",db = "bioproject")
            readLinks = Entrez.read(extLinks)
            if(len(readLinks[0]["LinkSetDb"]) == 0):
                EXTERNAL_LINK = "Not Available"
            else:
                EXTERNAL_LINK = [link["Id"] for link in readLinks[0]["LinkSetDb"][0]["Link"]]
                
            # Save the necessary information collected above
            GENOME = {
                "Genome ID" : ID,
                "Project ID" : PROJECT_ID,
                "Published Date" : CREATED_DATE,
                "Sequencing Platform" : PLATFORM,
                "Associated publication" :  EXTERNAL_LINK
            }
            
            GENOMES_LIST.append(GENOME)
            #print(GENOME)
     
