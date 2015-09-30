from sklearn import PolynomialFeatures

X = [[1,2,3],[2,3,4],[3,4,5]];
y = [32, 75, 144]

poly = PolynomialFeatures(degree=3)
poly.fit_transform