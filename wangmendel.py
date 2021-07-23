import numpy as np

from membership import Triangular, InferiorBorder, SuperiorBorder
from rule_base import FuzzySet, FuzzyRule, FuzzyRuleBase


def get_fuzzy_regions(arr, n_regions, name_preffix='A'):
    
    if n_regions<2:
        raise Exception("The number of fuzzy regions must be at least 2!")
        
    regions = []
        
    ini = min(arr)
    end = max(arr)
    
    step = (end-ini)/(n_regions-1)
        
    fset1 = FuzzySet(name_preffix+'1',InferiorBorder(ini,ini+step))
    fsetN = FuzzySet(name_preffix+str(n_regions), SuperiorBorder(end-step,end))
    
    regions.append(fset1)
    
    for i in range(2, n_regions):
        top = ini+(i-1)*step
        fset = FuzzySet(name_preffix+str(i), Triangular(top-step, top, top+step))
        regions.append(fset)
        
    regions.append(fsetN)
    
    return regions


def learn_fuzzy_rules(X, y,
                      n_regions_inputs=None,
                      n_regions_output=5,
                      name_preffix_inputs=None,
                      name_preffix_output="Out"):
    
    # Convert the dtype of X to numpy array for easier indexing
    if type(X) is list:
        X = np.array(X)
        
    # If the number of fuzzy regions for each of the inputs is not passed,
    # it is defined as 5 regions by default
    if n_regions_inputs is None:
        n_regions_inputs = np.full(X.shape[1], 5)
        
    assert len(n_regions_inputs)==X.shape[1]
    
    # If the name preffix for the inputs is not set, then assign 
    # letter in alphabetical order
    if name_preffix_inputs is None:
        preffix = 'A'
        name_preffix_inputs = []
        for i in range(X.shape[1]):
            name_preffix_inputs.append(chr(ord(preffix)+i))
    
    # Get the fuzzy regions for each of the input variables
    input_regions = []
    for j in range(X.shape[1]):
        input_regions.append(get_fuzzy_regions(X[:,j], n_regions_inputs[j], name_preffix_inputs[j]))
    
    # And for the output
    output_regions = get_fuzzy_regions(y, n_regions_output, name_preffix_output)
    
    rule_base = FuzzyRuleBase()
    for i in range(X.shape[0]):
        
        antecedents = []
        strength = 1
        
        for j in range(X.shape[1]):
            
            
            # Calculate the pertinence degree for the input in each
            # antecedent and get the fuzzy set with maximum pertinence
            max_pertinence = 0
            antecedent = None
            for region in input_regions[j]:
                pertinence = region.set.pertinence(X[i][j])
                
                if pertinence > max_pertinence:
                    antecedent = region
                    max_pertinence = pertinence
                    
            antecedents.append(antecedent)
            strength = strength * max_pertinence
            
        # Calculate the pertinence degree for the output in each
        # consequent and get the fuzzy set with maximum pertinence
        max_pertinence = 0
        consequent = None
        for region in output_regions:
            pertinence = region.set.pertinence(y[i])
            
            if pertinence > max_pertinence:
                consequent = region
                max_pertinence = pertinence
                
        strength = strength * max_pertinence
        
        # Define the fuzzy rule
        rule = FuzzyRule(antecedents, consequent, strength)
        
        # Append the rule into the rule base
        rule_base.appendRule(rule)
        
        
    # Finally we are going to set the value ranges for each input variable
    # and for the output. This step will be important in the inference, more specifically
    # when we calculate the intersection between inputs and antecedents
    input_ranges = []
    for j in range(X.shape[1]):
        input_ranges.append((min(X[:,j]), max(X[:,j])))
    
    output_range = ((min(y), max(y)))
    
    rule_base.setInputRanges(input_ranges)
    rule_base.setOutputRange(output_range)
        
    return rule_base


def clean_rule_base(rule_base):
    cleaned_rule_base = FuzzyRuleBase()
    
    for i in range(rule_base.size()):
        candidate_rule = rule_base.ruleBase[i]
        
        # This flag indicates if the candidate rule has the biggest strength
        # if so, the candidate rule should be included in the cleaned rule base
        strongest_rule = True
        
        for j in range(i, rule_base.size()):
            test_rule = rule_base.ruleBase[j]
            
            if candidate_rule.antecedents == test_rule.antecedents and candidate_rule.strength < test_rule.strength:
                # We found a rule with same antecedents but bigger strength
                # so we should not include the candidate rule into the cleaned rule base
                strongest_rule = False
                break
                
        if strongest_rule:
            cleaned_rule_base.appendRule(candidate_rule)
            
    cleaned_rule_base.setInputRanges(rule_base.inputRanges)
    cleaned_rule_base.setOutputRange(rule_base.outputRange)
    
    return cleaned_rule_base
            