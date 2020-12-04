import React from "react";
import "./homepage.scss"

export class Homepage extends React.Component {
    render() {
        return(
            <div className='homepage'>
                <div className='titulo'>
                    <span>¿Qué proteína analizamos hoy?</span>
                </div>
                <div className='input-codigo-pdb'>
                    <input type='text'/>
                    <button className='boton-consulta-pdb'>
                        ¡Vamos!
                    </button>
                </div>
            </div>
        )
    }
}
