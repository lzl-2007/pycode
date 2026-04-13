import matplotlib.pyplot as plt
languages=["C","c++","python"]
popularity=[25,30,45]
plt.pie(popularity,labels=languages,autopct="%2.1f%%",startangle=80)
plt.show()