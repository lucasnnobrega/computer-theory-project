states=list(map(int,input("Enter States : ").split(" ")))
symbols=list(input("Enter Symbols : ").split(" "))
initial_state=int(input("Enter initial state : "))
final_states=list(map(int,input("Enter final states : ").split(" ")))

transitions=[]
inlists=[]

for i in range(len(symbols)):
    print("Enter transitions for symbol "+symbols[i]+" from all states :")
    for j in range(len(states)):
        inlists.append(int(input()))
    transitions.append(inlists)
    inlists=[]
cur_state=initial_state

while(True):
    cur_state=initial_state
    string=input("Enter string : ")

    if string=='#':
        break

    for symbol in string:
        print("["+str(cur_state)+"]"+"-"+symbol+"->",end="")
        cur_state=transitions[symbols.index(symbol)][cur_state]

    if cur_state in final_states:
        print("["+str(cur_state)+"]")
        print("String is accepted.")
    else:
        print("["+str(cur_state)+"]")
        print("String is not accepted.")
