import csv, sys, os
project_dir = "/Users/josephawwal/BoligNytFinal/mysite/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'




from mysite.bolignyt.models import PythonBolig
data = csv.reader(open("/Users/josephawwal/BoligNytFinal/mysite/mysite/bolignyt/DBA.csv", encoding='Cp1252'), delimiter=",")

for row in data:
    if row[0] != 'date_found':
        bolig = PythonBolig()
        bolig.date_Found = row[0]
        bolig.Price = row[1]
        bolig.Url = row[2]
        bolig.Description = row[3]
        bolig.save()
