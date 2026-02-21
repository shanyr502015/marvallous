from sklearn.datasets import load_iris

def main():
    print(" irish classification case study ")

    Dataset = load_iris()

    border = "_"*40
    print(border)
    for i in range(len(Dataset.target)):
        print("ID %d, features %s, label %s" , (i,Dataset.data[i],Dataset.target[i]))

    
if __name__ == "__main__":
    main()