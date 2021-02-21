def removeDuplicates(cookbook):
    if type(cookbook) is list:
        return removeDuplicatesList(cookbook)
    elif type(cookbook) is dict:
        return removeDuplicatesDict(cookbook)

def removeDuplicatesDict(cookbook):
    duplicates = 0
    for i, recipe1 in enumerate(cookbook["Cookbook"]):
        for j, recipe2 in enumerate(cookbook["Cookbook"][i+1:], i+1):
            #print(i,j, recipe1, recipe2)
            if recipe1["Recipe"]["Ingredients"] == recipe2["Recipe"]["Ingredients"]:
                duplicates += 1
                #print(i,j,cookbook)
                #print(recipe1, recipe2, recipe1 == recipe2)
                #for k, char in enumerate(recipe1[0]):
                #    #print(k, char, recipe2[0][k])
                #    if char != recipe2[0][k]:
                #        break
                #else: 
                #    k += 1
                #if k > 0:
                #    recipe1[0] = recipe1[0][0:k]
                cookbook["Cookbook"].remove(recipe2)

    return cookbook, duplicates

def removeDuplicatesList(cookbook):
    duplicates = 0
    for i, recipe1 in enumerate(cookbook):
        for j, recipe2 in enumerate(cookbook[i+1:], i+1):
            #print(i,j, recipe1, recipe2)
            if recipe1[1] == recipe2[1]:
                duplicates += 1
                #print(i,j,cookbook)
                #print(recipe1, recipe2, recipe1 == recipe2)
                #for k, char in enumerate(recipe1[0]):
                #    #print(k, char, recipe2[0][k])
                #    if char != recipe2[0][k]:
                #        break
                #else: 
                #    k += 1
                #if k > 0:
                #    recipe1[0] = recipe1[0][0:k]
                cookbook.remove(recipe2)

    return cookbook, duplicates



def splitInstructions(cookbook):
    if type(cookbook) is list:
        return splitInstructionsList(cookbook)
    elif type(cookbook) is dict:
        return splitInstructionsDict(cookbook)

def splitInstructionsDict(cookbook):
    for recipe in cookbook["Cookbook"]:
        instructions = recipe["Recipe"].pop("Instructions").split("\n")
        method = None
        for i, inst in enumerate(instructions):
            if inst[:4] == "METH":
                method = i
                recipe["Recipe"]["Method"] = []
            elif inst[:4] == "YIEL":
                #recipe["Recipe"]["Yield"] = inst.split(" ")[-2]
                recipe["Recipe"]["Yield"] = inst[7:].strip()
            if (method != None) and (method < i) and (inst != ""):
                recipe["Recipe"]["Method"].append(inst)



    return cookbook

def splitInstructionsList(cookbook):
    #for i, recipe in enumerate(cookbook):
    #    instructions = recipe.pop(2)
    #    print(instructions)

    print("NOT IMPLEMENTED")
    return cookbook
