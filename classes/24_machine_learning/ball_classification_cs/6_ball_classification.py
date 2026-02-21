from sklearn import tree

def main():
    print(" mv ball case study ")
    # original endcoded dataset
    # independent variable/feature
    X = [[35,1], [47,1], [90,0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    # dependent variable/label
    Y = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2]  

    # independent variable/feature for training
    xtrain = [[35,1], [47,1], [90,0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    # independent variable/feature for testing
    xtest = [[35,1],[95,0]]
    # depentant variable/label for training
    ytrain = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2] 
    # dependent variable/label for testing
    ytest = [1, 2] 

    # created object of decision tree classifier
    modelobj = tree.DecisionTreeClassifier()
    
    # training the model
    trainedmodel = modelobj.fit(xtrain, ytrain)

    # predicting the result for test data
    result = trainedmodel.predict(xtest)    
    result = trainedmodel.predict([[35,1]]) 
    
    print(type(result))

    if result == 1:
        print("model predicts the object as : tennis ball")
    elif result == 2:
        print("model predicts the object as : cricket ball")
    else:
        print("model predicts the object as : unknown ball")  

    print("model predicts the objects as :", result)
    
if __name__ == "__main__":
    main()