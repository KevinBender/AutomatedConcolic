import ast
import astor
import concolic
import sys
def replaceVarWithConcolicGet(expr):
#print(ast.dump(expr))
 #   print('\n')
    if isinstance(expr, ast.Name):
        return ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='get', ctx=ast.Load()), args=[ast.Constant(value = expr.id)], keywords=[])
    elif isinstance(expr, ast.Constant):
        return ast.Constant(expr.value)
    elif isinstance(expr, ast.NamedExpr):
        print("named expression: " + ast.dump(expr))
    elif isinstance(expr, ast.BoolOp):
        values = []
        for x in expr.values:
            values.append(replaceVarWithConcolicGet(x))
      #  return ast.Constant(value = True)
        return ast.BoolOp(op = expr.op, values = values);
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


def insertConcolicOnFunction(function):
    for i in range(0, len(function)):
        node = function[i]
        if isinstance(node, ast.If):
            guard = replaceVarWithConcolicGet(node.test)
            guardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuard = value=ast.UnaryOp(op=ast.Not(), operand = guard)
            notGuardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[notGuard], keywords=[]))
            node.body.insert(0,guardCall)
            node.orelse.insert(0, notGuardCall)
            insertConcolicOnFunction(node.body)
            insertConcolicOnFunction(node.orelse)
        if isinstance(node, ast.While):
            guard = replaceVarWithConcolicGet(node.test)
            guardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuard = value=ast.UnaryOp(op=ast.Not(), operand = guard)
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
                        toAssignExpr = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='set', ctx=ast.Load()), args=[toAssignVar, node.value], keywords=[]))
                        function.insert(function.index(node)+1,toAssignExpr)
                        i = i+1;
                    else:
                        print(ast.dump(toAssignVar))


with open("f1.py", "r") as source:
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
    
