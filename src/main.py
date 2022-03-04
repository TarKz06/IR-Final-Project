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
    except:
        print("Error")

def tfidf_scoring_by_title(query):

    csv_file = "src/resources/new Food Ingredients and Recipe.csv"
    data = pd.read_csv(csv_file)
    all_data = pd.DataFrame(data, columns=['Title', 'Image_Name', 'Ingredients'])
    rank_list = []
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(all_data['Title'].apply(lambda x: np.str_(x)))
    query_vectorizer = vectorizer.transform([query])
    results = cosine_similarity(X, query_vectorizer).reshape((-1,))
    rank = 0
    for i in results.argsort()[-10:][::-1]:
        rank = rank + 1
        rank_list.append({
            "Rank": rank,
            "Title": all_data.iloc[i, 0],
            "Image": all_data.iloc[i, 1],
            "Ingredient": all_data.iloc[i, 2],
            "Score": results[i]
            }
        )
    return rank_list

def tfidf_scoring_by_ingredients(query):

    csv_file = "src/resources/new Food Ingredients and Recipe.csv"
    data = pd.read_csv(csv_file)
    all_data = pd.DataFrame(data, columns=['Title', 'Image_Name', 'Ingredients'])
    rank_list = []
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(all_data['Ingredients'].apply(lambda x: np.str_(x)))
    query_vectorizer = vectorizer.transform([query])
    results = cosine_similarity(X, query_vectorizer).reshape((-1,))
    rank = 0
    for i in results.argsort()[-10:][::-1]:
        rank = rank + 1
        rank_list.append({
            "Rank": rank,
            "Title": all_data.iloc[i, 0],
            "Image": all_data.iloc[i, 1],
            "Ingredient": all_data.iloc[i, 2],
            "Score": results[i]
            }
        )
    return rank_list
  
  # Read csv file
cleanData = pd.read_csv('src/resources/new Food Ingredients and Recipe.csv')

#Search TF-IDF
def tf_idfByIng(Input):
    vectorizer = TfidfVectorizer()
    data_new = pd.DataFrame(cleanData, columns=['Title','Ingredients','Instructions','Image_Name'])
    findTarg = vectorizer.fit_transform(cleanData['Ingredients'].apply(lambda x: np.str_(x)))
    query_vec = vectorizer.transform([Input])
    results = cosine_similarity(findTarg, query_vec).reshape((-1,))
    count = 0
    dataTfidf = []
    for i in results.argsort()[:][::-1]:
        if (results[i]>0.1):
            count += 1
            dataTfidf.append({
                "Number": count,
                "Title": data_new.iloc[i, 0],
                "Ingredients": data_new.iloc[i, 1],
                "Instructions": data_new.iloc[i, 2],
                "Image_Name": data_new.iloc[i, 3],
                "Score": results[i]
            })

    return dataTfidf


