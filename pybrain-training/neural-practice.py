from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection

# Create objecet to hold network
n = FeedForwardNetwork()

# Create the layers
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

# add the layers to the network
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

# specify connections
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

# add connections definition to the network
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

# sort according to connection definitions
n.sortModules()

print(n)

n.activate([1,2])