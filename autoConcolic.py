import ast
import astor
import concolic
import sys
def replaceVarWithConcolicGet(expr):
    if isinstance(expr, ast.Name):
        return ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='get', ctx=ast.Load()), args=[ast.Constant(value = expr.id)], keywords=[])
    elif isinstance(expr, ast.Constant):
        return ast.Constant(expr.value)
    elif isinstance(expr, ast.NamedExpr):
        print("named expression: " + ast.dump(expr))
    elif isinstance(expr, ast.BoolOp):
        values = []
        for x in expr.values:
            values.append(replaceVarWithConcolicGetGuard(x))
        print("OPERATION:  " + ast.dump(expr.op))
        if isinstance(expr.op, ast.And):
            return ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='And', ctx=ast.Load()), args=values, keywords=[])
        else:
            return ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='Or', ctx=ast.Load()), args=values, keywords=[])
    elif isinstance(expr, ast.BinOp):
        left = replaceVarWithConcolicGet(expr.left)
        right = replaceVarWithConcolicGet(expr.right)
        print('binop ' )
        return ast.BinOp(left, expr.op, right)
    elif isinstance(expr, ast.UnaryOp):
        ex = replaceVarWithConcolicGet(expr.operand)
        return ast.UnaryOp(expr.op, ex)
    elif isinstance(expr, ast.IfExp):
        test = replaceVarWithConcolicGet(expr.test)
        body = replaceVarWithConcolicGet(expr.body)
        orelse = replaceVarWithConcolicGet(expr.orelse)
        return ast.IfExp(test, body, orelse)
    elif (isinstance(expr, ast.Call)):
        print("callin: " + ast.dump(expr))
    elif isinstance(expr, ast.Compare):
        left = replaceVarWithConcolicGet(expr.left)
        ops = expr.ops
        comparators = []
        for c in expr.comparators:
            comparators.append(replaceVarWithConcolicGet(c))
        return ast.Compare(left,expr.ops, comparators)
    return ast.Constant(value = True)

def replaceVarWithConcolicGetGuard(expr):
    if isinstance(expr, ast.Name):
        return ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='get', ctx=ast.Load()), args=[ast.Constant(value = expr.id)], keywords=[])
    elif isinstance(expr, ast.Constant):
        return ast.Constant(expr.value)
    elif isinstance(expr, ast.NamedExpr):
        print("named expression: " + ast.dump(expr))
    elif isinstance(expr, ast.BoolOp):
        values = []
        for x in expr.values:
            values.append(replaceVarWithConcolicGetGuard(x))
        print("OPERATION:  " + ast.dump(expr.op))
        if isinstance(expr.op, ast.And):
            return ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='And', ctx=ast.Load()), args=values, keywords=[])
        else:
            return ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='Or', ctx=ast.Load()), args=values, keywords=[])
    elif isinstance(expr, ast.BinOp):
        left = replaceVarWithConcolicGetGuard(expr.left)
        right = replaceVarWithConcolicGetGuard(expr.right)
        print('binop ' )
        return ast.BinOp(left, expr.op, right)
    elif isinstance(expr, ast.UnaryOp):
        ex = replaceVarWithConcolicGetGuard(expr.operand)
        return ast.UnaryOp(expr.op, ex)
    elif isinstance(expr, ast.IfExp):
        test = replaceVarWithConcolicGetGuard(expr.test)
        body = replaceVarWithConcolicGetGuard(expr.body)
        orelse = replaceVarWithConcolicGetGuard(expr.orelse)
        return ast.IfExp(test, body, orelse)
    elif (isinstance(expr, ast.Call)):
        print("callin: " + ast.dump(expr))
    elif isinstance(expr, ast.Compare):
        left = replaceVarWithConcolicGetGuard(expr.left)
        ops = expr.ops
        comparators = []
        for c in expr.comparators:
            comparators.append(replaceVarWithConcolicGetGuard(c))
        return ast.Compare(left,expr.ops, comparators)
    return ast.Constant(value = True)

def insertConcolicOnFunction(function):
    i = 0
    while i < len(function):
        node = function[i]
        print("pp hard: " + ast.dump(node))
        if isinstance(node, ast.If):
            guard = replaceVarWithConcolicGetGuard(node.test)
            guardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuard = (ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='Not', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[notGuard], keywords=[]))
            node.body.insert(0,guardCall)
            node.orelse.insert(0, notGuardCall)
            insertConcolicOnFunction(node.body)
            insertConcolicOnFunction(node.orelse)
        elif isinstance(node, ast.While):
            guard = replaceVarWithConcolicGetGuard(node.test)
            guardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuard = ast.Call(func=ast.Attribute(value=ast.Name(id='z3', ctx=ast.Load()), attr='Not', ctx=ast.Load()), args=[guard], keywords=[])
            notGuardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[notGuard], keywords=[]))
            node.body.insert(0,guardCall)
            node.orelse.insert(0, notGuardCall)
            insertConcolicOnFunction(node.body)
            insertConcolicOnFunction(node.orelse)
        elif isinstance(node, ast.Assign):
            pos = function.index(node)
            if(not(function.index(node) - 1 >=0 and isinstance(function[function.index(node)], ast.Expr) and isinstance(function[pos].value, ast.Call) and function[pos].attr == 'set'  )):
                toAssign = replaceVarWithConcolicGet(node.value)
                for toAssignVar in node.targets:
                    if isinstance(toAssignVar, ast.Name):
                        print('varname: ' + '\'' + str(toAssignVar.id) + '\'')
                        toAssignExpr = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='set', ctx=ast.Load()), args=[ast.Constant(toAssignVar.id), node.value], keywords=[]))
                        function.insert(function.index(node)+1,toAssignExpr)
                   #     i
                    else:
                        print(ast.dump(toAssignVar))
        elif isinstance(node, ast.Assert):
            assertGuard = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[replaceVarWithConcolicGetGuard(node.test)], keywords=[]))
            function.insert(function.index(node)+1, assertGuard)
        i += 1

isFile = False
toRead = ''
shouldWrite = False
toWrite = ''
isFileOut = False;
for x in sys.argv:
    if isFile:
        toRead = x
        isFile = False
    if x == '-r':
        isFile = True
    if x == '-w':
        shouldWrite = True
    if x == '-f': #write to file after this
        isFileOut = True
    if isFileOut:
        toWrite = x
        isFileOut = False
splitFile = toRead.split('.')
assert(len(splitFile) == 2 and splitFile[1] == 'py' and len(splitFile[0]) > 0 , "Not a valid python filename for input!")



if toWrite == '' and shouldWrite:
    toWrite = ''.join(splitFile[0] + "-concolic.py")
    print(toWrite)
    
splitFile = toWrite.split('.')
assert(len(splitFile) == 2 and splitFile[1] == 'py' and len(splitFile[0]) > 0 , "Not a valid python filename for input!")

if toRead != '':
    with open(toRead, "r") as source:
        code = source.read()
        tree = ast.parse(code)
        code1 = compile(tree, filename="", mode="exec")
        print(astor.to_source(tree))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                insertConcolicOnFunction(node.body)
        print('/n/n/n')
        print(astor.to_source(tree))
        print('\n\n' + str(sys.argv))
    f = open(toWrite, "w")
    f.write(astor.to_source(tree))
    f.close()
    
