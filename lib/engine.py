"""Production engine for fleet MIDI service."""
import json
def process(v, base=60):
    n=[base]
    for x in v:
        if x==1: n.append(n[-1]+4)
        elif x==-1: n.append(n[-1]-4)
        else: n.append(n[-1])
    return n
def stats(v):
    return {'density':sum(1 for x in v if x!=0)/len(v),'balance':(sum(1 for x in v if x==1)-sum(1 for x in v if x==-1))/len(v)}
if __name__=='__main__':
    v=[1,0,-1,1,0,-1,1,1]
    print(json.dumps({'notes':process(v),'stats':stats(v)}))
