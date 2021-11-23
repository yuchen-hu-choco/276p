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
                candidate["YearsCoding"] = 30
            else:
                arr = experience.split()[0].split('-')
                if len(arr) is 2:
                    candidate["YearsCoding"] = str(int((int(arr[0]) + int(arr[1])) / 2))
                else:
                    candidate["YearsCoding"] = "N/A"
        else:
            candidate["YearsCoding"] = "N/A"


def convert(dataframe):
    convertEmployment(dataframe)
    convertEducation(dataframe)
    processExperience(dataframe)
    print(dataframe.head())