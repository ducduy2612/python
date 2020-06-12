from itertools import permutations,product

a = 2.0
b = 4.0
c = 7.0
d = 8.0
allset = range(1,100)
numbers = ["a","b","c","d"]
operators = ["+", "-", "*", "/", "**"]      
allanswers= {}
for i in allset:
    allanswers[i] = []

def eval_formula(formula, target):
    try:
        actual = eval(formula)
        if actual - target==0:
            allanswers[target].append(formula)
        else:
            pass
    except OverflowError:
        pass
    except ZeroDivisionError:
        pass

for target in allset:
    for n in range(2,len(numbers)+1):
        for values in permutations(numbers, n):
            for oper in product(operators, repeat = n - 1):
                if n == 2:
                    formula = "".join(o + v for o, v in zip([""] + list(oper), values))
                    eval_formula(formula, target)
                if n == 3:
                    ## pattern (a oper b) oper c
                    valuesWithBracket = ["(" + values[0], values[1] + ")", values[2]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper (b oper c)
                    valuesWithBracket = [values[0], "(" + values[1], values[2] + ")"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                if n == 4:
                    ## pattern (a oper b) oper c oper d
                    valuesWithBracket = ["(" + values[0], values[1] + ")", values[2], values[3]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper (b oper c) oper d
                    valuesWithBracket = [values[0], "(" + values[1], values[2] + ")", values[3]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper b oper (c oper d)
                    valuesWithBracket = [values[0], values[1],"(" + values[2], values[3] + ")"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper (b oper c oper d)
                    valuesWithBracket = [values[0],"(" + values[1],values[2], values[3] + ")"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern (a oper b oper c) oper d
                    valuesWithBracket = ["(" +values[0], values[1],values[2]+ ")", values[3]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern ((a oper b) oper c) oper d
                    valuesWithBracket = ["((" +values[0], values[1]+ ")",values[2]+ ")", values[3]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern (a oper (b oper c)) oper d
                    valuesWithBracket = ["(" +values[0],"(" + values[1],values[2]+ "))", values[3]]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern (a oper b) oper (c oper d)
                    valuesWithBracket = ["(" +values[0], values[1]+ ")","(" +values[2], values[3]+ ")"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper (b oper (c oper d))
                    valuesWithBracket = [values[0], "(" +values[1],"(" +values[2], values[3]+ "))"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    ## pattern a oper ((b oper c) oper d)
                    valuesWithBracket = [values[0], "(" +values[1],"(" +values[2], values[3]+ "))"]
                    formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                    eval_formula(formula, target)
                    
print('end')
