import React from "react";
import "./homepage.scss"
import {SeleccionSecuencia} from "../informacion-proteina/SeleccionSecuencia";
import SequenceService from "../../services/SequenceService";
import {InformacionSobreLaSecuencia} from "../informacion-secuencia/InformacionSobreLaSecuencia";
import { Dropdown } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';



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
            loading: false,
            evalue: 0.001,
            coverage: 90,
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
        
        SequenceService().conseguirTodaLaInfo(secuencia, this.state.evalue, this.state.coverage).then((response) => {

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
                               placeholder={'Ingresa el PDB'}
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

                {this.state.mostrarSeleccionSecuencias &&  
                <div>
                    
                    <label>Parametros Blast</label>
                    <br/>

                    <label>E-value:</label>
                    <input type='text'
                           className={'evalue'}
                           value={this.state.evalue}
                           defaultValue={this.state.evalue}
                           onChange={(event) => this.setState({evalue: event.target.value})}/>
                    
                    <label>Coverage:</label>
                    <input type='text'
                           className={'coverage'}
                           value={this.state.coverage}
                           defaultValue={this.state.coverage}
                           onChange={(event) => this.setState({coverage: event.target.value})}/>

                    <br/>
                    
                    <label>Gap open:</label>
                    <input type='number'
                           value="11"
                           defaultValue="11"
                           disabled={true}/>
                    
                    <label>Gap extend:</label>
                    <input type='number'
                           value='1'
                           defaultValue='1'
                           disabled={true}/>
                    
                    <br />

                    <label>matrix:</label>
                    <Dropdown>
                        <Dropdown.Toggle variant="info" id="dropdown-basic" disabled={true}>
                            BLOSUM62
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            
                            <Dropdown.Item >BLOSUM62</Dropdown.Item> 
                            
                        </Dropdown.Menu>
                    </Dropdown>

                    
                </div> }
                {this.state.loading && <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>}
                {this.state.mostrarInformacionAnalizada && <InformacionSobreLaSecuencia codigoPdb={this.state.pdbCode}
                sequences={this.state.sequences} dssps={this.state.dssps}/>}

            </div>
        )
    }
}
