def findDecision(obj): #obj[0]: Sepal length, obj[1]: Sepal width, obj[2]: Petal length, obj[3]: Petal width
   if obj[2]>1.9:
      if obj[1]<=3.4:
         if obj[0]>5.4:
            if obj[3]>0.6:
               return 0.5143267214298248
         elif obj[0]<=5.4:
            if obj[3]>0.6:
               return 0.5143267214298248
      elif obj[1]>3.4:
         return -0.2533705234527588
   elif obj[2]<=1.9:
      return -0.2571633458137512
