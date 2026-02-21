from sklearn.datasets import load_iris

def main():
    print(" irish classification case study ")

    Dataset = load_iris()

    print(Dataset.data[0])
    print(Dataset.data[1])
    print(Dataset.data[2])
    print(Dataset.data[3])

    print(Dataset.target[0])
    print(Dataset.target[1])
    print(Dataset.target[2])
    print(Dataset.target[3])


    
if __name__ == "__main__":
    main()