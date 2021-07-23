class FuzzyRuleBase:

    def __init__(self):
        self.ruleBase = []
        self.inputRanges = []
        self.outputRange = None

    def appendRule(self, rule):
        self.ruleBase.append(rule)

    def size(self):
        return len(self.ruleBase)
    
    def setInputRanges(self, inputRanges):
        self.inputRanges = inputRanges
        
    def setOutputRange(self, outputRange):
        self.outputRange = outputRange

    def printRule(self,index):
        print("antecedents:")
        for antecedent in self.ruleBase[index].antecedents:
            print(antecedent.name)
        print("consequent:", self.ruleBase[index].consequent.name)
        print("strength:", self.ruleBase[index].strength)

class FuzzyRule:

    def __init__(self, antecedents, consequent, strength):		
        self.antecedents = antecedents
        self.consequent = consequent
        self.strength = strength


class FuzzySet:
    
    def __init__(self, name, fset):
        self.name = name
        self.set = fset
        
    def __repr__(self):
        return "{} = {}".format(self.name, str(self.set))
    
    def __str__(self):
        return "{} = {}".format(self.name, str(self.set))

# 	def __init__(self, name, fset, representation):
# 		self.name = name
# 		self.set = fset
# 		self.representation = representation


