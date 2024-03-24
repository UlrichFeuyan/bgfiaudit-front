import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def documents(request):
    documents_active = 'True'
    dropdown_document = 'True'
    liste_document_active = 'True'
    header_title= "Liste des documents"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'documents',
            },
            {
                'name': 'liste des documents',
            },
        ]
    return render(request, 'services/documents/documents.html', locals())

def list_documents(request):
    get_data = requests.get(listedocument)
    data_list = get_data.json()
    return render(request, "services/documents/list_documents.html", locals())

def edit_documents(request, pk):
    get_famillerisk = requests.get(f"{listedocument}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        titre_doc = request.POST.get('titre_doc')
        ref_document = request.POST.get('ref_document')
        # Données à envoyer dans la requête POST
        data = {
                "titre_doc": titre_doc,
                "ref_document": ref_document,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listedocument}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/documents/form_documents.html", locals())

def add_documents(request):
    if request.method == "POST":
        titre_doc = request.POST.get('titre_doc')
        ref_document = request.POST.get('ref_document')
        # Données à envoyer dans la requête POST
        data = {
                "titre_doc": titre_doc,
                "ref_document": ref_document,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listedocument}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/documents/form_documents.html", locals())

def del_documents(request, pk):
    get_famillerisk = requests.get(f"{listedocument}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listedocument}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/documents/del_documents.html", locals())
