Script runs SVN and Desicion Tree models to predict customers churn.

EDA, vizualization and different models exploration are in exploratory_data_analysis.ipynb

Short summary of analysis:

                        Model       Score       ROC
0     Support Vector Machines    0.987241  0.987272
1                         KNN   92.980000  0.859904
3               Random Forest  100.000000  0.813813
4                 Naive Bayes   80.410000  0.802328
9     Decision Tree unprunned  100.000000  0.771798
8               Decision Tree   92.430000  0.770063
2         Logistic Regression   76.280000  0.762366
5                  Perceptron   59.360000  0.588731
7                  Linear SVC   51.920000  0.519723
6  Stochastic Gradient Decent   49.990000  0.498934

Feature importance:

               importance
DayMins          0.152191
CustServCalls    0.126595
DayCharge        0.125896
EveCharge        0.069660
EveMins          0.065197
IntlPlan         0.061667
IntlCalls        0.049894
IntlMins         0.045316
IntlCharge       0.034040
NightMins        0.033756
DayCalls         0.031391
NightCharge      0.031391
AccountLength    0.030978
EveCalls         0.030150
NightCalls       0.028654
VMailMessage     0.027222
State            0.024262
VMailPlan        0.024155
AreaCode         0.007586

Also in repositary are US State churn interactive vizualization and pdf for desesion tree model.  