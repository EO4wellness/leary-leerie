document.body.addEventListener('click', function () {
     var myParent = document.getElementsByTagName("h1")[0]; 
     var myImage = document.createElement("img");
     myImage.src = 'https://thecatapi.com/api/images/get?format=src&type=gif';
     myParent.appendChild(myImage);
     myImage.style.marginLeft = "160px";
});
