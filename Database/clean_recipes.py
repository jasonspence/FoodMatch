import xml.etree.ElementTree as xml
import json
import clean_recipes_functions as crf

# XML to List of Recipes
def parseCookbook(cookBook, filename):
    # Start with the root element
    root = xml.parse(filename)

    recipes = root.findall("recipe")
    for r in recipes:
        recipeName = r.get("description")
        #print(recipeName)
        newRecipe = []
        newRecipe.append(recipeName)

        newIngredients = []
        ingredients = r.findall("RecipeItem")
        for i in ingredients:
            ingredientName = i.get("ItemName").split(",")[0]
            #print("    ", ingredientName)
            newIngredients.append(ingredientName)
        newRecipe.append(newIngredients)

        instructions = r.find("XML_MEMO1").text
        #print(instructions)
        newRecipe.append(instructions)

        cookBook.append(newRecipe)

    return cookBook

# XML to Dict of Recipes
def parseCookbookDictionary(cookBook=None, filename=None):
    # Start with the root element
    root = xml.parse(filename)

    if (cookBook == None):
        cookBook = {"Cookbook": []}

    recipes = root.findall("recipe")
    for r in recipes:
        recipeName = r.get("description")
        #print(recipeName)
        newRecipe = {}
        newRecipe["Name"] = recipeName
        newRecipe["Ingredients"] = []
        ingredients = r.findall("RecipeItem")
        for i in ingredients:
            ingredientName = i.get("ItemName").split(",")[0]
            #print("    ", ingredientName)
            newRecipe["Ingredients"].append({"Ingredient": ingredientName})

        instructionsDiv = r.find("XML_MEMO1")
        if (instructionsDiv != None):
            instructions = instructionsDiv.text
        else:
            instructions = "Method:/n/nNone"
        #print(instructions)
        newRecipe["Instructions"] = instructions

        cookBook["Cookbook"].append({"Recipe": newRecipe})

    return cookBook
    
def makeXML(xmlRoot, Array):
    for r in Array:
        recipeName = r[0]
        #print(recipeName)
        newRecipe = xml.Element("Recipe")
        newRecipe.text = recipeName
        
        for i in r[1]:
            ingredientName = i
            #print("    ", ingredientName)
            newIngredient = xml.Element("Ingredient")
            newIngredient.text = ingredientName
            newRecipe.append(newIngredient)
        xmlRoot.append(newRecipe)
    
    return xmlRoot

def printXMLCookbook(book):
    recipes = book.findall("Recipe")
    for r in recipes:
        recipeName = r.text
        print(recipeName)
        ingredients = r.findall("Ingredient")
        for i in ingredients:
            ingredientName = i.text
            print("    ", ingredientName)

def printCookbook(book):
    for r in book:
        recipeName = r[0]
        print(recipeName)
        for i in r[1]:
            ingredientName = i
            print("    ", ingredientName)
        print(r[2])

if __name__ == "__main__":
    outFilenameXML  = "./Cookbook.xml"
    outFilenameJSON = "./Cookbook.json"

    cookDict = parseCookbookDictionary(filename="./ESHA+Recipes+(EXL+Files)/CommonRecipes.exl")
    #cookDict = parseCookbookDictionary(cookDict, "./ESHA+Recipes+(EXL+Files)/ArmedForcesRecipes.exl")
    
    cookDict, duplicates = crf.removeDuplicates(cookDict)
    
    print(json.dumps(cookDict))
    print(duplicates, "duplicates")
    with open(outFilenameJSON, "w") as file_object:
        json.dump(cookDict, file_object)
    quit()

    # Import and parse cookbooks
    #cookBook = []
    #cookBook = parseCookbook(cookBook, "./ESHA+Recipes+(EXL+Files)/CommonRecipes.exl")
    #cookBook = parseCookbook(cookBook, "./ESHA+Recipes+(EXL+Files)/EthnicRecipes.exl")
    #cookBook = parseCookbook(cookBook, "./ESHA+Recipes+(EXL+Files)/VegetarianRecipes.exl")
    #cookBook = parseCookbook(cookBook, "./ESHA+Recipes+(EXL+Files)/ArmedForcesRecipes.exl")
    #printCookbook(cookBook)
    #print("DONE THE LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST")

    # Edit the entries
    cookBook, duplicates = crf.removeDuplicates(cookBook)
    cookBook = crf.splitInstructions(cookBook)
    #printCookbook(cookBook)
    print(duplicates, "duplicates")

    # Convert back to XML
    cookBookRoot = xml.Element("Cookbook")
    cookBookRootPlusChildren = makeXML(cookBookRoot, cookBook)
    cookBookTree = xml.ElementTree(cookBookRootPlusChildren)

    #printXMLCookbook(cookBookTree)
    cookBookTree.write(outFilenameXML)
