//const jsonPath = "../Database/Cookbook.json"
const jsonPath = "https://jasonspence.github.io/WeGotThis/Database/Cookbook.json";

const request = async (jsonPath) => {
    const response = await fetch(jsonPath);
    const data = await response.json();
    console.log(data);
    return data;
}

const main = async (jsonPath) => {
    data = await request(jsonPath)
    
    let ingredients = new Set();

    //let promises = data.Cookbook.map( item => console.log(item.Recipe.Name) );
    for(let recipe of data.Cookbook) {
        //console.log(recipe.Recipe.Name);
        for(let ing of recipe.Recipe.Ingredients) {
            ingredients.add(ing.Ingredient);
        }
    }
    console.log(ingredients);

    var ingredients_container = document.getElementById("ingredients_container");
    var ingredients_chosen = document.getElementById("ingredients_chosen");
    for(let ing of ingredients) {
        ingredients_container.innerHTML += '<p class="ingredient">' + ing + '</p>';
        if (Math.random(1) < 0.01) {
            ingredients_chosen.innerHTML += '<p class="ingredient">' + ing + '</p>';
        }
    }
}


main(jsonPath)

