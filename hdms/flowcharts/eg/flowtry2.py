from graphviz import Digraph

dot = Digraph(comment='A Round Graph')

# Adding nodes
dot.attr('node', shape='box')
dot.node('A', 'End User')
dot.node('B', 'Communication Channels')
dot.node('C', 'Helpdesk Operator')
dot.node('D', 'Helpdesk Software')
dot.node('E', 'Support Team Member(s) of Department(s)')
dot.node('F', 'Chatbot')
dot.attr('node', shape='cylinder')
dot.node('G', 'Solution Bank')
dot.node('H', 'Database')

# Adding edges
dot.edges(['AB', 'AD', 'BC', 'BD', 'BF', 'CB', 'DE', 'DA', 'DH', 'ED', 'FG'])

# saving source code
dot.format = 'png'
dot.render('Graph', view=True)
