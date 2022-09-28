article = ("Facial recognition technology has grown by leaps and bounds over the last decade, and it can be hard to keep up with all the developments. If you are wondering how face recognition works, our comprehensive guide will explain the technology in detail. How is your iPhone able to unlock by scanning your face? Why does the customs office at an airport scan your face when you enter a country? Read on to find out.")



substitutions = {
"Facial":"Face",
"iPhone":"phone",
"Read on to find out":"Keep on reading to find out",
"hard":"difficult",
"technology":"tech",
"decade":"many years",
}

for key, value in substitutions.items():
  article = article.replace(key,value)
  
print (article)