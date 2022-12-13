'use strict';

const ohjeet = document.getElementById('ohjeet');
const pisteet = document.querySelector('#pisteet');
const dialog = document.querySelector('main').
    appendChild(document.createElement('dialog'));
let pelaajaid;
let sijainti;
let karsivallisyys;
let icao;

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

pisteet.addEventListener('click', async function(e) {
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

    pelaajalista.push(pelaajaobjekti);
    console.log(pelaajaobjekti);

    dialog.innerText = new Tabulator('dialog', {
      data: pelaajalista,
      autoColumns: true,
    });
    dialog.showModal();
  }
});

function hidename() {
  document.querySelector('#nimikentta').style.display = 'None';
  document.querySelector('form').
      appendChild(
          document.createElement('p')).innerText = document.querySelector(
      '#nimikentta').value;
}

// pelinluonti

const aloitusnappi = document.querySelector('#aloitapeli');
aloitusnappi.addEventListener('click', async () => {
  document.querySelector('#aloitapeli').style.display = 'None';
  const infopalkki = document.querySelector('.infopalkki');

  const pelaajanimi = document.querySelector('#nimikentta').value;

  const pelinhaku = await fetch(
      `http://127.0.0.1:3000/uusi_peli?nimi=${pelaajanimi}`);
  const status = await pelinhaku.json();

  console.log(status);

  pelaajaid = infopalkki.appendChild(
      document.createElement('p'));
  sijainti = infopalkki.appendChild(
      document.createElement('p'));
  karsivallisyys = infopalkki.appendChild(document.createElement(
      'p'));

  pelaajaid.innerText = `Pelaaja-id: ${status.ID}`;
  sijainti.innerText = `Sijainti: ${status.Sijainti}`;
  karsivallisyys.innerText = `Kissan kärsivällisyys: ${+(status['Kisun kärsivällisyys']) -
  +(status['Käytetty kärsivällisyys'])}`;
});

// tähän kristiinan tekemät napit matkaanlähtöön
// document.querySelector('.lentonapit').
//     forEach().
//     addEventListener('click', async (e) => {
//       const inv = document.querySelector('.invlista');
//
//       const lento = await fetch(
//           `http://127.0.0.1:3000/matkusta?id=${+(pelaajaid.innerText)}&kohde=${this.id}`);
//       const tiedot = await lento.json();
//     });

// kartan lisäys

const iframe = document.createElement('iframe');
iframe.src = 'kartta.html';
document.querySelector('.map').appendChild(iframe);