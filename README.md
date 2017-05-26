# BoligNyt
BOLIGNYT - App for real estate hunting


![picture alt](http://ambitionplacements.com/wp-content/uploads/2015/06/real-estate-banner.jpg)


Python Exam Project


## Synopsis
Webapp baseret på crawlet bolig data fra DBA. Med hjælp fra Django kan brugeren angive postnummer/pris også foreslår app'en nogle boliger i området. Webscraperen er lavet med Python og konstruktion af webapp med Django.



## Installation
Project is made in Python. It is required to have Python installed.  

Django installation is required to run the Django files.   

`pip install django`  

The scraper also requires some modules to run. Make you that you can import the following modules:  
BeautifulSoup4  `pip install beautifulsoup4`     
Requests        `pip install requests`  
Pandas          `pip install pandas`  
CSV             `pip install csv`  
DateTime        `pip install DateTime`  
Itertools       `pip install itertools`  

The following modules should already be installed by default with Python:  
warnnings  
sys  
fileinput  


## How to 
### The scraper can be run as a standalone component.  
1. Download & navigate to Mainscraper.py's location in terminal  
2. Type`python MainScraper.py` in terminal and scraper will start and print progress.  
3. A file called "DBA.csv" will be created if it's the first time scraper is run. Otherwise new data will be appended to existing DBA.csv file.  

### Django  
1. Download the project and navigate to the folder within your terminal.  
2. Type 'python manage.py runserver' in your terminal.  
3. Server will start at: '127.0.0.1:8000'. You can type in the local-ip within your browser and see the results.  


