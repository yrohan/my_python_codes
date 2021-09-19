from nltk.corpus import sentiwordnet as swn

r1 = swn.senti_synset('breakdown.n.03')

print(r1)

print(r1.pos_score())
print(r1.neg_score())
print(r1.obj_score())

a1=swn.all_senti_synsets()

print(a1)