import math

data = {
  "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
  },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}


def impactInfectionsByRequestTime():
    currentlyInfected = int(data.get("reportedCases") * 10)

    if data["periodType"] == "weeks":
        timeToElapseInDays = data["timeToElapse"] * 7
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime 

    if data["periodType"] == "months":
        timeToElapseInDays = data["timeToElapse"] * 30
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime

    if data["periodType"] == "days":
        factor = math.trunc(data["timeToElapse"] / 3)
        infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))
        return infectionsByRequestedTime 



def severeImpactInfectionsByRequestTime():
    currentlyInfected = int(data.get("reportedCases") * 50)

    if data["periodType"] == "weeks":
        timeToElapseInDays = data["timeToElapse"] * 7
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))
        return infectionsByRequestedTime 

    if data["periodType"] == "months":
        timeToElapseInDays = data["timeToElapse"] * 30
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime

    if data["periodType"] == "days":
        factor = math.trunc(data["timeToElapse"] / 3)
        infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))
        return infectionsByRequestedTime 

def estimator(data):
    data = data

    estimate = {
      'data': data,

      'impact': {
        "currentlyInfected": data["reportedCases"] * 10,
        "infectionsByRequestedTime": impactInfectionsByRequestTime()
      },

      'severeImpact': {
        "currentlyInfected": data["reportedCases"] * 50,
        "infectionsByRequestedTime": severeImpactInfectionsByRequestTime()
      }
    }
    return estimate



print(estimator(data))
