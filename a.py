import ast
import codegen
with open("f2.py", "r") as source:
    code = source.read()
    tree = ast.parse(code)
    print(ast.dump(tree))
Module(body=[Import(names=[alias(name='z3'), alias(name='concolic')]), Expr(value=



Call(func=Attribute(value=Name(id='concolic', ctx=Load()), attr='guard', ctx=Load()), args=[Constant(value=True)], keywords=[]))

], type_ignores=[])
