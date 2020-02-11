from django.http import HttpResponse
from django.shortcuts import render
import calendar

def calendarhome(request):
    return render(request,'index.html')

def sendyear(request):
    year = request.GET['year']
    printthis = (calendar.TextCalendar(firstweekday=0).formatyear(int(year)))
    return render(request,'years.html',{'cal':printthis})