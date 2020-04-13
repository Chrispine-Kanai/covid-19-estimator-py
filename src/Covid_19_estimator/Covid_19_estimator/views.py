from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys
from django.template.context import RequestContext
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):

    return render(request,'index.html')


def estimator(request):


    name = request.POST.get('data-name')
    avgAge = request.POST.get('data-avg-Age')
    avgDailyIncomeInUSD = request.POST.get('data-avg-daily-income-in-USD')
    avgDailyIncomePopulation = request.POST.get('data-avg-daily-income-population')

    periodType = request.POST.get('data-period-type')
    timeToElapse = request.POST.get('data-time-to-elapse')
    reportedCases = request.POST.get('data-reported-cases')
    population = request.POST.get('data-population')
    totalHospitalBeds = request.POST.get('data-total-hospital-beds')
    

    output = run([sys.executable, os.path.join(BASE_DIR, 'estimator.py'), name, avgAge, avgDailyIncomeInUSD, avgDailyIncomePopulation, periodType, timeToElapse, reportedCases, population, totalHospitalBeds],shell=False,stdout=PIPE, text=True)
    print(output)
    return render(request,'index.html', {'data': output.stdout})

