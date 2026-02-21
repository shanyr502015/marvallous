from sklearn.datasets import load_iris

def main():
    print("Iris classification case study")
    Dataset = load_iris()
    # Metadata of dataset
    print("Independent variables are : ", Dataset.feature_names)
    print("Dependent variables are : ", Dataset.target_names)
if __name__ == "__main__":
    main()
