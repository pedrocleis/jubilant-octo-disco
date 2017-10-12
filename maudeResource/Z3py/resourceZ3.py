from z3 import *
solv = Solver()
i = Const('i', IntSort())
j = Const('j', IntSort())
n = Const('n', IntSort())
m = Const('m', IntSort())
v = Const('v', IntSort())


limit = Int('limit')
S = Function('S', IntSort(), BoolSort())

solv.add(ForAll(n,Implies( n > limit, Not(S(n)))))

solv.add(ForAll(n,Implies(n < 0, Not(S(n)))))

solv.add(ForAll(n, Implies( And(n <= limit, n >= 0), S(n)))   )

rss = Function('rss', IntSort(), IntSort(), BoolSort())
rii = Function('rii', IntSort(), IntSort(), BoolSort())
solv.add(ForAll([i, n, m],  Implies(And(rss(i, n), rss(i, m)), n == m)))
solv.add(ForAll([i, n, m],  Implies(And(rii(i, n), rii(i, m)), n == m)))
#solv.add(ForAll(n, Implies(rss(0, n), n >= 0)))
#solv.add(ForAll(n, Implies(rii(0, n), n >= 0)))
#solv.add(S(0) == rss(0, 100)  )
#solv.add(S(0) ==  rii(0, 100) )

solv.add(ForAll([n], S(n) == Exists([v], rii(n, v) ) ))
solv.add(ForAll([n], S(n) == Exists([v], rss(n, v) ) ))

t_function = Function('t_function', IntSort(), IntSort(), BoolSort())
solv.add(
ForAll([i, j, n, m],
t_function(i, j) == And( And(S(i), S(j), j == i + 1 ),
Implies( And( rss(i,n), rii(i, m) ), And(rss(j, n- 20 ), rii(j, m -20)) ))
))

minRes = Int('minRes')

solv.add(minRes == 0)
solv.add(limit == 6)
solv.add(rss(0, 100))
solv.add(rii(0, 100))
solv.add(S(0))
solv.add(S(1))
solv.add(S(2))
solv.add(S(3))
solv.add(S(4))
solv.add(S(5))
solv.add(S(6))
#solv.add(S(7))
#solv.add(S(8))
#solv.add(S(9))
#solv.add(S(10))
solv.add(Exists([i, n], And(rss(i, n), n <= minRes) ))

print(solv.check() )
mod = solv.model()
for d in mod.decls() :
    print "%s = %s" % (d.name(), mod[d] )
