from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListHeaderTForm, ListDetailsTForm, ListHeaderSelectForm, ListHeaderTForm, ListDetailsTForm
from .models import ListHeaderT, ListDetailsT
from django.core.paginator import Paginator
from LoginRegister.utils import increment_click_count

import logging
from django.http import HttpResponseServerError

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'listsplan/main_landing_page.html', {})

def main_landing_page(request):
    click_count = increment_click_count('listsplan')
    firs_listHeader = ListHeaderT.objects.first()
    return render(request, 'listsplan/main_landing_page.html', {
        'firs_listHeader': firs_listHeader,
        'click_count': click_count,
    })

def FTListChores(request, listheader_id=None):
    # listheader = None
    firs_listHeader = ListHeaderT.objects.first()
    if listheader_id:
        listheader = ListHeaderT.objects.get(id=listheader_id)
        listdetails = ListDetailsT.objects.filter(ListHeaderFK=listheader)
        # Show 10 ListDetailsT objects per page
        paginator = Paginator(listdetails, 2)
        # get page number for each ListHeaderT instance
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
    else:
        listdetails = None
        page = None

    listHeaderForm = ListHeaderTForm()
    selected_header = ListHeaderT.objects.get(id=listheader_id)
    listDetailForm = ListDetailsTForm(list_header=selected_header)
    selectedHeaderForm = ListHeaderSelectForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'ListHeaderTForm':
            listHeaderForm = ListHeaderTForm(request.POST)
            if listHeaderForm.is_valid():
                listHeaderForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'ListDetailsTForm':
            listDetailForm = ListDetailsTForm(request.POST)
            if listDetailForm.is_valid():
                listDetailForm.save()

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

        elif form_type == 'SelectedHeaderTForm':
            selectedHeaderForm = ListHeaderSelectForm(request.POST)
            if selectedHeaderForm.is_valid():
                listheaderName = selectedHeaderForm.cleaned_data['LHName']
                listheader = ListHeaderT.objects.get(LHName=listheaderName)
                listdetails = listheader.listdetailst_set.all()
                # Show 10 ListDetailsT objects per page
                paginator = Paginator(listdetails, 5)
                # get page number for each ListHeaderT instance
                page_number = request.GET.get('page', 1)
                page = paginator.get_page(page_number)
                print(type(listheader.id))

                return redirect('listsplan:FTListChores', listheader_id=listheader.id)

    else:
        listHeaderForm = ListHeaderTForm()
        selected_header = ListHeaderT.objects.get(id=listheader_id)
        listDetailForm = ListDetailsTForm(list_header=selected_header)
    return render(request, 'listsplan/FTListChores.html', {
        'listHeaderForm': listHeaderForm,
        'firs_listHeader': firs_listHeader,
        'listDetailForm': listDetailForm,
        'selectedHeaderForm': selectedHeaderForm,
        'listheader': listheader,
        'listdetails': page,
        'title': 'List and Chores',
    })


def listHeader_update(request, pk):
    listHeader = get_object_or_404(ListHeaderT, pk=pk)
    if request.method == 'POST':
        form = ListHeaderTForm(request.POST, instance=listHeader)

        if form.is_valid():
            form.save()
            return redirect('listsplan:FTListChores', listheader_id=listHeader.id)
    else:
        form = ListHeaderTForm(instance=listHeader)
    return render(request, 'FTListChores.html', {
        'form': form,
        'listHeader': listHeader,
        'title': 'Edit Header',
    })


def listDetail_update(request, pk):
    listDetail = get_object_or_404(ListDetailsT, pk=pk)
    if request.method == 'POST':
        form = ListDetailsTForm(request.POST, instance=listDetail)

        if form.is_valid():
            form.save()
            return redirect('listsplan:FTListChores', listheader_id=listDetail.ListHeaderFK.id)
        else:
             # Log form errors
            logger.error(form.errors)
            # Print form errors to the console (for development purposes)
            print(form.errors)
            return HttpResponseServerError("Form is not valid. See server logs for details.")
    else:
        form = ListDetailsTForm(instance=listDetail)
    return render(request, 'listsplan/FTListChores.html', {
        'form': form,
        'listHeader': listDetail,
        'title': 'Edit List Detail',
    })


def listHeader_delete(request, pk):
    listHeader = get_object_or_404(ListHeaderT, pk=pk)
    listHeader.delete()

    return redirect('listsplan:FTListChores', listheader_id=listHeader.id)


def listDetail_delete(request, pk):
    listDetail = get_object_or_404(ListDetailsT, pk=pk)
    listDetail.delete()

    return redirect('listsplan:FTListChores', listheader_id=listDetail.ListHeaderFK.id)
