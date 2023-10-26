class NeuralNetwork:

    def __init__(self):
        self.layers = 0
        self.neurons = 0
        self.inputs = 0
        self.outputs = 0

        self.activationFunction = ""

        self.weightLayer = [] #Stores 2D matrices of weights for each layer
        self.activationLayer = [] # Stores a vector of activations of the previous layer
        self.biasLayer = [] #Stores a vector of biases for each layer


    def createNN(self, neurons, layers, inputs, outputs, activeFunction):
        """
        Creates a matrice of neurons to store the biases of the nn

        :param p1: Amount a neurons per layer
        :param p2: Amount of layers in the nn excluding the input and output layers
        :param p3: Amount of inputs into the nn
        :param p4: Amount of outputs
        :return: 
        """   
        if activeFunction not in ("relu", "sigmoid"):
            raise ValueError("expects relu or sigmoid")

        self.layers = layers
        self.neurons = neurons
        self.inputs = inputs
        self.outputs = outputs
        self.activationFunction = type

        weighs_0 = [[0 for _ in range (inputs)] for _ in range(neurons)]
        activation_0 = [0 for _ in range (inputs)]
        biases_0 = [0 for _ in range (inputs)]





    def add_weightLayer(self, matrix):
        """
        Add a 2D matrix to the matrices list.
        
        :param matrix: 2D list representing the matrix.
        :return: ID (index) of the matrix.
        """
        self.weightLayer.append(matrix)
        return len(self.weightLayer) - 1
    
    def add_activationLayer(self, activationVectors):
        """
        Add a activation layer
        """
        self.activationLayer.append(activationVectors)
        return len(self.activationLayer) - 1
    
    def add_biaslayer(self, biasArray):
        """
        add bias array
        """
        self.biasLayer.append(biasArray)
        return len(self.biasLayer)


def sigmoid(x):
    """
    Caculates the sigmoid of a given value
    """