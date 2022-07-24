console.log('Hello Tenzin')

function savePost(){
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDescription").value
    price = document.getElementById("newPrice").value
    seller = document.getElementById("newSeller").value
  
    axios.post("", {title : title, description : description, price : price, seller : seller}).then((response) => {
      window.location.href = "../../"
      })
  
  }
  
  function editPost(){
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDescription").value
    price = document.getElementById("newPrice").value
    seller = document.getElementById("newSeller").value
  
    axios.post("", {title : title, description : description, price : price, seller : seller}).then((response) => {
      window.location.href = "../../../"
      })
  
  }

  