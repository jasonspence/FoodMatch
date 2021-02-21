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


const data = fetch(jsonPath)
.then(response => {
   return response.json();
})
.then(console.log("Hey did this work??"))
.then(data => console.log(data));

for(const recipe in data.Cookbook) {
    console.log(recipe.Name)
}
