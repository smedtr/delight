# Zie https://stackoverflow.com/questions/70768547/how-to-pass-date-and-id-through-url-in-django
# In de URL zit een date field die we gebruiken in de query
# 
from datetime import date, datetime

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)