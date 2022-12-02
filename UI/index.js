const ohjeet = document.querySelector('#ohjeet');
const pisteet = document.querySelector('#pisteet');
const dialog = document

[ohjeet, pisteet].forEach(item => {
  item.addEventListener('click', (e) => {
    e.preventDefault();

  });
});