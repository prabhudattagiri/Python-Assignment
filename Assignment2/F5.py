# 5. Wap to create biodata of a student using variable length argument function incv format available in ms doc?
def biodata (name , email , phone , branch,clg, *skill):
    details ="   Bio Data   "+"\nName :"+name+"\nEmail :"+email+"\nPhone :"+phone+"\nBranch :"+branch+"\nCollege :"+clg+"\nSkills :"
    for s in skill:
        details+=" "+s

    return details

# Calling Function
r=biodata("Prabhudatta Giri","prabhudattagiri@gmail.com","9178808047","MCA","IGIT","C","C++","Java","Python") # variable length argument
print(r)