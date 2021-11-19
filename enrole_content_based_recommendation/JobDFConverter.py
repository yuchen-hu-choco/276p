# Todo
import pycountry
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
    dataframe.insert(dataframe.shape[1], "CompanySize", ["N/A"] * len, True)
    dataframe.insert(dataframe.shape[1], "Employment", ["N/A"] * len, True)


def processCountry(dataframe):
    for index, job in dataframe.iterrows():
        for country in pycountry.countries:
            if country.name in job["Country"]:
                job["Country"] = country.name
                break


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


def extract():
    data = ["Looking for Selenium engineers...must have solid java coding skills I have several openings some 3 month to hire some 6...must be able to go PERM  This can be someone with 0-5 years of experience. Most important qualities are Eagerness and Aptitude. POSITION PURPOSE - Do you want to be on the forefront of cutting edge technology, introduce solutions to problems that didn’t exist before, and have the ability to see the result of your successes? Our client assures growth by collaborating with development teams and creating tools that aid engineers in building, testing, debugging, and releasing software. We touch millions of users by increasing the rate of development and ensuring our products are methodically tested. We are experts in software health, testability, and sustainability. As a Software Engineer in Test at our client, you can expect to build flexible and scalable solutions while working on some of the most complex challenges in large-scale computing by utilizing your skills in data structures and object oriented programming. MAJOR TASKS, RESPONSIBILITIES AND KEY ACCOUNTABILITIES - Lead and contribute to engineering efforts from planning to execution and delivery to solve complex engineering problems in tools and testing. • Design and build advanced automated testing frameworks. • Build tooling to help Developers measure and increase their velocity. • Adopt best practices in software health, testing, and sustainability. • Analyze and break down complex software systems and collaborate with Development teams to improve the overall design. NATURE AND SCOPE - • Typically reports to Manager Test Engineering • No associates report to the person in this role on a permanent basis • Analyze and resolve complex quality issues critical to solution delivery • Fast-paced environment of freedom and responsibility PREFERRED QUALIFICATIONS • Hands on Java Development experience • Proficient in Ab Initio ETL and Batch testing • Hands-on knowledge of Soap UI, ITKO Lisa, and Selenium • Hands on experience with Unix, KSH, and Bourne Shell Scripting • Strong scripting knowledge with Java, Groovy and Jmeter • Strong development experience working on web services (REST and SOAP) • Experience building test automation frameworks for web services using Soap UI, Groovy, or Lisa • Proficient in SQL • Working knowledge of SVN and Jenkins – build and development process • eCommerce/Retail QA experience • Excellent written and verbal communication skills • Self-motivated with a strong work ethic and a positive attitude • Desire to work in a fast-paced, results orientated team • Experience with a scripting language such as Perl • Passion to understand, learn, dissect and improve new technologies • Proficient in one or more of the following: Retail applications, Windows platform, UNIX platforms, JAVA, Relational Databases, Websphere Application Server, Websphere Commerce, Websphere MQ • Comprehensive understanding of systems, applications and networks KNOWLEDGE, SKILLS, ABILITIES AND COMPETENCIES - • Proficient in one or more of the following: Retail applications, Windows platform, UNIX platforms, MVS COBOL, JAVA, J2EE, Relational Databases, Websphere Application Server, Websphere Commerce, Websphere MQ, Networking (Voice, LAN, WAN), SAP, Siebel, Peoplesoft • Comprehensive understanding of systems, applications and networks • Strong problem solving and analytical skills • Strong oral and written communication skills • Ability to coordinate and collaborate across cross-functional teams "]
    nlp = MonkeyLearn(key)
    results = nlp.extractors.extract(model_id=model_id, data=data)
    print(results.body[0]['extractions'])

def convert(dataframe):
    preProcessColumn(dataframe)

    processCountry(dataframe)
    processEmployment(dataframe)
    #print(dataframe.head())
    extract()
    return dataframe
