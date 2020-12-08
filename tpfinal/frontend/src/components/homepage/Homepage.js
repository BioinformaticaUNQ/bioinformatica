import React from "react";
import "./homepage.scss"
import {SeleccionSecuencia} from "../informacion-proteina/SeleccionSecuencia";
import SequenceService from "../../services/SequenceService";
import {InformacionSobreLaSecuencia} from "../informacion-secuencia/InformacionSobreLaSecuencia";



export class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pdbCode: '',
            mostrarSeleccionSecuencias: false,
            mostrarErrorDeCodigoPdb: false,
            mostrarProteina3d: false,
            mostrarInformacionAnalizada: false,
            dssps: [],
            sequence: [],
            loading: false 
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

    conseguirTodaLaInfo = (secuencia) => {
        
        this.setState({loading: true, mostrarSeleccionSecuencias: false})
        
        SequenceService().conseguirTodaLaInfo(secuencia).then((response) => {

            const dssps = response.data.map(info => {
                return   {
                    name: info['sequence']['pdbcode'],
                    sequence: info['dssp']
                    }
            })
    
            const sequences = response.data.map(info => {
              return   {
                name: info['sequence']['pdbcode'],
                sequence: info['sequence']['sequence']
                }
            })

            this.setState({mostrarInformacionAnalizada: true, 
                dssps: dssps, sequences: sequences, loading: false})

        }).catch(() => {
            console.log("Esto es una mierda")
        })
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
                <SeleccionSecuencia mostrarSeleccionSecuencias={this.state.mostrarSeleccionSecuencias}
                                    secuenciasParaElegir={this.state.secuenciasParaElegir}
                                    onSecuenciaSeleccionada={this.conseguirTodaLaInfo}/>

                    
                {this.state.loading && <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>}
                {this.state.mostrarInformacionAnalizada && <InformacionSobreLaSecuencia codigoPdb={this.state.pdbCode} 
                sequences={this.state.sequences} dssps={this.state.dssps}/>}
            </div>
        )
    }
}
