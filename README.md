# Potato Whole Genome Dashboard

This is a dashboard, built using Django, to display the details of potato whole genomes submitted to SRA run selector after 2018.

## Software Requirements

1. Python3
2. Django
3. Django_crontab

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
 
        python3 -m pip install -e /path/to/your/local/clone/django/    #Replace path with the location of the django clone in your local system 

#### Django_crontab

Install the django-crontab via : 
  
    pip install django-crontab

## Installing the SOLYNTA Whole Genome Dashboard application

1. To install the Potato Whole Genome Dashboard, first clone the following repository:

       git clone https://github.com/samhitapn/SOLYNTA_PilotProject.git
    
 2. Go to the following folder:

        cd SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask
    Refer https://pypi.org/project/django-crontab/, for further information on django-crontab.

## Running the SOLYNTA Whole Genome Dashboard application

1. Run the following commands one-by-one:
   
       python manage.py makemigrations
       
       python sqlmigrate potatoGenome 0001

       python manage.py migrate
       
2.  To fetch the necessary data once, run the following command:
 
        python manage.py getGenomes
        
3.  To initiate the database refresh on regular intervals, run the following command:

        python manage.py crontab add
    Currently, running this will initiate a schedule to refresh the database once every 10 mins.
    This frequency of the refresh can be configured by changing the value in the CRONJOBS section of ```~/SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomTask/settings.py``` file.
    
    For further details on how to configure the frequency, please refer to : https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules.
    
    Once you have made any changes to the CRONJOBS, please re-run the crontab before procedding further.
    
        python manage.py crontab add
    
    
4. Finally, to view the application/ dashboard, run the following command:

        python manage.py runserver
    Now you can access the application/ potato whole genome dashboard via :
    
        http://127.0.0.1:8000/potatoGenome
    The app uses DataTables and the example styling provided in : https://datatables.net/examples/data_sources/dom.
    This can be updated by changing the html template provided in ```~/SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/templates/potatoGenome/index.html```
        
 ## Additional instructions
 
 1. To see when the database was recently refreshed, please refer the log file in :
        
        ~/SOLYNTA_PilotProject/potatoGenome_SolyntaTask/logfile.log
   Please point the path to the log file by updating the path to a prefered location in the file ```~/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenomTask/settings.py``` in the filename of the LOGGING section.
   
 2. Change the value to ```Entrez.email``` in ```~/SOLYNTA_PilotProject/potatoGenome_SolyntaTask/potatoGenomeTask/potatoGenome/getPotatoGenomes.py``` to provide your own email for reference to NCBI.
    
