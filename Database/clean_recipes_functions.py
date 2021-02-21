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
    for i, recipe in enumerate(cookbook):
        instructions = recipe.pop(2)
        print(instructions)


    return cookbook
