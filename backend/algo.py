import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity


def makeResult(Title, Location, Education, Years, Skills, Employment):
    title = Title
    location = Location
    education = Education
    years = Years
    skills = Skills
    employment = Employment
    weight = 1.0

    df0 = makeInput(title, location, education, years, skills, employment)

    df1 = pd.read_csv('data/user_data_2.csv')
    df2 = pd.read_csv('data/user_data_3.csv')
    df2 = df2.sort_index(axis=1)
    df = pd.concat([df1, df2], axis=1)
    df = pd.concat([df0, df])
    input_data = df0.to_numpy()
    user_data = df.to_numpy()

    # df = pd.read_csv('job_data_2.csv')
    df1 = pd.read_csv('data/job_data_2.csv')
    df2 = pd.read_csv('data/job_data_3.csv')
    df2 = df2.sort_index(axis=1)
    df = pd.concat([df1, df2], axis=1)
    job_data = df.to_numpy()
    job_data = np.delete(job_data, 0, 1)

    cs0 = CS(input_data, input_data, job_data, job_data, weight)
    cs1 = CS(user_data, user_data, job_data, job_data, weight)
    input_similarity = cs0.similarity()
    similarity = cs1.similarity()
    input_similarity

    threshold = 0.25
    result = np.transpose((input_similarity > threshold).nonzero())

    user_id = -1
    df1 = pd.read_csv('data/user_data_1.csv')
    df1.fillna(0, inplace=True)
    df2 = pd.read_csv('data/job_data_1.csv')
    df2.fillna(0, inplace=True)
    df3 = pd.DataFrame({'A': []})
    for i in result:
        #     if user_id != i[0]:
        #         print('-----------------------------------------------')
        #         print(df1.loc[i[0]])
        #         print('----------------recommendations---------------')
        #         user_id = i[0]
        #    print('\u2022',df2.loc[i[1]])
        df3 = pd.concat([df3, df2.loc[i[1]]])
    df3 = df3.drop(columns=['A'])

    similarity = normalize(similarity, axis=1, norm='l1')

    mf = MF(similarity * 5, K=6, alpha=0.1, beta=0.001, iterations=10)
    training_process = mf.train()

    # print(similarity*5, mf.full_matrix())
    prediction = similarity * 5 - mf.full_matrix()
    # print(prediction[0])
    threshold = 0.05
    result = np.transpose((prediction[0] < -threshold).nonzero())
    # print(result)
    # user_id = -1
    df3 = pd.DataFrame({'A': []})
    for i in result:
        #     if user_id != i[0]:
        #         print('-----------------------------------------------')
        #         print(df1.loc[i[0]])
        #         print('----------------recommendations---------------')
        #         user_id = i[0]
        #    print('\u2022',df2.loc[i])
        df3 = pd.concat([df3, df2.loc[i]])
    df3 = df3.drop(columns=['A'])
    df3 = df3.drop(columns=['ID'])
    return df3.to_dict()


def makeInput(title, location, education, years, skills, employment):
    df0 = pd.read_csv('data/user_data_0.csv')
    df1_dict = df0.to_dict()
    df0_dict = {k.lower(): v for k, v in df1_dict.items()}
    loc = 'country_' + location.lower()
    if loc in df0_dict.keys():
        df0_dict[loc] = 1
    else:
        df0_dict['country_n/a'] = 1

    edu = 'formaleducation_' + education.lower()
    if edu in df0_dict.keys():
        df0_dict[edu] = 1
    else:
        df0_dict['formaleducation_n/a'] = 1

    skill_list = skills.split(",")
    for skill in skill_list:
        if skill.lower().strip() in df0_dict.keys():
            df0_dict[skill.lower()] = 1

    years = int(years)
    if years <= 2:
        df0_dict["yearscoding_less than 2 years"] = 1
    elif years <= 4:
        df0_dict["yearscoding_3 - 4 years"] = 1
    elif years <= 7:
        df0_dict["yearscoding_5 - 7 years"] = 1
    elif years <= 10:
        df0_dict["yearscoding_7 - 10 years"] = 1
    elif years > 10:
        df0_dict["yearscoding_more than 10 years"] = 1
    else:
        df0_dict["yearscoding_n/a"] = 1

    if employment == "full time":
        df0_dict["employment_full time"] = 1
    elif employment == "part time":
        df0_dict["employment_part time"] = 1
    elif employment == "contractor":
        df0_dict["employment_contractor"] = 1
    else:
        df0_dict["employment_n/a"] = 1

    for k, v in df1_dict.items():
        df1_dict[k] = df0_dict[k.lower()]
    return pd.DataFrame.from_dict(df1_dict)


