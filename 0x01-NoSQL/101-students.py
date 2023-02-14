def top_students(mongo_collection):

    res = mongo_collection.find()

    for i in mongo_collection:

        i = 0

        sc = 0

        for j in i[topics]:

            sc += j[score]

            i +=1

        i.averageScore = sc/ i
