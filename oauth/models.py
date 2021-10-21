from django.db import models

class XMLmodel(models.Model):
    email_of_user = models.TextField(null=True)
    XMLlist = models.TextField(null=True)

    def set_xml(self, xml):
        self.XMLlist = xml
    
    def get_xml(self):
        return self.XMLlist