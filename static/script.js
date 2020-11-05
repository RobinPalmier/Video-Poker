const logo = document.querySelectorAll('.logo');
const cards = document.querySelectorAll('.content-card');

// Fonction pour convertir les strings en boolean
function strToBool(str){
    if(str === 'true'){
        return true
    } else {
        return false
    }
}

// Fonction pour récupérer les cartes choisies
function getFirstHand(){
    let newHand = [];
    Array.from(cards[0].children).map(el => {
        newHand.push(strToBool(el.attributes['data-keep'].value))
    })

    return newHand;
}

// Fonction pour démarrer une nouvelle partie
function startNewGame(){
    location.href = "/game";
}

// Fonction pour relancer une partie :
function replay(){
    location.href = "/table";
}

// Fonction qui fait retourner à la page d'accueil
function backToHome(){
    location.href = "/";
}
logo[0].addEventListener("click", backToHome, true);

// Fonction qui permet de définir l'état de la carte :
function toggleStateCard(carte){
    let card = carte.getAttribute("data-card");
    let keep = carte.getAttribute("data-keep");
    let img = carte.getAttribute("src");
    
    if(img === "/static/img/cartes/back.png"){
        img = `/static/img/cartes/${card}.png`;
        keep = true;
    } else {
        img = `/static/img/cartes/back.png`;
        keep = false;
    }

    carte.setAttribute("data-card", card);
    carte.setAttribute("data-keep", keep);
    carte.setAttribute("src", img);
    getFirstHand();
}