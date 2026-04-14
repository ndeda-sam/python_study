#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
name =  '  JOHn  .'
name=name.strip()
name=name.capitalize()
print(name)

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_one = 'The Dog' \
' Breed is German Shepherd'
print(sentence_one.find("d,13"))
print(sentence_one[8:23])
sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two.find("c",16))
print(sentence_two[16:30])

# Split the below sentence using a semicolon i.e ; And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.”

seentence3='The lazy dog; ran so fast; it hit the wall.'
splt=seentence3.split(";")
print(len(splt))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
first_name="  Joh.n"
last_name="   Do,e"

first_name=first_name.strip()
first_name=first_name.replace(".","")
print(first_name)

last_name=last_name.strip()
last_name=last_name.replace(",","")
print(last_name)

full_name=first_name+" "+last_name
print(full_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r=r.replace(",","")
r=r.replace('"',"")
r=r.replace("[","")
r=r.replace("]","")
print(r)