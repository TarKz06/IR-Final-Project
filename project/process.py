from spellchecker import SpellChecker
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re



def get_and_clean_data():
    data = pd.read_csv('src/resource/Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

    id = data['No']
    title = data['Title'].astype(str)
    ingredients = data['Cleaned_Ingredients'].astype(str)
    instructions = data['Instructions'].astype(str)
    image_name = data['Image_Name'].astype(str)

    # clean title #
    cleaned_title = title.apply(lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
    cleaned_title = cleaned_title.apply(lambda s: s.lower())
    cleaned_title = cleaned_title.apply(
        lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))

    # clean instructions #
    cleaned_instructions = instructions.apply(
        lambda s: s.translate(str.maketrans('', '', string.punctuation + u'\xa0')))
    cleaned_instructions = cleaned_instructions.apply(lambda s: s.lower())
    cleaned_instructions = cleaned_instructions.apply(
        lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))

    # clean ingredients #
    punctuation = "!\"#$%&'()*+,-:;<=>?@[\]^_`{|}~/"
    cleaned_ingredients = ingredients.apply(lambda s: s.translate(str.maketrans('', '', punctuation + u'\xa0')))
    cleaned_ingredients = cleaned_ingredients.apply(lambda s: s.lower())
    cleaned_ingredients = cleaned_ingredients.apply(
        lambda s: s.translate(str.maketrans(string.whitespace, ' ' * len(string.whitespace), '')))
    # make new csv dataset #
    cleaned_csv_data = {"id": id, "Title": cleaned_title, "Instructions": cleaned_instructions,
                        "Image_Name": image_name, "Ingredients": cleaned_ingredients}
    dataFrame = pd.DataFrame(data=cleaned_csv_data)

    try:
        print("Finish cleaned")
        return dataFrame
    except:
        print("Error")

def exampleoutput(dataFrame):
    print("gen sample data")
    data = dataFrame
    tempJson = []
    for i in range(8):
    #   data.at[i, 'Image_Name'] = data.at[i, 'Image_Name'] + ".jpg"
    #   tempJson.append([[data.at[i, 'id']],[data.at[i, 'Title']],[data.at[i, 'Image_Name']]])
        tempJson.append({"id": data.at[i, 'id'],
                         "Title": data.at[i, 'Title'],
                         "Image_Name": data.at[i, 'Image_Name']})

    print('success gen  example')
    return tempJson

def findfooddetails(dataframe, inputword):
    data = dataframe
    foodname = inputword
    print(foodname)
    fooddetails = []
    for i, row in data.iterrows():
        if data.at[i, 'Title'] == foodname:
            fooddetails.append({"Title": data.at[i, 'Title'],
                                "Instructions": data.at[i, 'Instructions'],
                                "Ingredients": data.at[i, 'Ingredients'],
                                "Image_Name": data.at[i, 'Image_Name']})

# df = pd.DataFrame(tempJson, columns=["no","artist","songname","lyric"])
# cleanData = pd.read_csv("src/resource/Food Recipe.csv")
#Search TF-IDF for Title
# def tf_idfByTitle(Input):
#     vectorizer = TfidfVectorizer()
#     data_new = pd.DataFrame(cleanData, columns=['Title', 'Ingredients', 'Instructions', 'Image_Name'])
#     findTarg = vectorizer.fit_transform(cleanData['Title'].apply(lambda x: np.str_(x)))
#     spell = SpellCheck(Input)
#     query_vec = vectorizer.transform([spell])
#     results = cosine_similarity(findTarg, query_vec).reshape((-1,))
#     count = 0
#     dataTfidf = []
#     for i in results.argsort()[:][::-1]:
#         if (results[i] > 0.1):
#             count += 1
#             dataTfidf.append({
#                 "Number": count,
#                 "Title": data_new.iloc[i, 0],
#                 "Ingredients": data_new.iloc[i, 1],
#                 "Instructions": data_new.iloc[i, 2],
#                 "Image_Name": data_new.iloc[i, 3],
#                 "Score": results[i]
#             })
#
#     return dataTfidf
#
# #Search TF-IDF for Ingredient
# def tf_idfByIng(Input):
#     vectorizer = TfidfVectorizer()
#     data_new = pd.DataFrame(cleanData, columns=['Title','Ingredients','Instructions','Image_Name'])
#     findTarg = vectorizer.fit_transform(cleanData['Ingredients'].apply(lambda x: np.str_(x)))
#     spell = SpellCheck(Input)
#     query_vec = vectorizer.transform([spell])
#     results = cosine_similarity(findTarg, query_vec).reshape((-1,))
#     count = 0
#     dataTfidf = []
#     for i in results.argsort()[:][::-1]:
#         if (results[i]>0.1):
#             count += 1
#             dataTfidf.append({
#                 "Number": count,
#                 "Title": data_new.iloc[i, 0],
#                 "Ingredients": data_new.iloc[i, 1],
#                 "Instructions": data_new.iloc[i, 2],
#                 "Image_Name": data_new.iloc[i, 3],
#                 "Score": results[i]
#             })
#
#     return dataTfidf

def searchtfidf(inputword,df_new,where):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(df_new[where])
    print(X.shape)
    query = inputword
    query_vec = vectorizer.transform([query])
    results = cosine_similarity(X, query_vec).reshape((-1,))
    tfidfJson = []
    for i in results.argsort()[::-1]:
        if results[i] > 0:
            tfidfJson.append({"id": df_new.iloc[i, 0],
                             "foodTitle": df_new.iloc[i, 1],
                             "foodPicture": df_new.iloc[i, 3]})
    return tfidfJson

def favoritesearchtfidf(inputword,df_new):
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(df_new['foodTitle'])
    print(X.shape)
    query = inputword
    query_vec = vectorizer.transform([query])
    results = cosine_similarity(X, query_vec).reshape((-1,))
    tfidfJson = []
    for i in results.argsort()[::-1]:
        print(results[i])
        if results[i] > 0:
            tfidfJson.append({"id": df_new.iloc[i, 0],
                             "foodTitle": df_new.iloc[i, 1],
                             "foodPicture": df_new.iloc[i, 2]})
    return tfidfJson

def wordsuggestion(inputword):
    spell = SpellChecker()
    input = inputword.split()
    wordtemp = []
    for word in input:
        wordtemp.append(spell.correction(word))
    wordtemp=wordtemp
    wordtemp = ' '.join(wordtemp)
    if wordtemp == inputword:
        return inputword
    else:
        return wordtemp

# Spell checker
def SpellCheck(Input):
    spellaray = []
    spell = SpellChecker()
    dataSpell = Input.split()
    for i in dataSpell:
        spellaray.append(spell.correction(i))
    spellaray = ' '.join(spellaray)
    return spellaray

def pagination(datainput,page):
    page = page-1
    dataperpage = 12
    result = len(datainput)
    data = []
    point = 0
    if result/dataperpage <= 1:
        data.append(datainput)
        return data
    else:
        pagenumber = result//dataperpage
        print('have: ',pagenumber,' page')
        for i in range(pagenumber+1):
            if point < result:
                datatemp = []
                for j in range(dataperpage):
                    if point < result:
                        datatemp.append(datainput[point])
                        point = point+1
                data.append(datatemp)
        print(data[page])
        return data

def currentpage(currentpage, allpage):
    previouspage = True
    nextpage = True
    if currentpage-1 >= 0:
        previouspage = True
    else:
        previouspage = False
    if currentpage+1 < allpage:
        nextpage = True
    else:
        nextpage = False
    return [{'previouspage': previouspage,'nextpage': nextpage}]