from textblob import TextBlob
b="Campk12 is a good compny and alays valule ttheir employeees."
a=TextBlob (b)
a=a.correct()
print(a)
