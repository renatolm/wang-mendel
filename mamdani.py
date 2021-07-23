from __future__ import division
import numpy as np
import membership

def intersection(fuzzy_input, fuzzy_set):
	if len(fuzzy_input) != len(fuzzy_set):
		raise ValueError("Argument arrays must have the same size")	

	minimum = []

	for i in range(0, len(fuzzy_input)):
		minimum.append(min(fuzzy_input[i], fuzzy_set[i]))

	result = max(minimum)

	return result

def aggregateOutputs(outputs):
    final_output = outputs[0]
    for i in range(1,len(outputs)):
        final_output = np.maximum(final_output, outputs[i])
    return final_output


def predict(fuzzy_inputs, rule_base):
    
    fuzzy_input_arrays = []
    
    # Map inputs to series of points with precision 100
    for i,fuzzy_input in enumerate(fuzzy_inputs):
        fuzzy_input_array = []
        for x in np.linspace(rule_base.inputRanges[i][0], rule_base.inputRanges[i][1], 100):
            fuzzy_input_array.append(fuzzy_input.set.pertinence(x))
        fuzzy_input_arrays.append(fuzzy_input_array)
        
    for rule in rule_base.ruleBase:
        degree = 1
        
        # Map antecedents to series of points with precision 100
        # and then calculate the intersection (sup-min)
        for j,antecedent in enumerate(rule.antecedents):
            antecedent_array = []
            for x in np.linspace(rule_base.inputRanges[j][0], rule_base.inputRanges[j][1], 100):
                antecedent_array.append(antecedent.set.pertinence(x))
            degree = min(degree, intersection(fuzzy_input_array, antecedent_array))
            
        output_array = []
        Y = np.linspace(rule_base.outputRange[0], rule_base.outputRange[1], 100)
        for y in Y:
            output_array.append(min(degree, rule.consequent.set.pertinence(y)))
            
        outputs.append(output_array)
        
    # Finally, aggregate the outputs of individual rules
    f_y = aggregateOutputs(outputs)
    
    return Y, f_y


def predict_crisp(inputs, rule_base):    
        
    outputs = []
    for rule in rule_base.ruleBase:
        degree = 1
        
        # Map antecedents to series of points with precision 100
        # and then calculate the intersection (sup-min)
        for j,antecedent in enumerate(rule.antecedents):
            degree = min(degree, antecedent.set.pertinence(inputs[j]))
            
        output_array = []
        Y = np.linspace(rule_base.outputRange[0], rule_base.outputRange[1], 100)
        for y in Y:
            output_array.append(min(degree, rule.consequent.set.pertinence(y)))
            
        outputs.append(output_array)
        
    # Finally, aggregate the outputs of individual rules
    f_y = aggregateOutputs(outputs)
    
    return Y, f_y