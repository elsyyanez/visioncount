// Inicializar Firebase
const firebaseConfig = {
    apiKey: "AIzaSyAG9HlMWoXjUC7ub5Dp7OvZnSyPL8nrb1g",
    authDomain: "integradora-2-51f86.firebaseapp.com",
    projectId: "integradora-2-51f86",
    storageBucket: "integradora-2-51f86.appspot.com",
    messagingSenderId: "752846426914",
    appId: "1:752846426914:web:6f0915c872335e5678cb7b"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();

// Evento al hacer clic en el botón "Confirmar"
document.getElementById("confirmar-btn").addEventListener("click", async () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        // Intentar iniciar sesión
        const userCredential = await auth.signInWithEmailAndPassword(email, password);
        
        // Si el inicio de sesión es exitoso, redirigir
        alert("Inicio de sesión exitoso");
        window.location.href = "administrador/bienvenida_admin.html"; 

    } catch (error) {
        // Mostrar mensaje de error
        alert("Datos incorrectos. Verifica tu correo y contraseña.");
    }
});
