from pyflowchart import *

st = StartNode('End User')
op = OperationNode('Communication Channels')
sub = SubroutineNode('A Subroutine')
e = EndNode('End')

# define the direction the connection will leave the node from
sub.set_connect_direction("right")

st.connect(op)
op.connect(sub)
sub.connect(op)
sub.connect(e)

fc = Flowchart(st)
print(fc.flowchart())
