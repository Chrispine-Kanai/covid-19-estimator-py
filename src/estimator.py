import math

data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 5,
        "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 38,
    "reportedCases": 2747,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}

def impactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 10

    infectionsByRequestTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestTime)

    return [currentlyInfected, infectionsByRequestTime, severeCasesByRequestedTime]


def severeImpactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 50

    infectionsByRequestTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestTime)

    return [currentlyInfected, infectionsByRequestTime, severeCasesByRequestedTime]


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
        },

        'severeImpact': {
            'currentlyInfected': severeImpact[0],
            'infectionsByRequestedTime': severeImpact[1],
            'severeCasesByRequestedTime': severeImpact[2],
        }
    }

    return data
