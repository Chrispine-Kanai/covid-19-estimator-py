import math

data = {
  "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
  },
  "periodType": "months",
  "timeToElapse": 1,
  "reportedCases": 2747,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}


def estimateData(data):

    impactCurrentlyInfected = data['reportedCases'] * 10
    severeImpactCurrentlyInfected = data['reportedCases'] * 50

    estimate = {
      'impact': {
        'currentlyInfected': impactCurrentlyInfected
      },
      'severeImpact': {
        'currentlyInfected': severeImpactCurrentlyInfected
      }
    }

    return estimate


def normalise_Duration(data):

    if data["periodType"] is "weeks":
        days = data["timeToElapse"] * 7
        return days

    if data["periodType"] is "months":
        days = data["timeToElapse"] * 30
        return days

    if data["periodType"] is "days":
        days = data["timeToElapse"]
        return days


def estimationByRequestedTime(data):

    days = normalise_Duration(data)
    estimateInfectedCases = estimateData(data)


    impactInfectionsByRequestTime = (estimateInfectedCases['impact']['currentlyInfected'] * (2 ** (days // 3)))

    severeImpactInfectionsByRequestTime = estimateInfectedCases['severeImpact']['currentlyInfected'] * (2 ** (days // 3))

    estimateInfectedCasesByTime = {
      'impact': {
        'InfectionsByRequestedTime': impactInfectionsByRequestTime
      },
      'severeImpact': {
        'InfectionsByRequestedTime': severeImpactInfectionsByRequestTime
      }
    }
    
    return estimateInfectedCasesByTime



def estimator(data):

    estimate = estimationByRequestedTime(data)
    estimateInfections = estimateData(data)

    data = {
        'data': data,

        'impact': {
          'currentlyInfected': estimateInfections['impact']['currentlyInfected'],
          'InfectionsByRequestedTime': estimate['impact']['InfectionsByRequestedTime']
        },

        'severeImpact': {
          'currentlyInfected': estimateInfections['severeImpact']['currentlyInfected'],
          'InfectionsByRequestedTime': estimate['severeImpact']['InfectionsByRequestedTime']
        }
    }

    return data


print(estimator(data))
