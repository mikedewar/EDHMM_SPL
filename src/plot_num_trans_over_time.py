import cPickle as pk
import pylab as pb

fh = open('W_exp3.dat')
W = []
while True:
    try:
        W.append(pk.load(fh))
    except EOFError:
        break

W = pb.array(W)
W = W.reshape((len(W)/500,500))

burnin=500

pb.figure(figsize=(6,2))
pb.plot(pb.mean(W,1)[burnin:burnin+1000], 'k-', lw=1)
pb.xlabel('iteration',{"family":"Times New Roman", "color":"black"})
pb.ylabel('number of transitions visited',{"family":"Times New Roman", "color":"black"})
pb.xlim((0,1000))
pb.subplots_adjust(bottom=0.21)
#pb.show()
pb.savefig('../pic/number_transitions_visited.pdf')


        
