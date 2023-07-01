function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdownContent");
    dropdownContent.style.display = dropdownContent.style.display === "none" ? "block" : "none";
  }
  
  function openWindowCentered(url, title, width, height) {
    console.log("funcion ventana");
    var left = (screen.width / 2) - (width / 2);
    var top = (screen.height / 2) - (height / 2);
    
    window.open(url, title, 'width=' + width + ',height=' + height + ',top=' + top + ',left=' + left);
  }
  
  
  
