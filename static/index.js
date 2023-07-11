var modal = document.getElementById("myModal");
var btn = document.getElementById("openModalBtn");
var editBtns = document.getElementsByClassName("editBtn");
var span = document.getElementsByClassName("close");
var modalsEdit = document.getElementsByClassName("modal");
var spanEdit = document.getElementsByClassName("close");

btn.onclick = function() {
  modal.style.display = "block";
};

for (var i = 0; i < editBtns.length; i++) {
  editBtns[i].addEventListener("click", function() {
    var modalEdit = this.nextElementSibling;
    modalEdit.style.display = "block";
  });
}

for (var i = 0; i < span.length; i++) {
  span[i].onclick = function() {
    modal.style.display = "none";
  };
}

for (var i = 0; i < spanEdit.length; i++) {
  spanEdit[i].onclick = function() {
    var modalEdit = this.parentElement.parentElement;
    modalEdit.style.display = "none";
  };
}

window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  } else {
    for (var i = 0; i < modalsEdit.length; i++) {
      if (event.target === modalsEdit[i]) {
        modalsEdit[i].style.display = "none";
      }
    }
  }
};

function copyToClipboard(shortLink) {
  const base = 'http://127.0.0.1:5000/';
  const url = base + shortLink;
  const el = document.createElement('textarea');
  el.value = url;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);

  alert("Short link copied to clipboard!");
}
