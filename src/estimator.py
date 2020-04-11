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
    "population": 92931687,
    "totalHospitalBeds": 678874
}

def impactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 10

    infectionsByRequestTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestTime)

    hospitalBedsByRequestedTime = math.trunc(0.35 * data['totalHospitalBeds']) - severeCasesByRequestedTime + 1

    return [currentlyInfected, infectionsByRequestTime, severeCasesByRequestedTime, hospitalBedsByRequestedTime]


def severeImpactEstimations(data):

    days = normalise_Duration(data)

    currentlyInfected = data['reportedCases'] * 50

    infectionsByRequestTime = math.floor(currentlyInfected * (2 ** (days // 3)))

    severeCasesByRequestedTime = math.floor(0.15 * infectionsByRequestTime)

    hospitalBedsByRequestedTime = math.trunc(0.35 * data['totalHospitalBeds']) - severeCasesByRequestedTime + 1

    return [currentlyInfected, infectionsByRequestTime, severeCasesByRequestedTime, hospitalBedsByRequestedTime]


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
        },

        'severeImpact': {
            'currentlyInfected': severeImpact[0],
            'infectionsByRequestedTime': severeImpact[1],
            'severeCasesByRequestedTime': severeImpact[2],
            'hospitalBedsByRequestedTime': severeImpact[3],
        }
    }

    return data

print(estimator(data))