import matplotlib.pyplot as plt
import seaborn as sns


def plot_country(dataframe, save=None):
    plt.figure(figsize=(10, 10))
    country = dataframe["Country"].value_counts().reset_index()
    ax = sns.barplot("Country", "index", data=country[:20], linewidth=2)
    plt.xlabel("number of responses")
    plt.ylabel("country")
    plt.title("Number of responses in different countries")
    plt.grid(True, alpha=.3)

    for i, j in enumerate(country["Country"][:20]):
        ax.text(.7, i, j, weight="bold")
    if save is None:
        plt.show()
    else:
        plt.savefig(save);


def plot_empty_rate(dataframe, save=None):
    miss = dataframe.isnull().sum().reset_index()
    miss[0] = miss[0] * 100 / miss[0].sum()

    plt.figure(figsize=(13, 10))
    ax = sns.barplot("index", 0, data=miss, color="orange")
    plt.xticks(fontsize=13)
    plt.title("percentage of missing values")
    ax.set_facecolor("k")
    ax.set_ylabel("percentage of missing values")
    plt.show()
    if save is None:
        plt.show()
    else:
        plt.savefig(save);


def plot_experience(dataframe, save=None):
    plt.figure(figsize=(15, 10))
    experience = dataframe["YearsCoding"].value_counts().reset_index()
    ax = sns.barplot("YearsCoding", "index", data=experience, linewidth=2)
    plt.xlabel("number of responses")
    plt.ylabel("Years of Coding")
    plt.title("Coding experience distribution")
    plt.grid(True, alpha=.3)

    for i, j in enumerate(experience["YearsCoding"]):
        ax.text(.7, i, j, weight="bold")
    if save is None:
        plt.show()
    else:
        plt.savefig(save);


def plot_education(dataframe, save=None):
    plt.figure(figsize=(35, 15))
    dataframe["FormalEducation"].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("Set1"),
                                                         fontsize=16, wedgeprops={"linewidth": 2, "edgecolor": "white"},
                                                         shadow=True)
    plt.title("Education distribution")
    plt.show()
    if save is None:
        plt.show()
    else:
        plt.savefig(save);


def plot_company_size(dataframe, save=None):
    plt.figure(figsize=(18, 10))
    experience = dataframe["CompanySize"].value_counts().reset_index()
    ax = sns.barplot("CompanySize", "index", data=experience, linewidth=2)
    plt.xlabel("number of responses")
    plt.ylabel("Company Size")
    plt.title("Company size distribution")
    plt.grid(True, alpha=.3)

    for i, j in enumerate(experience["CompanySize"]):
        ax.text(.7, i, j, weight="bold")
    if save is None:
        plt.show()
    else:
        plt.savefig(save);


def ploy_employment(dataframe, save=None):
    plt.figure(figsize=(30, 15))
    dataframe["Employment"].value_counts().plot.pie(autopct="%1.1f%%", colors=sns.color_palette("Set1"),
                                                    fontsize=16, wedgeprops={"linewidth": 2, "edgecolor": "white"},
                                                    shadow=True)
    plt.title("Employment distribution")
    plt.show()
    if save is None:
        plt.show()
    else:
        plt.savefig(save);
