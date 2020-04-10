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


def impactInfectionsByRequestTime():
    currentlyInfected = int(data.get("reportedCases") * 10)

    if data["periodType"] == "weeks":
        timeToElapseInDays = data["timeToElapse"] * 7
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime 

    if data.get("periodType") == "months":
        timeToElapseInDays = data["timeToElapse"] * 30
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime

    if data.get("periodType") == "days":
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

    if data.get("periodType") == "months":
        timeToElapseInDays = data["timeToElapse"] * 30
        factor = math.trunc(timeToElapseInDays / 3)
        infectionsByRequestedTime = currentlyInfected * (2 ** factor)
        return infectionsByRequestedTime

    if data.get("periodType") == "days":
        factor = math.trunc(data["timeToElapse"] / 3)
        infectionsByRequestedTime = int(currentlyInfected * (2 ** factor))
        return infectionsByRequestedTime 

def estimator(data):
    _data = data

    return{
      'data': _data,

      'impact': {
        "currentlyInfected": _data.get("reportedCases") * 10,
        "infectionsByRequestedTime": impactInfectionsByRequestTime()
      },

      'severeImpact': {
        "currentlyInfected": data.get("reportedCases") * 50,
        "infectionsByRequestedTime": severeImpactInfectionsByRequestTime()
      }
}


print(estimator(data))
