var jsonPath = "../Database/Cookbook.json"

console.log("THIS IS WORKING")

//var mydata = JSON.parse(data)

/*
function readJSON(path) { 
    var xhr = new XMLHttpRequest(); 
    xhr.open('GET', path, true); 
    xhr.responseType = 'blob'; 
    xhr.onload = function(e) {  
      if (this.status == 200) { 
          var file = new File([this.response], 'temp'); 
          var fileReader = new FileReader(); 
          fileReader.addEventListener('load', function(){ 
               //do stuff with fileReader.result 
               console.log("Hello")
          }); 
          fileReader.readAsText(file); 
      }  
    } 
    xhr.send(); 
} 
readJSON(jsonPath)
*/

const request = async (jsonPath) => {
    const response = await fetch(jsonPath);
    const data = await response.json();
    console.log(data);

    for(const recipe in data.Cookbook) {
        console.log(recipe.Name)
    }
}

request(jsonPath)


