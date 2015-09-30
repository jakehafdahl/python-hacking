from pybrain.datasets import SupervisedDataSet
from pybrain.tools.neuralnets import NNregression
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from random import normalvariate
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def make_dataset():
    """
        Creates a set of training data.
        """
    
    X = []
    y = []
    
    for i in range(0,100):
        x = normalvariate(i, 1.6)
        X.append([x, x + 1])
        y.append([4 * x ** 2])
    
    poly = PolynomialFeatures(2)
    X_poly = poly.fit_transform(X);
    
    data = SupervisedDataSet(5,1)
    data.setField('input', X_poly)
    data.setField('target', y)

    return data


def training(d):
    """
        Builds a network and trains it.
        """
    print("Creating Neural Network")
    n = NNregression(d)
    print("Setting Up Neural Network")
    n.setupNN()
    print("Training Neural Network")
    n.runTraining()
        
    print("Returning Trainier")
    return n.Trainer


def test(trained):
    """
        Builds a new test dataset and tests the trained network on it.
        """
    X = []
    y = []
    
    for i in range(3,10):
        x = normalvariate(i, 1.6)
        X.append([x, x + 1])
        y.append([4 * x ** 2])
    
    poly = PolynomialFeatures(2)
    X_poly = poly.fit_transform(X);
    
    testdata = SupervisedDataSet(5,1)
    testdata.setField('input', X_poly)
    testdata.setField('target', y)
    trained.testOnData(testdata, verbose= True)


def run():
    """
        Use this function to run build, train, and test your neural network.
        """
    trainingdata = make_dataset()
    trained = training(trainingdata)
    test(trained)

run()