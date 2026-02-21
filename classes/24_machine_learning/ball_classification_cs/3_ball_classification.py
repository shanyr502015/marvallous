from sklearn import tree

# rought = 1
# smooth = 0

# tennis = 1
# cricket = 2

def main():
    # independent variable/feature
    features = [[35,1], [47,1], [90,0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    # dependent variable/label
    labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]  

    modelobj = tree.DecisionTreeClassifier()
    trainedmodel = modelobj.fit(features, labels)
    # result = trainedmodel.predict([[37,1]]) # [1]
    result = trainedmodel.predict([[37,1],[94,0]]) # [1 2]

    print("model predicts the objects as :",result)
    
if __name__ == "__main__":
    main()