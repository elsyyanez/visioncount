import pyrebase

config = {
    apiKey: "AIzaSyAG9HlMWoXjUC7ub5Dp7OvZnSyPL8nrb1g",
    authDomain: "integradora-2-51f86.firebaseapp.com",
    projectId: "integradora-2-51f86",
    storageBucket: "integradora-2-51f86.appspot.com",
    messagingSenderId: "752846426914",
    appId: "1:752846426914:web:6f0915c872335e5678cb7b"
}

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Función de inicio de sesión
document.getElementById("login-btn").addEventListener("click", () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            alert("Inicio de sesión exitoso");
            window.location.href = "administrador/bienvenida_admin.html"; // Redirige al panel de administrador
        })
        .catch((error) => {
            alert("Error al iniciar sesión: " + error.message);
        });
});