# Potato Whole Genome Dashboard

This is a dashboard, built using Django, to display the details of potato whole genomes submitted to SRA run selector after 2018.

## Software Requirements

1. Python3
2. Django
3. Django_crontab
4. Biopython

## Software Installations
#### Python3

To download and install Python3 please refer to https://www.python.org/downloads/

#### Django

To download and install Django, follow the instructions detailed in this page based on your operating system : https://docs.djangoproject.com/en/4.2/topics/install/.

 or follow the following steps (via terminal for creating a virtual environment on unix based operating systems or Mac):
 
 1. Clone the git repositry 
            
         git clone https://github.com/django/django.git
  
 2. Create a virtual environment

         python3 -m venv ~/.virtualenvs/django
         
 3. Activate the virtual environment created above
         
         source ~/.virtualenvs/django/bin/activate
         
 4. Install the previously cloned django git repository
 
        python -m pip install -e /path/to/your/local/clone/django/    #Replace path with the location of the django clone in your local system 

#### Django_crontab

Install the django-crontab via : 
  
    pip install django-crontab
   Refer https://pypi.org/project/django-crontab/, for further information on django-crontab.
    
#### Biopython

Install Biopython via : 
 
    pip install biopython

## Installing the SOLYNTA Whole Genome Dashboard application

1. To install the Potato Whole Genome Dashboard, first clone the following repository:

       git clone https://github.com/samhitapn/SOLYNTA_PilotProject.git

## Running the Potato Whole Genome Dashboard application

1. Change the value of ```Entrez.email``` in ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/getPotatoGenomes.py``` to provide your own email for reference to NCBI.  

       def getGenomeData():
              Entrez.email="example@gmail.com" ### Change the email id here to your own
2. Navigate to the folder:

        cd SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask
        
3. Run the following commands one-by-one:
   
       python manage.py makemigrations

       python manage.py migrate

4. To view the application/ dashboard, run the following command:

        python manage.py runserver
    Now you can view the application/ potato whole genome dashboard via :
    
        http://127.0.0.1:8000/potatoGenome
        
    Note: The app uses DataTables and the example styling provided in : https://datatables.net/examples/data_sources/dom.
    This can be configured by changing the html template in ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/templates/potatoGenome/index.html```
    
5. The dashboard is currently set to be refreshed every 10 minutes. Every time the database is refreshed, its details are logged into the log file you pointed to above.

   The frequency of the refresh can be configured per your need by following the below steps : 
    
    i.  Open the file ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenomeTask/settings.py``` in an editor.
    
    ii. Change the value of ```*/10 * * * *``` in the CRONJOBS section as necessary.
           
           CRONJOBS = [
            ('*/10 * * * *', 'django.core.management.call_command', ['getGenomes'])
           ]
      For further details on how to configure this frequency, please refer to : https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules.
    
    iii. Once you have made the changes, please re-run the below command:
    
        python manage.py crontab add
