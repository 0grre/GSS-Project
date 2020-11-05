//scrollbar
window.addEventListener('scroll', function() {
    // A chaque fois que l'utilisateur va scroller (descendre la page)
    let y = window.scrollY; // On récupérer la valeur du scroll vertical
    console.log(y)

//si cette valeur > à 550 on ajouter la class
    if (y >= 550) {
        document.getElementById("mainNav").className = "navbar navbar-expand-lg navbar-light fixed";
    } else {
        // sinon, on l'enlève
        document.getElementById("mainNav").className = "navbar navbar-expand-lg navbar-light";
    }
  });


  