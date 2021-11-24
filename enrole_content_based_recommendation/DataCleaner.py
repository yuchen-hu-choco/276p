# Todo
import category_encoders as ce

def one_hot(dataframe):
    encoder = ce.OneHotEncoder(cols=['Country', 'FormalEducation', 'YearsCoding', 'Employment'], use_cat_names=True)
    return encoder.fit_transform(dataframe)

def clean_dataframe(dataframe):
    return one_hot(dataframe)
