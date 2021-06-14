
const cargarUsuarios = async ()=>{
    
    let res = await axios.get("http://localhost:8000/usuarios/");
    usuarios = res.data;

    let cuerpoTabla = document.querySelector("#body-tabla");

    usuarios.forEach(i =>{

        let tr = document.createElement("tr");
        let tdNombre = document.createElement("td");
        let tdEmail = document.createElement("td");
        tdNombre.innerText = i.username;
        tdEmail.innerText = i.email;

        tr.appendChild(tdNombre);
        tr.appendChild(tdEmail);

        cuerpoTabla.appendChild(tr);

    });

};

cargarUsuarios();