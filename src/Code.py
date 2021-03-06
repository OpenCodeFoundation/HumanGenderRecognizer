from sklearn import tree
dtc = tree.DecisionTreeClassifier() #storing decision tree model

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

dtc = dtc.fit(X, Y) 
#fit method trains the decision tree on our data

prediction = dtc.predict([[190, 70, 43]])

print("Predict Decision Tree: ", prediction)
