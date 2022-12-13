'use strict';

const koordinaatit = [
  {'icao': 'EFHK', 'koord1': 24.9497, 'koord2': 60.3183, 'maa': 'Suomi'},
  {'icao': 'ESSA', 'koord1': 17.9186, 'koord2': 59.6519, 'maa': 'Ruotsi'},
  {'icao': 'ENGM', 'koord1': 11.1004, 'koord2': 60.1939, 'maa': 'Norja'},
  {'icao': 'EETN', 'koord1': 24.8327, 'koord2': 59.41329, 'maa': 'Viro'},
  {'icao': 'EVRA', 'koord1': 23.9710, 'koord2': 56.9235, 'maa': 'Latvia'},
  {'icao': 'EYVI', 'koord1': 25.2858, 'koord2': 54.6341, 'maa': 'Liettua'},
  {'icao': 'EPWA', 'koord1': 20.9671, 'koord2': 52.1656, 'maa': 'Puola'},
  {'icao': 'UMMS', 'koord1': 28.0399, 'koord2': 53.8880, 'maa': 'Valko-Venäjä'},
  {'icao': 'UKBB', 'koord1': 30.8946, 'koord2': 50.34500, 'maa': 'Ukraina'},
  {'icao': 'LROP', 'koord1': 26.085, 'koord2': 44.5711, 'maa': 'Romania'},
  {'icao': 'LBSF', 'koord1': 23.4114, 'koord2': 42.6966, 'maa': 'Bulgaria'},
  {
    'icao': 'LWSK',
    'koord1': 21.6214,
    'koord2': 41.9616,
    'maa': 'Pohjois-Makedonia',
  },
  {'icao': 'LGAV', 'koord1': 23.9445, 'koord2': 37.9364, 'maa': 'Kreikka'},
  {'icao': 'LATI', 'koord1': 19.7206, 'koord2': 41.4146, 'maa': 'Albania'},
  {'icao': 'LYBE', 'koord1': 20.3090, 'koord2': 44.8184, 'maa': 'Serbia'},
  {'icao': 'LDZA', 'koord1': 16.0687, 'koord2': 45.74290, 'maa': 'Kroatia'},
  {'icao': 'LYPG', 'koord1': 19.2519, 'koord2': 42.3594, 'maa': 'Montenegro'},
  {'icao': 'LJLJ', 'koord1': 14.4576, 'koord2': 46.2237, 'maa': 'Slovenia'},
  {'icao': 'LHBP', 'koord1': 19.2610, 'koord2': 47.4297, 'maa': 'Unkari'},
  {'icao': 'LOWW', 'koord1': 16.5697, 'koord2': 48.1102, 'maa': 'Itävalta'},
  {'icao': 'LKPR', 'koord1': 14.26, 'koord2': 50.1008, 'maa': 'Tšekki'},
  {'icao': 'LZIB', 'koord1': 17.2126, 'koord2': 48.1702, 'maa': 'Slovakia'},
  {'icao': 'EDDB', 'koord1': 13.4938, 'koord2': 52.3513, 'maa': 'Saksa'},
  {'icao': 'EKCH', 'koord1': 12.6560, 'koord2': 55.6179, 'maa': 'Tanska'},
  {'icao': 'EHAM', 'koord1': 4.7638, 'koord2': 52.3086, 'maa': 'Alankomaat'},
  {'icao': 'EBBR', 'koord1': 4.4844, 'koord2': 50.9014, 'maa': 'Belgia'},
  {
    'icao': 'EGLL',
    'koord1': -0.4619,
    'koord2': 51.4706,
    'maa': 'Iso-Britannia',
  },
  {'icao': 'EIDW', 'koord1': -6.2700, 'koord2': 53.4212, 'maa': 'Irlanti'},
  {'icao': 'ELLX', 'koord1': 6.2044, 'koord2': 49.6233, 'maa': 'Luxemburg'},
  {'icao': 'LFPG', 'koord1': 2.55, 'koord2': 49.0127, 'maa': 'Ranska'},
  {'icao': 'LSZH', 'koord1': 8.5480, 'koord2': 47.4580, 'maa': 'Sveitsi'},
  {'icao': 'LIRF', 'koord1': 12.2519, 'koord2': 41.8045, 'maa': 'Italia'},
  {'icao': 'LNMC', 'koord1': 7.4196, 'koord2': 43.725, 'maa': 'Monaco'},
  {'icao': 'LESU', 'koord1': 1.4091, 'koord2': 42.3386, 'maa': 'Andorra'},
  {'icao': 'LEMD', 'koord1': -3.5626, 'koord2': 40.4719, 'maa': 'Espanja'},
  {'icao': 'LPPT', 'koord1': -9.1359, 'koord2': 38.7813, 'maa': 'Portugali'}];

const ohjeet = document.getElementById('ohjeet');
const pisteet = document.querySelector('#pisteet');
const dialog = document.querySelector('main').
    appendChild(document.createElement('dialog'));
let pelaajaid;
let sijainti;
let karsivallisyys;
let icao;
let icaot = [];
let esinekentat = [];
let kaydytkentat = [];

const apiURL = 'http://127.0.0.1:3000';
const startLoc = 'EFHK';

function kenttienarpominen() {
  for (let i = 0; i < koordinaatit.length; i++) {
    const tamaicao = koordinaatit[i].icao

    icaot[tamaicao] = i
    icaot['arvo'] = ''
  }


  // kissa kentälle

  const kissaluku = Math.floor((Math.random() * 36) + 1)
  icaot[kissaluku].arvo = 'Kissa'

  // 6 herkkutikkua

  for (let i = 1; i <= 6; i++) {
    let successful = false;
    while (!successful) {
      let kentanarvo = (Math.floor(Math.random() * 36) + 1)

      if (kentanarvo === kissaluku) {

      } else if (icaot[kentanarvo].arvo === '') {
        icaot[kentanarvo].arvo = 'Herkkutikku'
        successful = true;

      }

    }
  }

  // 5 tonnikalaa

  for (let i = 1; i <= 5; i++) {
    let successful = false;
    while (!successful) {
      let kentanarvo = (Math.floor(Math.random() * 36) + 1)

      if (kentanarvo === kissaluku) {

      } else if (icaot[kentanarvo].arvo === '') {
        icaot[kentanarvo].arvo = 'Tonnikala'
        successful = true;
      }
    }
  }

  // 4 kissanminttua

  for (let i = 1; i <= 4; i++) {
    let successful = false;
    while (!successful) {
      let kentanarvo = (Math.floor(Math.random() * 36) + 1)

      if (kentanarvo === kissaluku) {

      } else if (icaot[kentanarvo].arvo === '') {
        icaot[kentanarvo].arvo = 'Kissanminttu'
        successful = true;
      }
    }
  }

  return icaot
}

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
  const kenttienarvot = kenttienarpominen()


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
// document.querySelectorAll('.marker').
//     forEach().
//     addEventListener('click', async (e) => {
//       const inv = document.querySelector('.invlista');
//
//       const lento = await fetch(
//           `http://127.0.0.1:3000/matkusta?id=${+(pelaajaid.innerText)}&kohde=${this.id}`);
//       const tiedot = await lento.json();
//
//       // inventaario
//
//     });

// kartan lisäys

const iframe = document.createElement('iframe');
iframe.src = 'kartta.html';
document.querySelector('.map').appendChild(iframe);

