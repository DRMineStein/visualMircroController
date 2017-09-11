from subprocess import call
call(["ls", "-l"])

def createGraph(dataStates, type, w, h):
    if type == 'FSM':
        graph = "digraph finite_state_machine {"+"\n"
        graph += "\t"+"rankdir=LR;"+"\n"
        graph += "\t"+"size=\"8,5\""+"\n"
        graph += "\t" + "node [shape = circle fontsize=10 fixedsize=TRUE];"+"\n"

        for key in dataStates.keys():
            for value in dataStates[key][0]:
                if value == 'init':
                    graph += "\t" + value + "->" + key + ";" +"\n"

            for value in dataStates[key][1]:
                graph += "\t" + key + "->" + value + ";" +"\n"
        graph += "}" + "\n"

    dotFile = open("state_graph.dot","w")
    dotFile.write(graph)
    dotFile.close()

    call("dot -Tpng -Gsize="+str(w/10)+","+str(h/10)+"\! -Gdpi=10 state_graph.dot > state_graph.png", shell=True)
    call("sips -s format gif state_graph.png --out state_graph.gif", shell=True)
    call("rm state_graph.png", shell=True)


def generateFlow(t, dataFlow,w,h):
    graph = "digraph " + t +"_flow {" + "\n"
    graph += "\t" + "size=\"8,5\"" + "\n"
    graph += "\t" + "node [shape = \"box\"];" + "\n"
    for d in dataFlow.keys():
        if t == d:
            graph += "\t" + dataFlow[d][1] + "->" + dataFlow[d][2] + ";" + "\n"
    graph += "}" + "\n"

    dotFile = open(t +"_flow.dot","w")
    dotFile.write(graph)
    dotFile.close()
    call("dot -Tpng -Gsize="+str(w/10)+","+str(h/10)+"\! -Gdpi=10 " + t + "_flow.dot > " + t + "_flow.png",
         shell=True)
    call("sips -s format gif " + t + "_flow.png --out " + t + "_flow.gif", shell=True)
    # call("rm " + t + "_flow.png", shell=True)