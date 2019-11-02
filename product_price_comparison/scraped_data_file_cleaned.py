text=["Heyi boss how are you are you in dhaka now","hi whats up are you lving capital city dhaka"]

from sklearn.feature_extraction.text from CountVectorizer
cv=CountVectorizer()
count_matrix=cv.fit_transform(text)
print(cv.get_feature_names())
print(count_matrix.toarray())

