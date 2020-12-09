import React from "react";
import "./informacion-secuencia.scss"
import MSAViewer from "react-msa-viewer";
import Viewer from "../viewer/Viewer";


export class InformacionSobreLaSecuencia extends React.Component {
    constructor(props) {
        
        super(props);
        this.state = {
            opcionSeleccionada: 1,
        }
    }

   

    render() {
        return(
            <div className='informacion-secuencia'>
                <div className='botonera'>
                    <div className='columna-boton'>
                        <button className='boton' onClick={() => this.setState({opcionSeleccionada: 1})}>
                            Ver alineamiento de secuencias
                        </button>
                    </div>
                    <div className='columna-boton'>
                        <button className='boton' onClick={() => this.setState({opcionSeleccionada: 2})}>
                            Ver estructura secundaria
                        </button>
                    </div>
                    <div className='columna-boton'>
                        <button className='boton' onClick={() => this.setState({opcionSeleccionada: 3})}>
                            Ver estructura terciaria
                        </button>
                    </div>
                </div>

                <div className='contenido'>
                    {this.state.opcionSeleccionada === 1 && <MSAViewer sequences={this.props.sequences}/>}
                    {this.state.opcionSeleccionada === 2 && <MSAViewer sequences={this.props.dssps}/>}
                    {this.state.opcionSeleccionada === 3 && <Viewer protein={this.props.codigoPdb}> </Viewer>}
                </div>
              

            </div>
        )
    }
}
