import csv, sys, os

from mysite.mysite.bolignyt.models import PythonBolig
from mysite.manage import DEFAULT_SETTINGS_MODULE



project_dir = "/Users/josephawwal/BoligNytFinal/mysite/"

sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)




data = csv.reader(open("/Users/josephawwal/BoligNytFinal/mysite/mysite/bolignyt/DBA.csv", encoding='Cp1252'), delimiter=",")

for row in data:
    if row[0] != 'date_found':
        bolig = PythonBolig()
        bolig.date_found = "lort"
        bolig.Price = "lort"
        bolig.Url = "lort"
        bolig.Description = "lort"
        bolig.save()
