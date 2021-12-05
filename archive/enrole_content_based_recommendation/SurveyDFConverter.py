def convertEmployment(dataframe):
    for index, candidate in dataframe.iterrows():
        if isinstance(candidate["Employment"], str):
            if "part-time" in candidate["Employment"]:
                candidate["Employment"] = "part time"
            elif "full-time" in candidate["Employment"]:
                candidate["Employment"] = "full time"
            elif "contractor" in candidate["Employment"]:
                candidate["Employment"] = "contractor"


def convert(dataframe):
    convertEmployment(dataframe)
    print(dataframe.head())