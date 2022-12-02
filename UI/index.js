const ohjeet = document.getElementById('ohjeet');
const pisteet = document.querySelector('#pisteet');
const dialog = document.querySelector('main').
    appendChild(document.createElement('dialog'));

ohjeet.addEventListener('click', (e) => {
  e.preventDefault();

  const txt = new XMLHttpRequest();
  txt.open('GET', 'ohjeet.txt');
  txt.onreadystatechange = () => {
    const text = txt.responseText;
    dialog.innerText = text;
  };
  txt.send();

  dialog.showModal();
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

    pelaajalista.push(pelaajaobjekti)

    const table = new Tabulator("dialog", {
    data: pelaajalista,
    autoColumns: true,
});

  }

});