from sklearn import datasets, svm

iris = datasets.load_iris()
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])
for i in range(0,len(digits.target)):
    cl = clf.predict(digits.data[i])
    print("The predicted output is: %s, expected %s" % (cl, digits.target[i]))