import json
import requests
from ..decorators import *
from django.contrib import messages
from apiRessource.endpointList import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


def categories_de_documents(request):
    dropdown_document = 'True'
    categorie_document_active = 'True'
    header_title= "Catégories de document"
    breadcrumb = [
            {
                'name': 'Accueil',
                'path': reverse('services:home_superAdmin'),
            },
            {
                'name': 'documents',
            },
            {
                'name': 'catégories de document',
            },
        ]
    return render(request, 'services/categories_de_documents/categories_de_documents.html', locals())

def list_categories_de_documents(request):
    get_data = requests.get(listecategoriedoc)
    data_list = get_data.json()
    return render(request, "services/categories_de_documents/list_categories_de_documents.html", locals())

def edit_categories_de_documents(request, pk):
    get_famillerisk = requests.get(f"{listecategoriedoc}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        code_categorie = request.POST.get('code_categorie')
        lib_categorie = request.POST.get('lib_categorie')
        # Données à envoyer dans la requête POST
        data = {
                "code_categorie": code_categorie,
                "lib_categorie": lib_categorie,
                }
        # Faire une requête POST à l'API
        response = requests.put(f"{listecategoriedoc}{pk}/", data=data)
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "ListChanged": None,
                    "showMessage": f"famille de risque N°Modifié."
                })
            }
        )
    return render(request, "services/categories_de_documents/form_categories_de_documents.html", locals())

def add_categories_de_documents(request):
    if request.method == "POST":
        code_categorie = request.POST.get('code_categorie')
        lib_categorie = request.POST.get('lib_categorie')
        # Données à envoyer dans la requête POST
        data = {
                "code_categorie": code_categorie,
                "lib_categorie": lib_categorie,
                }
        # Faire une requête POST à l'API
        response = requests.post(f"{listecategoriedoc}", data=data)
        return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "ListChanged": None,
                        "showMessage": f"Enregistrement ajouter."
                    })
                }
            )
    return render(request, "services/categories_de_documents/form_categories_de_documents.html", locals())

def del_categories_de_documents(request, pk):
    get_famillerisk = requests.get(f"{listecategoriedoc}{pk}")
    data = get_famillerisk.json()
    if request.method == "POST":
        response = requests.delete(f"{listecategoriedoc}{pk}")
        return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "ListChanged": None,
                "showMessage": f"enregistrement Supprimé."
            })
        })
    return render(request, "services/categories_de_documents/del_categories_de_documents.html", locals())
