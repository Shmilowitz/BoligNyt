import csv
import os
import sys

from mysite.mysite.bolignyt.models import PythonBolig
from mysite.manage import DEFAULT_SETTINGS_MODULE

project_dir = "/Users/josephawwal/BoligNytFinal/mysite/mysite/bolignyt/py"

sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)

dataReader = csv.reader(open('DBA.csv'), delimiter=',', quotechar='"')

for row in dataReader:
    bolig = PythonBolig()
    bolig.date = row[0]
    bolig.price = row[1]
    bolig.URL = row[2]
    bolig.Description = row[3]
    bolig.save()