def getRecommendation(Title, Location, Education, Years, Skills, Employment):
    resDict = makeResult(Title, Location, Education, Years, Skills, Employment)
    results = []
    companyList = list(resDict.get("Company").values())
    employmentList = list(resDict.get("Employment").values())
    locationList = list(resDict.get("Country").values())

    for i in range(len(companyList)):

        results.append({"Company": companyList[i],
            "Employment": employmentList[i],
            "Country": locationList[i]})


    return results


class CS():
    def __init__(self, users_req, users_skill, jobs_req, jobs_skill, weight):
        self.users_req = users_req
        self.jobs_req = jobs_req
        self.users_skill = users_skill
        self.jobs_skill = jobs_skill
        self.weight = weight
        self.one_weight = 1 - weight

    def similarity(self):
        row_u_r, col_u_r = self.users_req.shape
        row_u_s, col_u_s = self.users_skill.shape
        row_j_r, col_j_r = self.jobs_req.shape
        row_j_s, col_j_s = self.jobs_skill.shape


        similarity_req = cosine_similarity(self.users_req.reshape(row_u_r, col_u_r),
                                           self.jobs_req.reshape(row_j_r, col_j_r), dense_output=True)

        similarity_skill = cosine_similarity(self.users_skill.reshape(row_u_r, col_u_r),
                                             self.jobs_skill.reshape(row_j_r, col_j_r), dense_output=True)
        similarity = similarity_req * self.weight + similarity_skill * self.one_weight
        return similarity


class MF():

    def __init__(self, R, K, alpha, beta, iterations):
        """
        Perform matrix factorization to predict empty
        entries in a matrix.

        Arguments
        - R (ndarray)   : user-item rating matrix
        - K (int)       : number of latent dimensions
        - alpha (float) : learning rate
        - beta (float)  : regularization parameter
        """

        self.R = R
        self.num_users, self.num_items = R.shape
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations

    def train(self):
        # Initialize user and item latent feature matrice
        self.P = np.random.normal(scale=1. / self.K, size=(self.num_users, self.K))
        self.Q = np.random.normal(scale=1. / self.K, size=(self.num_items, self.K))

        # Initialize the biases
        self.b_u = np.zeros(self.num_users)
        self.b_i = np.zeros(self.num_items)
        self.b = np.mean(self.R[np.where(self.R != 0)])

        # Create a list of training samples
        self.samples = [
            (i, j, self.R[i, j])
            for i in range(self.num_users)
            for j in range(self.num_items)
            if self.R[i, j] > 0
        ]

        # Perform stochastic gradient descent for number of iterations
        training_process = []
        for i in range(self.iterations):
            np.random.shuffle(self.samples)
            self.sgd()
            mse = self.mse()
            training_process.append((i, mse))
            if (i + 1) % 10 == 0:
                print("Iteration: %d ; error = %.4f" % (i + 1, mse))

        return training_process

    def mse(self):
        """
        A function to compute the total mean square error
        """
        xs, ys = self.R.nonzero()
        predicted = self.full_matrix()
        error = 0
        for x, y in zip(xs, ys):
            error += pow(self.R[x, y] - predicted[x, y], 2)
        return np.sqrt(error)

    def sgd(self):
        """
        Perform stochastic graident descent
        """
        for i, j, r in self.samples:
            # Computer prediction and error
            prediction = self.get_rating(i, j)
            e = (r - prediction)

            # Update biases
            self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
            self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])

            # Create copy of row of P since we need to update it but use older values for update on Q
            P_i = self.P[i, :][:]

            # Update user and item latent feature matrices
            self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i, :])
            self.Q[j, :] += self.alpha * (e * P_i - self.beta * self.Q[j, :])

    def get_rating(self, i, j):
        """
        Get the predicted rating of user i and item j
        """
        prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
        return prediction

    def full_matrix(self):
        """
        Computer the full matrix using the resultant biases, P and Q
        """
        return self.b + self.b_u[:, np.newaxis] + self.b_i[np.newaxis:, ] + self.P.dot(self.Q.T)
