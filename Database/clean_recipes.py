import xml.etree.ElementTree as xml

# XML to List of Recipes and 
def parseCookbook(cookBook, filename):
    # Start with the root element
    root = xml.parse(filename)

    recipes = root.findall("recipe")
    for r in recipes:
        recipeName = r.get("description")
        #print(recipeName)
        newRecipe = []
        newRecipe.append(recipeName)
        
        ingredients = r.findall("RecipeItem")
        for i in ingredients:
            ingredientName = i.get("ItemName").split(",")[0]
            #print("    ", ingredientName)
            newRecipe.append(ingredientName)
        cookBook.append(newRecipe)

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

if __name__ == "__main__":
    outFilename = "./Cookbook.xml"

    cookBook = []
    cookBook = parseCookbook(cookBook, "./ESHA+Recipes+(EXL+Files)/CommonRecipes.exl")
    printCookbook(cookBook)
    print("DONE THE LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST")

    cookBookRoot = xml.Element("Cookbook")
    cookBookRootPlusChildren = makeXML(cookBookRoot, cookBook)
    cookBookTree = xml.ElementTree(cookBookRootPlusChildren)

    printXMLCookbook(cookBookTree)
    cookBookTree.write(outFilename)

    print(cookBook)