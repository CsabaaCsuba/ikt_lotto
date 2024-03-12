const defaultPage = "sorsolasok";

const rightSide = document.getElementById("jobb");

var currentPage = defaultPage;

const pages = {
    "sorsolasok":{title:"<h1>Korábbi sorsolások</h1>", body:"<h2>Az előző heti nyerőszámok</h2><div id='szamsor1' class='szam-container'></div><h2>A múlt heti nyerőszámok</h2><div class='szam-container' id='szamsor2'></div>"},
    "leggyakoribb":{title:"<h1>Leggyakoribb számok</h1>", body:"<h2>#1</h2><h2>#2</h2><h2>#3</h2>"},
    "leghasonlobb":{title:"<h1>Leghasonlóbb számok</h1>", body:"<h2></h2><div></div><h2></h2><div></div>"},
    "leghoszabb":{title:"<h1>A 3 leghoszabb sorozatot tartalmazó számsor</h1>", body: ""},
    "legkisebb":{title:"<h1>A 3 legkisebb összegű számsor</h1>", body: ""},
    // "grafikonok":{title:"<h1>Grafikonok</h1>", body:""},
    "erdekessegek":{title:"<h1>Érdekességek</h1>", body:'<div id="erdekessegek-szoveg"><p>Ebben még nem volna semmi rendkívüli, de öt hónapon belül már másodszor történt meg vele a dolog. A 88 éves asszonynak nincsenek is szerencseszámai, amikor december 23-án megvásárolta a szelvényt, a gépre bízta, melyik számsort játssza meg (ihletet keresőknek a nyertes számok a következők voltak: 8, 13, 20, 21, 27).</p><p>Ezzel meg is lett a jackpot, nyereménye pedig 138 000 dollár volt (ez kb. 40 millió forint).Ez a decemberi lottóvásárlás szinte 5 hónapra pontosan azután történt, hogy 2020. július 21-én megnyerte a főnyereményt, így egyáltalán nem számított rá, hogy akár egyetlen találata is lehet.</p><p>Nyáron kicsit kevesebbet, 94 000 dollárt (kb. 27 és félmillió forintot) nyert, azt a szelvényt férje vásárolta neki ugyanabban a boltban, mint ahol ő vette a mostanit (és ahol egyébként évek óta mindig megteszik ugyanezt).És hogy melyek voltak a nyári szerencseszámok? 2, 3, 12, 14, 28, ezeket szintén a gép választotta ki.</p></div>'}
}

const golyok = ["assets/golyo_piros.png", "assets/golyo_sarga.png", "assets/golyo_zold.png", "assets/golyo_kek.png", "assets/golyo_lila.png", ]



