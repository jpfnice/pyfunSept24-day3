import numpy
import pandas

df=pandas.read_csv("data.txt", 
                   sep="[:;]", 
                   names=["text1", "x1", "text2", "x2"], 
                   engine="python") 

print(df)

del df["text1"]
del df["text2"]

print(df)

df["y1"]=numpy.cos(df["x1"])
df["y2"]=numpy.sin(df["x2"])


print(df)

import matplotlib.pyplot as plt

plt.plot(df["x1"], df["y1"], label="Cosine")
plt.plot(df["x2"], df["y2"], label="Sine")

plt.title("A title")
plt.legend()
plt.show()
