# Todo
import pycountry
import re
import spacy
from spacy.matcher import Matcher
from monkeylearn import MonkeyLearn

model_id = "ex_Z4hc5c5z"
key = "e2374b955eee542d869c74f4bb89018a199583a5"


# convert to [['Country', 'FormalEducation', 'YearsCoding', 'CompanySize', 'Employment']]
def preProcessColumn(dataframe):
    # df.rename(columns={"A": "a", "B": "c"})
    len = dataframe.shape[0]
    dataframe.rename(columns={"Location": "Country"}, inplace=True)
    dataframe.insert(dataframe.shape[1], "FormalEducation", ["N/A"] * len, True)
    dataframe.insert(dataframe.shape[1], "YearsCoding", ["N/A"] * len, True)
    dataframe.insert(dataframe.shape[1], "Employment", ["N/A"] * len, True)


def processCountry(dataframe):
    for index, job in dataframe.iterrows():
        res = "N/A"
        for country in pycountry.countries:
            if country.name in job["Country"]:
                res = country.name
                break
        job["Country"] = res

def processEmployment(dataframe):
    for index, job in dataframe.iterrows():
        if isinstance(job["employmenttype_jobstatus"], str):
            employment = job["employmenttype_jobstatus"].lower()
            if "parttime" in employment or "part time" in employment or "part-time" in employment:
                job["Employment"] = "part time"
            elif "contractor" in employment:
                job["Employment"] = "contractor"
            elif "fulltime" in employment or "full time" in employment or "full-time" in employment:
                job["Employment"] = "full time"


def processEducation(dataframe):
    for index, job in dataframe.iterrows():
        if isinstance(job["jobdescription"], str):
            description = job["jobdescription"].lower().split()
            bs_list = ["bs", "b.s.", "bachelor", "bachelor's", "ba", "b.a."]
            ms_list = ["ms", "m.s.", "master", "master's", "m.a."]
            phd_list = ["doctor", "phd", "doctoral"]
            proceed = True
            for bs in bs_list:
                if bs in description:
                    job["FormalEducation"] = "Bachelor"
                    proceed = False

            if proceed:
                for ms in ms_list:
                    if ms in description:
                        job["FormalEducation"] = "Master"
                        proceed = False

            if proceed:
                for phd in phd_list:
                    if phd in description:
                        job["FormalEducation"] = "Doctor"
                        proceed = False

            if proceed:
                if "graduate" in description:
                    job["FormalEducation"] = "Master"
                elif "degree" in description:
                    job["FormalEducation"] = "Bachelor"


def processExperience(dataframe):
    for index, job in dataframe.iterrows():
        if isinstance(job["jobdescription"], str):
            description = job["jobdescription"].lower()
            pos = [m.start() for m in re.finditer('year', description)]
            if len(pos) == 0:
                continue
            min_value = None
            for end in pos:
                start = end - 1
                while start > 0 and description[start] != '.' and description[start] != ';':
                    start -= 1

                num = None
                while start < end:
                    if description[start].isdigit():
                        if num is None:
                            num = ""
                        num += description[start]
                        start += 1
                    elif num is None:
                        start += 1
                        continue
                    else:
                        break
                if num is not None:
                    if min_value is not None:
                        if int(num) < int(min_value):
                            min_value = num
                    else:
                        min_value = num
            if min_value is not None:
                job["YearsCoding"] = min_value



def convert(dataframe):
    preProcessColumn(dataframe)
    processCountry(dataframe)
    processEmployment(dataframe)
    processEducation(dataframe)
    processExperience(dataframe)
    dataframe.drop(['employmenttype_jobstatus', 'jobdescription'], axis=1, inplace=True)
    print(dataframe)
    return dataframe
