const defaultPage = "sorsolasok";

const rightSide = document.getElementById("jobb");

var currentPage = defaultPage;

const pages = {
    "sorsolasok":{title:"<h1>Korábbi sorsolások</h1>", body:"<h2>Az előző heti nyerőszámok</h2><div id='elozohetiSzamok'></div><h2>A múlt heti nyerőszámok</h2><div id='multhetiSzamok'></div>"},
    "leggyakoribb":{title:"<h1>Leggyakoribb számok</h1>", body:"<h2>#1</h2><h2>#2</h2><h2>#3</h2>"},
    "leghasonlobb":{title:"<h1>Leghasonlóbb számok</h1>", body:"<h2></h2><div></div><h2></h2><div></div>"},
    "leghoszabb":{title:"<h1>A 3 leghoszabb sorozatot tartalmazó számsor</h1>", body: ""},
    "grafikonok":{title:"<h1>Grafikonok</h1>", body:""},
    "erdekessegek":{title:"<h1>Érdekességek</h1>", body:""}
}

let loadPage = async (page) => {
    let pageData = pages[page];
    let response = await fetch(`http://127.0.0.1:8000/${page}`).then(result=>result.json())
    // .then(response=>console.log(response.json()))
    // .catch(e=>console.log(e));
    console.log(pageData)
    console.log(response)
    // let responseData = response.json()
    rightSide.innerHTML = ""+pageData.title
    rightSide.innerHTML += pageData.body
}

let onStart = async () => {
    await loadPage(defaultPage)
    var btns = document.getElementsByClassName("bal-point")
    for (let i=0; i<btns.length;i++){
        btns[i].addEventListener("click", ()=>{
            loadPage(btns[i].id);
        })
    }

    // var allPages = document.getElementsByClassName("bal-point")
    // for (let i=0; i<allPages.length; i++){
    //     allPages[i].addEventListener("click", ())
    // }
    // btns.array.forEach(element => {
    //     element.addEventListener("click", ()=>{
    //         loadPage(element.id);
    //     })
    // });
}


onStart()