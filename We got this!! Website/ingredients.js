jsonPath = "../Database/Cookbook.json"

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


fetch("../Database/Cookbook.json")
.then(response => {
   return response.json();
})
.then(data => console.log(data));
