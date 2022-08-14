form = document.getElementById("updateForm");

function updateUser(id, name, email,password,phone) {
fetch("/users/" + id, {
    method: "PATCH",
    body: JSON.stringify({
      name,
      email,
      password,
      phone
    }),
  }).then((response) => response.json());
  window.location.reload();
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const phone = document.getElementById("phone").value;
  const id = document.getElementById("id").value;

  updateMovie(id, name, email, password, phone);
});

async function deleteuser(id) {
  const res = await fetch("/users/" + id, {
    method: "DELETE",
  }).then((response) => response.json());
  window.location.reload();
}
