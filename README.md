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
    
 2. Navigate to the folder:

        cd SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask

## Running the Potato Whole Genome Dashboard application

1. Run the following commands one-by-one:
   
       python manage.py makemigrations
       
       python manage.py sqlmigrate potatoGenome 0001

       python manage.py migrate
    
2. The dashboard is currently set to be refreshed every 10 minutes. 
   The frequency of the refresh can be configured per your need by following the below steps : 
    
    i.  Open the file ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomTask/settings.py``` in an editor
    ii. Change the value of ```*/10 * * * *``` in the CRONJOBS section as necessary.
           
           CRONJOBS = [
            ('*/10 * * * *', 'django.core.management.call_command', ['getGenomes'])
           ]
      For further details on how to configure this frequency, please refer to : https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules.
    iii. Once you have made the changes, please re-run the below command:
    
        python manage.py crontab add
        
3. Finally, to view the application/ dashboard, run the following command:

        python manage.py runserver
    Now you can access the application/ potato whole genome dashboard via :
    
        http://127.0.0.1:8000/potatoGenome
        
    Note: The app uses DataTables and the example styling provided in : https://datatables.net/examples/data_sources/dom.
    This can be configured by changing the html template in ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/templates/potatoGenome/index.html```
        
 ## Additional instructions
 
 1. Change the value of ```Entrez.email``` in ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/getPotatoGenomes.py``` to provide your own email for reference to NCBI.

 2. To see when the database was recently refreshed, please refer the log file in :
        
        SOLYNTA_PilotProject/potatoGenome_SolyntaTask/logfile.log
   To change the path of the log file, please point to the desired location by updating the path by :
   i. Open the file ```SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenomTask/settings.py```.
   ii. Update the ```filename``` attribute to the desired location of the LOGGING section
   
      LOGGING = {
         'version': 1,
         'disable_existing_loggers': False,
         'handlers': {
             'file': {
                 'level': 'INFO',
                 'class': 'logging.FileHandler',
                 'filename': 'SOLYNTA_PilotProject/potatoGenome_SolyntaTask/logfile.log',  # Specify the path to your log file
             },
         },
         'root': {
             'handlers': ['file'],
             'level': 'INFO',
         },
     }
    
 3. Source the virtual environment whwile running the app every time via:
 
        source ~/.virtualenvs/django/bin/activate
