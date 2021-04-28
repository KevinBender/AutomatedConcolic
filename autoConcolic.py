import ast
import astor
import concolic
def replaceVarWithConcolicGet(expr):
#print(ast.dump(expr))
 #   print('\n')
    if isinstance(expr, ast.Name):
        return ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='get', ctx=ast.Load()), args=[ast.Constant(value = expr.id)], keywords=[])
    elif isinstance(expr, ast.Constant):
        return ast.Constant(expr.value)
    elif isinstance(expr, ast.BoolOp):
        values = []
        for x in expr.values:
            values.append(replaceVarWithConcolicGet(x))
      #  return ast.Constant(value = True)
        return ast.BoolOp(op = expr.op, values = values);
    elif isinstance(expr, ast.BinOp):
        left = replaceVarWithConcolicGet(expr.left)
        print('binop')
    elif isinstance(expr, ast.Compare):
        left = replaceVarWithConcolicGet(expr.left)
        ops = expr.ops
        comparators = []
        for c in expr.comparators:
            comparators.append(replaceVarWithConcolicGet(c))
        return ast.Compare(left,expr.ops, comparators)
    return ast.Constant(value = True)




with open("f1.py", "r") as source:
    code = source.read()
    tree = ast.parse(code)
    code1 = compile(tree, filename="", mode="exec")
    print(astor.to_source(tree))
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            guard = replaceVarWithConcolicGet(node.test)
            guardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[guard], keywords=[]))
            notGuard = value=ast.UnaryOp(op=ast.Not(), operand = guard)
            notGuardCall = ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='concolic', ctx=ast.Load()), attr='guard', ctx=ast.Load()), args=[notGuard], keywords=[]))
            for x in node.orelse:
                print("orelse: " + ast.dump(x))
            #print(node.body)
            #print(astor.to_source(node))
            node.body.insert(0,guardCall)
            node.orelse.insert(0, notGuardCall)
            #print(astor.to_source(node))
           #print(node.body)
    print('poopi\n\n\n')
    print(astor.to_source(tree))
    
