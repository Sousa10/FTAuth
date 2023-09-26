from django.shortcuts import render,  redirect
from django.urls import reverse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from .models import *
from .utils import Calendar
from django.views import generic
from django.utils.safestring import mark_safe


# KMS Generate PDF File Venue List
def venue_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()   
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Designate the Model
    venues = Venue.objects.all()

    # Create blank list
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")

    # Loop through lines
    for line in lines:
        textob.textLine(line)

    # Wrapup
    c.drawText(textob)
    c.showPage()
    c.save()    
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

# KMS Generate .csv File Venue List
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate the Model
    venues = Venue.objects.all()

    # Add column headings
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])
    
    # Loop Through Venues and Write
    for venue in venues:
        writer.writerow([venue.name,venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

    return response

# KMS Generate Text File Venue List
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.text'
    # Designate the Model
    venues = Venue.objects.all()
    # Create a Blank List
    lines = []
    # Loop Through Venues and Write
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')

    response.writelines(lines)
    return response

# KMS delete_venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)    
    venue.delete()
    return redirect('show-venues')

# KMS delete_event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)    
    event.delete()
    return redirect('events-list')

# KMS update_event.html
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)   
    if form.is_valid():
        form.save()  
        return redirect('events-list')       
    return render(request, 'events/update_event.html', {'event': event, 
    'form':form})

# KMS add_event.html
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  
            submitted = True
            # return HttpResponseRedirect('add_venue')
            return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})

# KMS update_venue.html
def update_venue(request, venue_id):
    uvenue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=uvenue)   
    if form.is_valid():
        form.save()  
        return redirect('show-venues')       
    return render(request, 'events/update_venue.html', {'uvenue': uvenue, 
    'form':form})

# KMS search_venues.html
def search_venues(request):
    if request.method == "POST":   
        searchedx = request.POST['searchedx']
        venues = Venue.objects.filter(name__contains=searchedx)
        return render(request, 
        'events/search_venues.html', 
        {'searchedx':searchedx,
         'venues':venues})
    else:
        return render(request, 
        'events/search_venues.html', 
        {})
       
# KMS venue.html    
def venuex(request, venue_id=None):
    if venue_id:
        venue = Venue.objects.get(pk=venue_id)
    else:
        return redirect('show-venue', venue_id = 1)
    return render(request, 'events/venue.html', {'venuex': venue, 
        'nav_venue_id': venue_id or 1})

# KMS show_venues.html
def show_venues(request):
    # venue_list = Venue.objects.all().order_by('name')
    venue_list = Venue.objects.all()

    # Set up Pagination
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "x" * venues.paginator.num_pages
    return render(request, 'events/show_venues.html', 
        {'venue_list': venue_list, 
         'venues': venues, 
         'nums':nums})

# KMS add_venue.html
def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()  
            submitted = True
            # return HttpResponseRedirect('add_venue')
            return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

def events_list(request):
    event_list = Event.objects.all().order_by('event_date', 'name')
    return render(request, 'events/events_list.html', 
        {'event_list': event_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Kirk"
    # Convert any month to all UPPER
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number)
    
    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M %p')

    return render(request, 
        'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time":time,
        })
