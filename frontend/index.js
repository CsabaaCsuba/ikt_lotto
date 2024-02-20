const defaultPage = "sorsolasok";

const rightSide = document.getElementById("jobb");

var currentPage = defaultPage;

const pages = {
    "sorsolasok":{title:"<h1>Korábbi sorsolások</h1>", body:"<h3>Az előző heti nyerőszámok</h3><div id='elozohetiSzamok'></div><h3>A múlt heti nyerőszámok</h3><div id='multhetiSzamok'></div>"},
    "leggyakoribb":{title:"<h1>Leggyakoribb számok</h1>", body:"<h3>#1</h3><h3>#2</h3><h3>#3</h3>"},
    "leghasonlobb":{title:"<h1>Leghasonlóbb számok</h1>"},
    "leghoszabb":{title:"<h1>Leghoszabb számok</h1>"},
    "grafikonok":{title:"<h1>Grafikonok</h1>"},
    "erdekessegek":{title:"<h1>Érdekességek</h1>"}
}

let loadPage = (page) => {
    let pageData = pages[page];
    console.log(pageData)
    rightSide.innerHTML = ""+pageData.title
    rightSide.innerHTML += pageData.body
}

let onStart = () => {
    loadPage(defaultPage)
    var btns = document.getElementsByClassName("bal-point")
    for (let i=0; i<btns.length;i++){
        btns[i].addEventListener("click", ()=>{
            loadPage(btns[i].id);
        })
    }
    btns.array.forEach(element => {
        element.addEventListener("click", ()=>{
            loadPage(element.id);
        })
    });
}


onStart()