const header = document.querySelector('header');
document.querySelector('#toggle_header').addEventListener('click', function () {
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
