from itertools import permutations,product
            
## main
a = 2
b = 4
c = 7
d = 8
x = 29
allnumbers = [["a","b","c","d"],["a","b"],["a","d"],["a","c"],["c","d"],["b","c"],["a","b","c"],["a","b","d"],["b","c","d"],["a","c","d"]]
target = x
operators = ["+", "-", "*", "/", "**"]        

def eval_formula(formula):
    if formula.count('**') <=2:
        try:
            actual = eval(formula)
            if abs(actual - target)==0:
                print(formula, "=", actual)
        except:
            if formula.count('**') < 2:
                print('err: ' + formula)
            pass
        
for numbers in allnumbers:
    for values in permutations(numbers, len(numbers)):
        for oper in product(operators, repeat=len(numbers) - 1):
            if len(numbers) == 3:
                ## pattern (a oper b) oper c
                valuesWithBracket = ["(" + values[0], values[1] + ")", values[2]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper (b oper c)
                valuesWithBracket = [values[0], "(" + values[1], values[2] + ")"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
            if len(numbers) == 4:
                ## pattern (a oper b) oper c oper d
                valuesWithBracket = ["(" + values[0], values[1] + ")", values[2], values[3]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper (b oper c) oper d
                valuesWithBracket = [values[0], "(" + values[1], values[2] + ")", values[3]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper b oper (c oper d)
                valuesWithBracket = [values[0], values[1],"(" + values[2], values[3] + ")"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper (b oper c oper d)
                valuesWithBracket = [values[0],"(" + values[1],values[2], values[3] + ")"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern (a oper b oper c) oper d
                valuesWithBracket = ["(" +values[0], values[1],values[2]+ ")", values[3]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern ((a oper b) oper c) oper d
                valuesWithBracket = ["((" +values[0], values[1]+ ")",values[2]+ ")", values[3]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern (a oper (b oper c)) oper d
                valuesWithBracket = ["(" +values[0],"(" + values[1],values[2]+ "))", values[3]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern (a oper b) oper (c oper d)
                valuesWithBracket = ["(" +values[0], values[1]+ ")","(" +values[2], values[3]+ ")"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper (b oper (c oper d))
                valuesWithBracket = [values[0], "(" +values[1],"(" +values[2], values[3]+ "))"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper ((b oper c) oper d)
                valuesWithBracket = [values[0], "(" +values[1],"(" +values[2], values[3]+ "))"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
print('end')