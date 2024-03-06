from django.db import models

class Document(models.Model):
    fillale = models.CharField(max_length=255)
    annee_de_reference = models.CharField(max_length=255)
    systeme = models.CharField(max_length=255)
    processus = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    criticite_issue_de_la_cartographie_des_risques = models.CharField(max_length=255)
    annee_theorique_du_dernier_audit = models.CharField(max_length=255)
    annee_de_realisation = models.CharField(max_length=255)
    criticite_issue_de_la_mission_d_audit = models.CharField(max_length=255)
    annee_de_la_prochaine_mission_d_audit = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fillale} - {self.annee_de_reference} - {self.systeme}"