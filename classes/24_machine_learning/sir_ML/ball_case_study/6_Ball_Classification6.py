from sklearn import tree

# Rough = 1
# Smooth = 0

# Tennis = 1
# Cricket = 2

def main():
    print("Ball classification case study")

    # Original encoded dataset
    # Independent variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] # Dataset Size : 15, 1st column is diameter and 2nd column is surface type (1 for rough and 0 for smooth).
    # Dependent Variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2] # Dataset Size : 15, 1 for tennis ball and 2 for cricket ball.

    # Independent variables for training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]] # Dataset Size : 13, 1st column is diameter and 2nd column is surface type (1 for rough and 0 for smooth).
    # Independent variables for testing
    Xtest = [[35,1],[95,0]] # Dataset Size : 2, 1st column is diameter and 2nd column is surface type (1 for rough and 0 for smooth).
    
    # Dependent variables for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2] # Dataset Size : 13, 1 for tennis ball and 2 for cricket ball.
    # Dependent variables for testing
    Ytest = [1,2] # Dataset Size : 2, 1 for tennis ball and 2 for cricket ball.

    modelobj = tree.DecisionTreeClassifier() # Create a Decision Tree Classifier object
    trainedmodel = modelobj.fit(Xtrain,Ytrain) # Train the model using the training dataset
    Result = trainedmodel.predict([[35,1]]) # Predict the class label for a new data point with diameter 35 and rough surface (1)
    print(type(Result))
    
    if Result == 1:
        print("Object looks like tennins ball")
    elif Result == 2:
        print("Object looks like cricket ball")

if __name__ == "__main__":
    main()
