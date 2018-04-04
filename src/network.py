'''
Created on Apr 4, 2018

Very simple neural network
Credit to https://becominghuman.ai/making-a-simple-neural-network-2ea1de81ec20

@author: Michael Ehnes
'''
inputs = [0, 1, 0, 0]
weights = [0, 0, 0, 0]
desiredResult = 1
learningRate = .2
trials = 6

# Taking the input / weight pairs and multiplying them together and adding the result
def evaluateNeuralNetwork(inputVector, weightVectror):
    
    result = 0
    index = 0
    
    for val in inputVector:
        layerValue = val * weightVectror[index]
        result += layerValue
        index += 1
        
    return format(result, '.2f')

# higher error = worse performance
def evaluateNeuralNetError(desired, actual):
    return format(desired - actual, '.2f')

def learn(inputVector, weightVector):
    
    index = 0
    
    for val in weightVector:
        
        if (inputVector[index] > 0):
            weightVector[index] += learningRate
            
        index += 1
        
    return   

x = 0

for x in range(trials):
    neuralNetResult = evaluateNeuralNetwork(inputs, weights)
    print(neuralNetResult)
    learn(inputs, weights)
    
'''

    What I learned 
    It takes a minimum of 6 trials to win
    basics of python (I've never used this language before)
    You need a way to calculate how far off you are from desired output
    You can increase / decrease learning rate
    The more weight something carries, the more correct it is
    Every time the learn function is rn, the correct answer carries more weight 

'''
        
        
        
        
        
        