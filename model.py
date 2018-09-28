from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report
from data_preparation import *
from sklearn.tree import DecisionTreeClassifier


def svm_model():
    """x_test - data we want to predict"""

    X_train, X_test, y_train, y_test = data_prepare_resample()
    svm = SVC()
    svm.fit(X_train, y_train)
    prediction_svc = svm.predict(X_test)
    ac_scv = accuracy_score(y_test, prediction_svc)
    roc_svc = roc_auc_score(y_test, prediction_svc)
    print("SVM acuraccy score is: " + str(ac_scv),
          "SVM ROC score is: " + str(roc_svc))
    print(classification_report(y_test, prediction_svc))
    print(confusion_matrix(y_test, prediction_svc))


def decision_tree():

    X_train, X_test, y_train, y_test = data_prepare()
    decisionTree = DecisionTreeClassifier()
    decisionTree = decisionTree.fit(X=X_train, y=y_train)
    dt_pred_unprunned = decisionTree.predict(X_test)

    ac_dt = accuracy_score(y_test, dt_pred_unprunned)
    roc_dt = roc_auc_score(y_test, dt_pred_unprunned)
    print("DT Acuraccy score is: " + str(ac_dt),
          "DT ROC score is: " + str(roc_dt))
    print(classification_report(y_test, dt_pred_unprunned))
    print(confusion_matrix(y_test, dt_pred_unprunned))

