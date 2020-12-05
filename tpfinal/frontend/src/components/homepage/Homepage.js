import React from "react";
import "./homepage.scss"
import {SeleccionSecuencia} from "../informacion-proteina/SeleccionSecuencia";
import SequenceService from "../../services/SequenceService";

export class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pdbCode: '',
            mostrarSeleccionSecuencias: false,
            mostrarErrorDeCodigoPdb: false
        }
    }

    getSequences = () => {
        if(this.esPdbValido()) {
            SequenceService().getSequence(this.state.pdbCode)
                .then((response) => {

                    this.setState({mostrarSeleccionSecuencias: true, secuenciasParaElegir: response.data})
                })
        }
    }

    esPdbValido = () => {
        this.setState({mostrarErrorDeCodigoPdb: this.state.pdbCode === '' || this.state.pdbCode.length !== 4})
        const esPdbValido = !(this.state.pdbCode === '' || this.state.pdbCode.length !== 4)
        return esPdbValido
    }

    render() {
        return(
            <div className='homepage'>
                <div className='titulo'>
                    <span>¿Qué proteína analizamos hoy?</span>
                </div>
                <div className='codigo-pdb'>
                    <div>
                        <input type='text'
                               className={'input-codigo-pdb ' + (this.state.mostrarErrorDeCodigoPdb ? 'with-error' : '')}
                               value={this.state.pdbCode}
                               onChange={(event) => this.setState({pdbCode: event.target.value})}/>

                        <button className='boton-consulta-pdb' onClick={this.getSequences}>
                            ¡Vamos!
                        </button>
                    </div>
                    { this.state.mostrarErrorDeCodigoPdb &&
                    <div className='pdb-id-error'>
                        <span>¡Ups! Parece que ese no es un PDB válido</span>
                    </div>
                    }
                </div>
                <SeleccionSecuencia mostrarSeleccionSecuencias={this.state.mostrarSeleccionSecuencias} secuenciasParaElegir={this.state.secuenciasParaElegir}/>
            </div>
        )
    }
}
