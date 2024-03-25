// Désactiver tous les liens de navigation sauf le premier
const wizardNavLinks = document.querySelectorAll('.nav-link');

//etape general
var importateur = document.getElementById('importateur');
var fournisseur = document.getElementById('fournisseur');
var type = document.getElementById('type');
var have_contrat = document.getElementById('have_contrat');
var ref_contrat = document.getElementById('ref_contrat');
var pays_dest = document.getElementById('pays_dest');
var rel_client = document.getElementById('rel_client');
var num_dossier = document.getElementById('num_dossier');
var motif = document.getElementById('motif');
var date_execution = document.getElementById('date_execution');
var delai_justif = document.getElementById('delai_justif');
var date_limite = document.getElementById('date_limite');
var type_financement = document.getElementById('type_financement');
var num_domiciliation = document.getElementById('num_domiciliation');
var montant_domiciation = document.getElementById('montant_domiciation');
var ref_sgs = document.getElementById('ref_sgs');
var ref_pr = document.getElementById('ref_pr');

//etape financier
var ref_facture = document.getElementById('ref_facture');
var montant_facture = document.getElementById('montant_facture');
var devise_facture = document.getElementById('devise_facture');
var taux_applique = document.getElementById('taux_applique');
var montant_facture_xaf = document.getElementById('montant_facture_xaf');
var facture_definitive = document.getElementById('facture_definitive');
var reference_facture_definitive = document.getElementById('reference_facture_definitive');
var montant_facture_definitive = document.getElementById('montant_facture_definitive');
var montant_transfert = document.getElementById('montant_transfert');
var taux_applique_transfert = document.getElementById('taux_applique_transfert');
var montant_transfert_xaf = document.getElementById('montant_transfert_xaf');
var mt103_202 = document.getElementById('mt103_202');
var date_mt103_202 = document.getElementById('date_mt103_202');
var mt950_mt940 = document.getElementById('mt950_mt940');

//etape douane
var bl = document.getElementById('bl');
var ref_bl = document.getElementById('ref_bl');
var quittance_douane = document.getElementById('quittance_douane');
var ref_quittance_douane = document.getElementById('ref_quittance_douane');
var montant_quittance_douane = document.getElementById('montant_quittance_douane');
var reference_declaration_im4 = document.getElementById('reference_declaration_im4');
var montant_declaration_im4 = document.getElementById('montant_declaration_im4');
var declaration_im4 = document.getElementById('declaration_im4');

//etape apurement
var document_realisation_suivi = document.getElementById('document_realisation_suivi');
var date_previsionnelle_apurement = document.getElementById('date_previsionnelle_apurement');
var statut_apurement = document.getElementById('statut_apurement');
var reference_mise_demeure = document.getElementById('reference_mise_demeure');
var date_mise_demeure = document.getElementById('date_mise_demeure');
var rvc = document.getElementById('rvc');
var document_fournis = document.getElementById('document_fournis');
var document_manquant = document.getElementById('document_manquant');
var observations = document.getElementById('observations');
var controle_beac = document.getElementById('controle_beac');

//etape autre
var contrat_po = document.getElementById('contrat_po');
var bon_declaration = document.getElementById('bon_declaration');
var bon_transport = document.getElementById('bon_transport');
var phy = document.getElementById('phy');


//gerer les coloris des barres
$(document).ready(function() {
    // Lorsqu'un onglet est cliqué
    $('.nav-link').on('click', function() {
        var activeTab = $(this).attr('aria-controls');
        var contentMenu = $('#content-part-menu');
        var contentbar = $('#vert-tabs-tab');
        // Modifier la classe de la div content-part-menu en fonction de l'onglet actif
        if (activeTab === 'vert-tabs-general') {
            contentMenu.css('border-top', '3px solid #105A90');
            contentbar.css('border-right', '2px solid #105A90');
        } else if (activeTab === 'vert-tabs-finance') {
            contentMenu.css('border-top', '3px solid #105A90');
            contentbar.css('border-right', '2px solid #105A90');

        } else if (activeTab === 'vert-tabs-douane') {
            contentMenu.css('border-top', '3px solid #105A90');
            contentbar.css('border-right', '2px solid #105A90');

        } else if (activeTab === 'vert-tabs-apurement') {
            contentMenu.css('border-top', '3px solid #105A90');
            contentbar.css('border-right', '2px solid #105A90');

        } else if (activeTab === 'vert-tabs-autres') {
            contentMenu.css('border-top', '3px solid #105A90');
            contentbar.css('border-right', '2px solid #105A90');
        }
    });
});
