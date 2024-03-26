import django_tables2 as tables
from .models import Document

class PlanAuditTable(tables.Table):
    class Meta:
        model = Document
        template_name = "django_tables2/bootstrap.html"
        fields = ("fillale", "annee_de_reference", "systeme", "processus", "site", "criticite_issue_de_la_cartographie_des_risques", "annee_theorique_du_dernier_audit", "annee_de_realisation", "criticite_issue_de_la_mission_d_audit", "annee_de_la_prochaine_mission_d_audit", )