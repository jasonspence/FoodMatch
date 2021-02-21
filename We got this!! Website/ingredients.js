//const jsonPath = "../Database/Cookbook.json"
const jsonPath = "https://jasonspence.github.io/WeGotThis/Database/Cookbook.json"

const request = async (jsonPath) => {
    const response = await fetch(jsonPath);
    const data = await response.json();
    console.log(data);
    return data
}

const main = async (jsonPath) => {
    data = await request(jsonPath)
    
    let ingredients = new Set()

    //let promises = data.Cookbook.map( item => console.log(item.Recipe.Name) );
    for(let recipe of data.Cookbook) {
        //console.log(recipe.Recipe.Name);
        for(let ing of recipe.Recipe.Ingredients) {
            ingredients.add(ing.Ingredient)
        }
    }

    console.log(ingredients)
}


main(jsonPath)