let loadPage = async (page) => {
    let pageData = pages[page];
    let response = await fetch(`http://127.0.0.1:8000/${page}`).then(result=>result.json())
    rightSide.innerHTML = ""+pageData.title
    rightSide.innerHTML += pageData.body
    // .then(response=>console.log(response.json()))
    // .catch(e=>console.log(e));
    // console.log(pageData)
    console.log("response: ",response)
    if (page == "sorsolasok"){
        var szamsor1 = document.getElementById("szamsor1")
        var szamsor2 = document.getElementById("szamsor2")
        for (let i=0; i<response.ny1.length;i++){
            szamsor1.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${response.ny1[i]}</span></div>`;
        }

        for (let i=0; i<response.ny2.length;i++){
            szamsor2.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${response.ny2[i]}</span></div>`;
        }

    }
    if (page == "leggyakoribb"){
        var numbers = response.gyakoriak;
        var gyakorisaguk = response.kihuzasuk;
        rightSide.innerHTML = pageData.title;
        for (let i=0; i<numbers.length; i++){
            
            rightSide.innerHTML += `<span class="leggyakoribb-szamok"><span>#${i+1}</span><div class="displayedGolyoDiv" style="background:url(${golyok[1]});background-size: 100% 100%;"><span class="number-inside-img">${numbers[i]}</span></div> - ${gyakorisaguk[i]}db</span>`
        }   
    }
    if (page == "leghasonlobb"){
        var hasonloak = response.hasonloak;
        var egyikszamsor = hasonloak.egyikszamsor;
        var masikszamsor = hasonloak.masikszamsor;
        console.log("egyik számsor:",egyikszamsor)
        console.log("másik számsor:",masikszamsor)

        rightSide.innerHTML += `<h2>${egyikszamsor.datum}</h2>`
        rightSide.innerHTML += '<div id="szamsor1"  class="szam-container"></div'
        var szamsor1 = document.getElementById("szamsor1")
        for (let i=0; i<5;i++){
            szamsor1.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${egyikszamsor.szamok[i]}</span></div>`;
        }
        rightSide.innerHTML += `<h2>${masikszamsor.datum}</h2>`
        rightSide.innerHTML += '<div id="szamsor2" class="szam-container"></div'
        var szamsor2 = document.getElementById("szamsor2")
        for (let i=0; i<5;i++){
            szamsor2.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${masikszamsor.szamok[i]}</span></div>`;
        }
    }

    if (page == "leghoszabb"){
        const szamsor1 = response.leghoszabbak.szamsor0
        const szamsor2 = response.leghoszabbak.szamsor1
        const szamsor3 = response.leghoszabbak.szamsor2
        console.log(szamsor1)
        console.log(szamsor2)
        console.log(szamsor3)

        rightSide.innerHTML += `<h2>${szamsor1.szamsorhossz} egymást követő szám</h2>`
        rightSide.innerHTML += '<div id="szamsor1" class="szam-container"></div'
        var szamsordiv1 = document.getElementById("szamsor1")

        for (let i=0; i<szamsor1.szamok.length; i++){
            szamsordiv1.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${szamsor1.szamok[i]}</span></div>`;
        }

        rightSide.innerHTML += `<h2>${szamsor2.szamsorhossz} egymást követő szám</h2>`
        rightSide.innerHTML += '<div id="szamsor2" class="szam-container"></div'
        var szamsordiv2 = document.getElementById("szamsor2")
        for (let i=0; i<szamsor2.szamok.length; i++){
            szamsordiv2.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${szamsor2.szamok[i]}</span></div>`;
        }
        rightSide.innerHTML += `<h2>${szamsor3.szamsorhossz} egymást követő szám</h2>`
        rightSide.innerHTML += '<div id="szamsor3" class="szam-container"></div'
        var szamsordiv3 = document.getElementById("szamsor3")
        for (let i=0; i<szamsor3.szamok.length; i++){
            szamsordiv3.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${szamsor3.szamok[i]}</span></div>`;
        }
    }

    if (page == "legkisebb"){
        var legkisebbek = response.legkisebbek;

        rightSide.innerHTML += `<h2>Összeg: ${legkisebbek.szamsor0.szamsorosszeg}</h2>`
        rightSide.innerHTML += '<div id="szamsor1" class="szam-container"></div>'
        const szamsor1 = document.getElementById("szamsor1")
        for (let i=0; i<legkisebbek.szamsor0.szamok.length; i++){
            szamsor1.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${legkisebbek.szamsor0.szamok[i]}</span></div>`;
        }

        rightSide.innerHTML += `<h2>Összeg: ${legkisebbek.szamsor1.szamsorosszeg}</h2>`
        rightSide.innerHTML += '<div id="szamsor2" class="szam-container"></div>'
        const szamsor2 = document.getElementById("szamsor2")
        for (let i=0; i<legkisebbek.szamsor1.szamok.length; i++){
            szamsor2.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${legkisebbek.szamsor1.szamok[i]}</span></div>`;
        }

        rightSide.innerHTML += `<h2>Összeg: ${legkisebbek.szamsor2.szamsorosszeg}</h2>`
        rightSide.innerHTML += '<div id="szamsor3" class="szam-container"></div>'
        const szamsor3 = document.getElementById("szamsor3")
        for (let i=0; i<legkisebbek.szamsor2.szamok.length; i++){
            szamsor3.innerHTML += `<div class="displayedGolyoDiv" style="background:url(${golyok[i]});background-size: 100% 100%;"><span class="number-inside-img">${legkisebbek.szamsor2.szamok[i]}</span></div>`;
        }
    }

    // let responseData = response.json()
    
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