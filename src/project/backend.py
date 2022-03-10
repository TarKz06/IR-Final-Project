import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_and_clean_data():

    data = pd.read_csv('src/resources/Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

    # Number id
    num = data['Number']

    # Title
    title = data['Title'].astype(str)
    cleaned_title = title.apply(lambda s: s.translate(str.maketrans ('','', '([$\'_&+,:;=?@\[\]#|<>.^*()%\\!"-])' +U'\xa8')))
    cleaned_title = cleaned_title.apply(lambda s: s.lower())
    cleaned_title = cleaned_title.apply(lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))

    # Instructions
    instructions = data['Instructions'].astype(str)
    cleaned_instructions = instructions.apply(lambda s: s.translate(str.maketrans ('','', '([$\'_&+,:;=?@\[\]#|<>.^*()%\\!"-])' +U'\xa8')))
    cleaned_instructions = cleaned_instructions.apply(lambda s: s.lower())
    cleaned_instructions = cleaned_instructions.apply(lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))

    # Image_name
    image_name = data['Image_Name'].astype(str)

    # Ingredients
    ingredients = data['Cleaned_Ingredients'].astype(str)
    cleaned_ingredients = ingredients.apply(lambda s: s.translate(str.maketrans ('','', '([$\'_&+,:;=?@\[\]#|<>.^*()%\\!"-])' +U'\xa8')))
    cleaned_ingredients = cleaned_ingredients.apply(lambda s: s.lower())
    cleaned_ingredients = cleaned_ingredients.apply(lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))

    gen_clean_csv = {"Number": num,"Title": cleaned_title ,"Instructions":cleaned_instructions,"Image_Name": image_name,"Ingredients": cleaned_ingredients}
    df = pd.DataFrame(data=gen_clean_csv)

    df.to_csv("src/resources/new Food Ingredients and Recipe.csv", encoding="utf8", index=False)

    try:
        df.to_csv("src/resources/new Food Ingredients and Recipe.csv", encoding="utf8", index=False)
        print('New csv : new Food Ingredients and Recipe.csv')
        return df
    except:
        print("Error")

def exampleoutput(dataFrame):
    print("create example output...")
    data = dataFrame
    tempJson = []
    for i in range(10):
        data.at[i, 'Image_Name'] = data.at[i, 'Image_Name'] + ".jpg"
        tempJson.append({"Number": data.at[i, 'Number'],
                         "Title": data.at[i, 'Title'],
                         "Image_Name": data.at[i, 'Image_Name']})
    print('success create json example')
    return tempJson
