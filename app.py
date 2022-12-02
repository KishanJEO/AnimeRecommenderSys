import streamlit as st
#from PIL import Image
import pandas as pd
#import base64

st.set_page_config(
    page_title="Anime Recommender", page_icon=":four_leaf_clover:", layout="wide"
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.pinimg.com/originals/89/86/57/8986574c2f071529b0bf7063421cc9f2.jpg");
background-size: cover;
}
</style>
"""

EMAIL = "kthamata@student.fitchburgstate.edu"

st.markdown(page_bg_img, unsafe_allow_html=True)

st.subheader("Hi, I am Kishan :wave:")

st.title("Anime Recommendation System")

Background = st.container()
Anime_Description = st.container()
Facts = st.container()
Project_Overview = st.container()
Theoretical_Description = st.container()
Dataset_Description = st.container()
Model = st.container()
Future_addon = st.container()

with Background:
    st.subheader("Background")

    st.write(
        "**A**nime is a Japanese word for hand-drawn or computer animation. Anime dates back to the early 20th century and has grown in popularity ever since.")
    st.write(
        "Anime's distinct style emerged in the sixties with Osamu Tezuka. Soon after, anime grew popular around the world and developed a large following.")
    st.write(
        "Anime has become widely recognizable for its unique style and look. It is regarded as an ideal story-telling mechanism, as it combines illustration, characterization, and cinematography.")

with Anime_Description:
    column_1, column_2, column_3 = st.columns([6, 2, 2])
    with column_1:
        st.subheader("Clarification on (**Anime** V **Cartoon** V **Manga**)")
        st.write(
            """  
        * **Cartoon**: no strict storyline. Aimed towards little kids. Have almost zero incentive for adults to watch. Has minimalist to zero mature content.

        * **Anime**: it is animated like cartoons but the opposite in mostly all sense. It has a storyline, different genres, mostlg aimed at young adults and adults.

        * **Manga** : Manga is nothing but anime in a sketch. Most animes are mangas that have been converted into animated series for viewers. In lay-man language, just like certain cartoons are made from comics, similarly anime are made from mangas.

        Most animes are thought to be Japanese Cartoon which isn't true at all. Any animation that has all the things I mentioned is an anime.

        *The difference between a manga and a comic is the same as the difference between a cartoon and an anime*.
        """
        )
        st.caption("[Learn More > ](https://www.techanimate.com/anime-vs-manga/)")

with Facts:
    st.subheader("Facts")
    st.write(
        """
    * In Japan, more paper is used to print manga than toilet paper!!
    * The highest grossing anime film of all time is **Demon Slayer: Mugen Train ($454,779,627)**!!
    * Did you know over 60% of the animated content in the world are actually anime! Not cartoon, not Disney, but Anime rules the world of animation!!
    * It usually costs around **100,000 USD to 200,000 USD** to make a single anime episode! Then think about how much it'll actually cost to make an entire season!!
    * In JoJo's Bizarre Adventure, a character called Boingo uses his stand ability to predict the future.  But what was actually surprising was, it seems like he actually predicted the 9/11 attack! \n
      **This manga was drawn in 1990, eleven years before the incident!!**
    * The global Anime market size was valued at **24.80 Billion USD** in the year 2021, **26.89 billion** USD in 2022 and **48.3 billion** USD by 2030!!
    """
    )
    st.caption("[Learn More >](https://15facts.com/15-awesome-facts-about-anime/)")

with Dataset_Description:
    st.subheader("Dataset Description")
    st.write("The dataset is taken from Kaggle Datasets.")
    st.write('''
    * The dataset initially consists of 18495 observations and 17 variables.
    * The dataset supplied to the Recommender model contains 13356 observations and 5 variables.
        * **Rank**  - The rank of the anime on the Anime planet website.
        * **Name**  - Title of the anime.
        * **Type**  - Anime type (Web,Movie,TV).
        * **Tags**  - Genres,keywords(swordplay,sliceoflife,demons,etc) and original creator.
        * **Name_new**  - A new variable derived from Name variable (feature engineering).
    * The dataset has made though web scraping from the Anime Planet website.

    ''')
    st.caption("[Dataset > ](https://www.kaggle.com/datasets/vishalmane10/anime-dataset-2022)")

with Project_Overview:
    column_4, column_5 = st.columns([6, 4])
    with column_4:
        st.header("Project Overview")
        st.write(
            """
        As the title suggests this project is about buliding an Anime Recommendation System. 
        The project has been carried out using the **content based filtering**.

        In the Content based filtering, the recommendations are made on the basis of similarity of contents. 
        This is done by creating **tags** and based on the similarity of tags, recommendations are made.

        We will be performing **Text Vectorization** using the **scikit_learn** library with **CountVectorizer**. 
        Furthermore, calculating the similarity score using **cosine_similarity**.
        """
        )
        st.caption(
            "[Learn More >](https://www.analyticssteps.com/blogs/what-content-based-recommendation-system-machine-learning)"
        )

with Theoretical_Description:
    st.header("Theoretical Description")
    st.subheader("Text Vectization")
    st.write(
        """
    Text Vectorization is basically the conversion of text into vectors.
    Inorder to achieve this there are many popular methods **Bag of Words**, **tfidf**, **Word2Vec**. \n
    However, in this project we will be using the **Bag of Words method**.
    """
    )
    st.caption(
        "[Learn More >](https://www.deepset.ai/blog/what-is-text-vectorization-in-nlp)"
    )

    st.subheader("Bag of Words")
    st.write(
        """
    In **Bag of Words**, all of the tags are combined together i.e., we do concatination of tags (Tag1, Tags2, Tag3,.....,Tag*n*).
    Where *n* is the the last observation tag.

    **Upon doing this a large string is formed**.

    From the large text formed we extract the top *n* most frequently occuring words.
    The tags of each observation are checked with top *n* most frequently occuring words. \n
    Hence a numpy array of vector for each observation is formed. 
    We need to also make sure that there are no stop_words(the,as,then,that,etc.)
    """
    )
    st.caption("[Learn More >](https://victorzhou.com/blog/bag-of-words/)")

    st.subheader("Similarity_score")
    st.write(
        """
    Since, we now have an array of vectors our next step would be to decide on how to determine the vectors close to the vector selected.

    There are multiple ways to do this through **Euclidian Distance** or through determining the least **θ** or angle formed. \n
    However, going with Euclidian Distance is not a correct option because it does not do well with a higher dimension graph. \n
    So let us choose the method to calculate the least angle from our observation. \n
    This can be accomplished by using the **cosine_similarity** from the **scikit_learn** library. \n
    Upon doing this a np array is generated with the similarity of one observation with all the other observations.

    Then when the input anime is given we do sorting in descending order on the anime similarity score and display the top 5 animes. \n
    **Along with the top 5 recommendations. A url for each recommended anime will be displayed which will direct you to offical Anime Planet Website**. 
    """
    )
    st.caption(
        "[Learn More >](https://www.learndatasci.com/glossary/cosine-similarity/)"
    )

Anime = pd.read_csv("ARS_clean.csv")

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=13500, stop_words="english")

cv.fit_transform(Anime["Tags"]).toarray()

vectors = cv.fit_transform(Anime["Tags"]).toarray()

from sklearn.metrics.pairwise import cosine_similarity

Similarity = cosine_similarity(vectors)

Anime["Name_new"] = Anime["Name"].apply(lambda x: x.lower())

# Remove Punctuation from a String
import string

Anime["Name_new"] = Anime["Name_new"].apply(
    lambda x: x.translate(str.maketrans("", "", string.punctuation))
)

# Removing extra spaces
Anime["Name_new"] = Anime["Name_new"].apply(lambda x: " ".join(x.split()))

# Replacing " " with "-"
Anime["Name_new"] = Anime["Name_new"].apply(lambda x: x.replace(" ", "-"))


# Similarity = pickle.load(
#    open(
#        "/Users/kishanjeo/Desktop/VS_code/Gitt/ARS_model_deployment/similarity_score.pkl",
#        "rb",
#    )
# )


# All GOOD
def Recommender(user_input):
    Index_of_anime = Anime[Anime["Name"] == user_input].index[0]
    Similarity_score = Similarity[Index_of_anime]
    Sorted_scores = sorted(
        list(enumerate(Similarity_score)), reverse=True, key=lambda x: x[1]
    )[1:6]
    Recommended_Anime = []
    for i in Sorted_scores:
        Recommended_Anime.append(Anime.iloc[i[0]].Name)
    return Recommended_Anime


def Anime_Planet():
    Anime_planet_index = []
    Anime_planet_names = []
    for i in Recommended_Anime:
        Anime_planet_index.append(Anime[Anime["Name"] == i].index[0])
    for j in Anime_planet_index:
        Anime_planet_names.append(Anime["Name_new"][j])
    return Anime_planet_names


with Model:
    st.write("------------")
    st.header("Get Recommendations")
    user_input = st.selectbox("Select or Type the Anime Name", Anime["Name"].values)

    if st.button("Recommend"):
        column_6, column_7, column_8, column_9, column_10 = st.columns(5)
        Recommended_Anime = Recommender(user_input)
        Anime_planet_names = Anime_Planet()

        url = "https://www.anime-planet.com/anime/"

        with column_6:
            st.write(Recommended_Anime[0])
            Anime_0 = str(url) + str(Anime_planet_names[0])
            st.write("----")
            st.write("Anime Planet Url:")
            st.write(Anime_0)

        with column_7:
            st.write(Recommended_Anime[1])
            Anime_1 = str(url) + str(Anime_planet_names[1])
            st.write("----")
            st.write("Anime Planet Url:")
            st.write(Anime_1)

        with column_8:
            st.write(Recommended_Anime[2])
            Anime_2 = str(url) + str(Anime_planet_names[2])
            st.write("----")
            st.write("Anime Planet Url:")
            st.write(Anime_2)

        with column_9:
            st.write(Recommended_Anime[3])
            Anime_3 = str(url) + str(Anime_planet_names[3])
            st.write("----")
            st.write("Anime Planet Url:")
            st.write(Anime_3)

        with column_10:
            st.write(Recommended_Anime[4])
            Anime_4 = str(url) + str(Anime_planet_names[4])
            st.write("----")
            st.write("Anime Planet Url:")
            st.write(Anime_4)

        st.write("-------")

    else:
        st.write("Select an Anime.")

with Future_addon:
    st.subheader("Whats Next?")
    st.write('''
    * Implementing a collaborative filtering based recommender system.
    * Key insights on the Anime Dataset through visualizations.
    * Top 50 Anime with images.
    ''')

    st.write("------")

    st.subheader(":mailbox:Connect with me")
    st.write(EMAIL)
    st.write("[LinkedIn > ](https://www.linkedin.com/in/kishan-kumar-reddy-thamatam-venkata-181682218/)")
    st.write("[GitHub > ](https://github.com/KishanJEO)")