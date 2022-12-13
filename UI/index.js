'use strict';

const ohjeet = document.getElementById('ohjeet');
const pisteet = document.querySelector('#pisteet');
const dialog = document.querySelector('main').appendChild(document.createElement('dialog'));

const apiURL = 'http://127.0.0.1:3000';
const startLoc = 'EFHK';


ohjeet.addEventListener('click', (e) => {
    e.preventDefault();

    const txt = new XMLHttpRequest();
    txt.open('GET', 'ohjeet.txt');
    txt.onreadystatechange = () => {
        dialog.innerText = txt.responseText;
    };
    txt.send();

    dialog.showModal();
    dialog.addEventListener('click', () => dialog.close());
});

pisteet.addEventListener('click', async function (e) {
    e.preventDefault();

    const highscore = await fetch('http://127.0.0.1:3000/testipisteet');
    const resp = await highscore.json();
    let pelaajalista = [];

    for (let pelaaja of resp) {
        const pelaajaobjekti = {
            spot: pelaaja.spot,
            name: pelaaja.name,
            score: pelaaja.score,
        };

        pelaajalista.push(pelaajaobjekti)
        console.log(pelaajaobjekti)

        dialog.innerText = new Tabulator("dialog", {
            data: pelaajalista,
            autoColumns: true,
        })
        dialog.showModal();
    }
});


// pelinluonti

async function pelinaloitus(url) {

}

const iframe = document.createElement("iframe");
iframe.src = "kartta.html";
document.querySelector(".map").appendChild(iframe);