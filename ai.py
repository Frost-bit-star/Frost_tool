from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from googlesearch import search

# Initialize CountVectorizer and Multinomial Naive Bayes classifier
vectorizer = CountVectorizer()
classifier = MultinomialNB()

# Define a function to train the machine learning model based on user input
def train_model(X_train, y_train):
    X_train_counts = vectorizer.fit_transform(X_train)
    classifier.fit(X_train_counts, y_train)

# Define a function to predict the response of the machine learning model
def predict_response(query):
    query_transformed = vectorizer.transform([query])
    prediction = classifier.predict(query_transformed)
    if prediction[0] == 'unknown':
        return search(query, num=1)[0]
    return prediction[0]

# Initialize training data
X_train = ['What is your name', 'How are you', 'unknown', 'unknown']
y_train = ['morgan', 'I am fine', 'unknown', 'unknown']

# Train the machine learning model
train_model(X_train, y_train)

# Main loop to interact with the user
while True:
    user_input = input('Ask me a question: ')
    response = predict_response(user_input)
    print(response)

