from model import *
from time import monotonic

start_time = monotonic()


def main():

    svm_model()
    decision_tree()


end_time = monotonic()
print("Script run in: " + str((end_time - start_time)))


if __name__ == "__main__":
    main()