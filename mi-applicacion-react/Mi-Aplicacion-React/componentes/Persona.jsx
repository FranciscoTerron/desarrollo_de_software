import React from "react";

const Persona = ({nombre,edad,ocupacion}) =>{
    return(
        <div className="contenedor-personas">
            <h2>Nombre : {nombre}</h2>
            <p>Edad: {edad}</p>
            <p>Ocupacion: {ocupacion} </p>
        </div>





    );
};

export default Persona;