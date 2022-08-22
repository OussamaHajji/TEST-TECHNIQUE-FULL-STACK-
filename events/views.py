from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Venue
# Import User Model From Django
from django.contrib.auth.models import User
from .forms import VenueForm
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import messages


# Import Pagination Stuff
from django.core.paginator import Paginator


# Show Events In A Venue
def venue_events(request, venue_id):
    # Grab the venue
    venue = Venue.objects.get(id=venue_id)
    # Grab the events from that venue
    events = venue.event_set.all()
    if events:
        return render(request, 'events/venue_events.html', {
            "events": events
        })
    else:
        messages.success(request, ("That Venue Has No Events At This Time..."))
        return redirect('admin_approval')


# Create Admin Event Approval Page


# Generate a PDF File Venue List
def venue_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    # lines = [
    #	"This is line 1",
    #	"This is line 2",
    #	"This is line 3",
    # ]

    # Designate The Model
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

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

# Generate CSV File Venue List





# Generate Text File Venue List
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    # Designate The Model
    venues = Venue.objects.all()

    # Create blank list
    lines = []
    # Loop Thu and output
    for venue in venues:
        lines.append(
            f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')

    # lines = ["This is line 1\n",
    #"This is line 2\n",
    #"This is line 3\n\n",
    # "John Elder Is Awesome!\n"]

    # Write To TextFile
    response.writelines(lines)
    return response

# Delete a Venue


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')


# mis ajour d'un evenement


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None,
                     request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'events/update_venue.html',
                  {'venue': venue,
                   'form': form})




def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)

    # Grab the events from that venue

    return render(request, 'events/show_venue.html',
                  {'venue': venue,
                   'venue_owner': venue_owner
                   })


def list_venues(request):
    #venue_list = Venue.objects.all().order_by('?')
    venue_list = Venue.objects.all()

    # Set up Pagination
    p = Paginator(Venue.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    return render(request, 'events/event.html',
                  {'venue_list': venue_list,
                   'venues': venues,
                   'nums': nums}
                  )


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id  # logged in user
            venue.save()
            # form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
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

    # Query the Events Model For Dates

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
                      "time": time,

                  })

'''
def all_venues(request):
    #venue_list = Venue.objects.all().order_by('?')
    venue_list = Venue.objects.all()

    # Set up Pagination
    p = Paginator(Venue.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages

    return JsonResponse(venue_list)
'''