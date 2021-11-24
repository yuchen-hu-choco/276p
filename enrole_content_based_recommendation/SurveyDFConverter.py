import pycountry

country_list = {'United States', 'Ireland', 'United Kingdom', 'Germany', 'Singapore', 'China', 'Australia', 'Japan', 'India', 'Switzerland', 'France', 'Brazil', 'Mexico', 'Poland', 'Israel', 'Hong Kong', 'Canada', 'Sweden', 'Netherlands', 'Italy'}

def convertEmployment(dataframe):
    for index, candidate in dataframe.iterrows():
        if isinstance(candidate["Employment"], str):
            if "part-time" in candidate["Employment"]:
                candidate["Employment"] = "part time"
            elif "full-time" in candidate["Employment"]:
                candidate["Employment"] = "full time"
            elif "contractor" in candidate["Employment"]:
                candidate["Employment"] = "contractor"
            else:
                candidate["Employment"] = "N/A"
        else:
            candidate["Employment"] = "N/A"

def convertEducation(dataframe):
    for index, candidate in dataframe.iterrows():
        if isinstance(candidate["FormalEducation"], str):
            education = candidate["FormalEducation"].lower()
            if "bachelor" in education:
                candidate["FormalEducation"] = "Bachelor"
            elif "master" in education:
                candidate["FormalEducation"] = "Master"
            elif "doctoral" in education:
                candidate["FormalEducation"] = "Doctor"
            else:
                candidate["FormalEducation"] = "N/A"
        else:
            candidate["FormalEducation"] = "N/A"


def processExperience(dataframe):
    for index, candidate in dataframe.iterrows():
        if isinstance(candidate["YearsCoding"], str):
            experience = candidate["YearsCoding"]
            if experience is "30 or more years" :
                candidate["YearsCoding"] = "more than 10 years"
            else:
                arr = experience.split()[0].split('-')
                if len(arr) is 2:
                    years = int((int(arr[0]) + int(arr[1])) / 2)
                    if years <= 2:
                        candidate["YearsCoding"] = "less than 2 years"
                    elif years <= 4:
                        candidate["YearsCoding"] = "3 - 4 years"
                    elif years <= 7:
                        candidate["YearsCoding"] = "5 - 7 years"
                    elif years <= 10:
                        candidate["YearsCoding"] = "7 - 10 years"
                    else:
                        candidate["YearsCoding"] = "more than 10 years"
                else:
                    candidate["YearsCoding"] = "N/A"
        else:
            candidate["YearsCoding"] = "N/A"


def processCountry(dataframe):
    for index, candidate in dataframe.iterrows():
        if isinstance(candidate["Country"], str):
            res = "N/A"
            for country in pycountry.countries:
                if country.name in candidate["Country"]:
                    res = country.name
                    break
            if res in country_list:
                candidate["Country"] = res
            else:
                candidate["Country"] = "N/A"
        else:
            candidate["Country"] = "N/A"

def convert(dataframe):
    convertEmployment(dataframe)
    convertEducation(dataframe)
    processExperience(dataframe)
    processCountry(dataframe)