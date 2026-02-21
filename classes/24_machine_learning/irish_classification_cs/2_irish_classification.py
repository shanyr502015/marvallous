from sklearn.datasets import load_iris

def main():
    print(" irish classification case study ")

    Dataset = load_iris()

    print(Dataset)

    # metadata of dataset
    print("independent variable are:")
    print(Dataset.feature_names)

    print("")
    print()

    
if __name__ == "__main__":
    main()