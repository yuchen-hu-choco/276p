import pandas as pd
import GraphMaker
import DFConverter
import DataCleaner


def create_candidate_dataframe(path):
    survey = pd.read_csv(path)
    pd.options.display.max_columns = None

    dataframe = survey[['Country', 'FormalEducation', 'YearsCoding', 'CompanySize', 'Employment']]
    print("Dataframe created successfully from", path, ". Number of rows: ", dataframe.shape[0]);
    return dataframe


def create_job_dataframe(path):
    survey = pd.read_csv(path)
    pd.options.display.max_columns = None

    dataframe = survey[['Location', 'employmenttype_jobstatus', 'jobdescription']]
    print("Dataframe created successfully from", path, ". Number of rows: ", dataframe.shape[0]);
    # Todo
    return DFConverter.convert(dataframe)


def createGraphs(dataframe):
    GraphMaker.plot_empty_rate(dataframe)
    GraphMaker.plot_country(dataframe)
    GraphMaker.plot_experience(dataframe)
    GraphMaker.plot_education(dataframe)
    GraphMaker.plot_company_size(dataframe)
    GraphMaker.ploy_employment(dataframe)


def main():
    candidate_dataframe = create_candidate_dataframe('survey.csv')
    job_dataframe = create_job_dataframe('jobs.csv')
    createGraphs(candidate_dataframe)
    DataCleaner.clean_dataframe(candidate_dataframe)
    DataCleaner.clean_dataframe(job_dataframe)


main()
