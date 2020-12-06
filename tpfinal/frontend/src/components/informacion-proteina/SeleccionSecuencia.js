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
            <div className='container-padre'>
                {this.props.mostrarSeleccionSecuencias &&
                <div>
                    <p>Por favor, selecciona una secuencia</p>
                    <div className='contenedor-secuencias'>
                        <div>
                            {
                                this.props.secuenciasParaElegir.map(secuencia => {
                                    return (
                                        <div className='contenedor-secuencia'
                                             onClick={() => this.props.onSecuenciaSeleccionada(secuencia)}>
                                            <span className='texto-secuencia'>{secuencia}</span>
                                        </div>)
                                })
                            }
                        </div>
                    </div>
                </div>
                }
            </div>

        )
    }
}
