from subprocess import call

def generateCode(dataPin, dataStates, dataFlow):
    ctextcode = "/* Code automatically generated by micro-controller GUI programming */\n\n#include <Wire.h>\n\n"

    ctextcode += initVariable(dataPin, dataStates, dataFlow)
    ctextcode += genSetup(dataPin, dataStates, dataFlow)
    ctextcode += genLoop(dataPin, dataStates, dataFlow)
    cCode = open("generatedCode.c","w")
    cCode.write(ctextcode)
    cCode.close()

def genSetup(dataPin, dataStates, dataFlow):
    code = "/* setup() function initialising the pin configuration */\n\n"
    indent = 0
    code += "void setup() {\n"
    indent += 1
    for d in list(dataPin.keys()):

        if d[0] == 'D':
            code += "\tpinMode("+dataPin[d][0]+", " + dataPin[d][2].upper() + ");\n"

            if dataPin[d][2] == "Output":
                if dataPin[d][1] != '' and int(dataPin[d][1]) > 0:
                    code += "\tdigitalWrite(" + dataPin[d][0] + ', HIGH);\n'
                elif dataPin[d][1] != '' and int(dataPin[d][1]) <= 0:
                    code += "\tdigitalWrite(" + dataPin[d][0] + ', LOW);\n'
                else:
                    pass
        elif d[0] == 'A':
            if dataPin[d][2] in ["SDA", "SCL"]:
                code += "\tWire.begin()\n"

            if dataPin[d][1] != '' and int(dataPin[d][1]) > 0:
                code += "\tanalogWrite(" + dataPin[d][0] + ', ' + dataPin[d][1] + ');\n'

    code += "}\n"
    return code

def initVariable(dataPin, dataStates, dataFlow):
    code = "\n/* initialisation of variables according to pin configuration*/\n\n"
    indent = 0
    indent += 1
    for d in list(dataPin.keys()):
        code += "int "+dataPin[d][0]+' = '+d[1:]+';\n'

    return code


def genLoop(dataPin, dataStates, dataFlow):
    code = "\n/* Switch case implementing the different states*/\n\n"

    code += "typedef enum {\n"
    for s in list(dataStates.keys()):
        code += "\t"+s+",\n"
    code += "} states;\n\n"
    initial_state = ""
    for s in list(dataStates.keys()):
        if "init" in dataStates[s][0]:
            initial_state = s
            code += "states s = " + s + ";\n"

    code += "\n/* The loop function runs over and over again forever */\n"
    indent = 0
    code += "void loop() {\n"
    indent += 1
    code += "\t"*indent + "switch(s){\n"
    indent += 1
    for s in list(dataStates.keys()):
        code += "\t"*indent +"case "+s+":\n"
        indent += 1
        code += genStateBlock(indent, s, dataPin, dataStates, dataFlow).replace("\n", "\n" + indent*"\t")

        if len(dataStates[s][1])==1:
            code += "\t"*indent + "s = "+ dataStates[s][1].pop() + ";\n"

        code += "\t"*indent + "break;\n"

        indent -= 1

    code += "\t"*indent +"default:\n"
    indent += 1
    code += "\t"*indent +"printf(\"Default case not admissible\");\n"
    indent -= 2
    code += "\t"*indent +"}\n"

    code += "}"

    return code


def genStateBlock(indent, state, dataPin, dataStates, dataFlow):
    code = ""

    for key in dataFlow[state]:
        line = key[0]

        i = line.index("##")

        if i > -1:
            j = line.index("__")

            if j > -1:
                shadow = line[i+2:j]
                if shadow in dataPin.keys():
                    code += "\t" * indent + line.replace(line[i:j+2], dataPin[shadow][0]) + "\n"
        else:
            code += "\t"*indent + line + "\n"

    return code
