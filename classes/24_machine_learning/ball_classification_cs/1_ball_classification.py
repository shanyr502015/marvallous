# steps for machine learning application

# step 1: data collection/gathering
# step 2: data preprocessing
# step 3: Data analysis & visualization
# step 4: data cleaning
# step 5: model selection
# step 6: model training
# step 7: model evaluation/testing
# step 8: model improvement
# step 9: prediction/deployment

import sklearn

def main():
    # print("sklearn version: ", sklearn.__version__)
    print("ball classification case study")
    # data collection/gathering/loading
    features = [[35,"rough"], [47,"rough"], [90,"smooth"], [48,"rough"],[90,"smooth"],[35,"rough"],[92,"smooth"],[35,"rough"],[35,"rough"],[35,"rough"],[96,"smooth"],[43,"rough"],[110,"smooth"],[35,"rough"],[95,"smooth"]]
    labels = ["tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket", "tennis", "tennis", "tennis", "cricket", "tennis", "cricket", "tennis", "cricket"]  

if __name__ == "__main__":
    main()


# data set size is 15, which is very small, so we will not split the data into training and testing sets, we will use the entire data set for training and testing.