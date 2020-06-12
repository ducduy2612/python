from itertools import permutations,product
            
## main
a = 2
b = 4
c = 7
d = 8
target = 29
numbers = ["a","b","c","d"]
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
        
        
for n in range(2,len(numbers)+1):
    for values in permutations(numbers, n):
        for oper in product(operators, repeat=len(numbers) - 1):
            if n == 3:
                ## pattern (a oper b) oper c
                valuesWithBracket = ["(" + values[0], values[1] + ")", values[2]]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
                ## pattern a oper (b oper c)
                valuesWithBracket = [values[0], "(" + values[1], values[2] + ")"]
                formula = "".join(o + v for o, v in zip([""] + list(oper), valuesWithBracket))
                eval_formula(formula)
            if n == 4:
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
