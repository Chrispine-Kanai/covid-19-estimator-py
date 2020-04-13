import math
import sys
        
data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 4,
        "avgDailyIncomePopulation": 0.73
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 92931687,
    "totalHospitalBeds": 678874
}


def impactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 10

    infectionsByRequestedTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestedTime)

    hospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - severeCasesByRequestedTime)

    casesForICUByRequestedTime = int(0.05 * infectionsByRequestedTime)

    casesForVentilatorsByRequestedTime = int(0.02 * infectionsByRequestedTime)

    dollarsInFlight = math.trunc((infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) // days)

    return [currentlyInfected, infectionsByRequestedTime, severeCasesByRequestedTime, hospitalBedsByRequestedTime, casesForICUByRequestedTime, casesForVentilatorsByRequestedTime, dollarsInFlight]


def severeImpactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 50

    infectionsByRequestedTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestedTime)

    hospitalBedsByRequestedTime = math.trunc((0.35 * data['totalHospitalBeds']) - severeCasesByRequestedTime)

    casesForICUByRequestedTime = int(0.05 * infectionsByRequestedTime)

    casesForVentilatorsByRequestedTime = int(0.02 * infectionsByRequestedTime)

    dollarsInFlight = math.trunc((infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) // days)

    return [currentlyInfected, infectionsByRequestedTime, severeCasesByRequestedTime, hospitalBedsByRequestedTime, casesForICUByRequestedTime, casesForVentilatorsByRequestedTime, dollarsInFlight]


def normalise_Duration(data):

    if data["periodType"] == "weeks":
        return data["timeToElapse"] * 7
        
    if data["periodType"] == "months":
        return data["timeToElapse"] * 30

    if data["periodType"] == "days":
        return data["timeToElapse"]


def estimator(data):

    impactCases = impactEstimations(data)
    severeImpact = severeImpactEstimations(data)

    data = {
        'data': data,

        'impact': {
            'currentlyInfected': impactCases[0] ,
            'infectionsByRequestedTime': impactCases[1],
            'severeCasesByRequestedTime': impactCases[2],
            'hospitalBedsByRequestedTime': impactCases[3],
            'casesForICUByRequestedTime': impactCases[4],
            'casesForVentilatorsByRequestedTime': impactCases[5],
            'dollarsInFlight': impactCases[6],
        },

        'severeImpact': {
            'currentlyInfected': severeImpact[0],
            'infectionsByRequestedTime': severeImpact[1],
            'severeCasesByRequestedTime': severeImpact[2],
            'hospitalBedsByRequestedTime': severeImpact[3],
            'casesForICUByRequestedTime': severeImpact[4],
            'casesForVentilatorsByRequestedTime': severeImpact[5],
            'dollarsInFlight': severeImpact[6],
        }
    }

    return data

print(estimator(data))
