import React from "react";
import "./seleccion-secuencias.scss"

export class SeleccionSecuencia extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return(
            <div className='contenedor-secuencias'>
                {this.props.mostrarSeleccionSecuencias &&
                <div>
                    {
                        this.props.secuenciasParaElegir.map(secuencia => {
                            return (
                                <div className='contenedor-secuencia'>
                                    <span className='texto-secuencia'>{secuencia}</span>
                                </div>)
                        })
                    }
                </div>
                }
            </div>
        )
    }
}
