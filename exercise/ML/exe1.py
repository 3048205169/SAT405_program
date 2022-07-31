from sklearn.datasets import load_iris

def datasets_demo():


    iris = load_iris()
    print("iris dataset:",iris)

    return None

if __name__ == "__main__":
    datasets_demo()