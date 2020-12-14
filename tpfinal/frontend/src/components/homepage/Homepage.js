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
            pbsAndChain: [],
            loading: false,
            evalue: 0.001,
            coverage: 90,
            secuenciaElegida: null,
            errorPDBCode: false,
        }
    }

    componentWillMount(){
        document.body.style.backgroundColor = "#fcf8ec";
    }

    getSequences = () => {

        this.setState({mostrarSeleccionSecuencias: false,
            mostrarErrorDeCodigoPdb: false,
            mostrarProteina3d: false,
            mostrarInformacionAnalizada: false, errorPDBCode: false, loading: false})

        if(this.esPdbValido()) {
            SequenceService().getSequence(this.state.pdbCode)
                .then((response) => {
                    const sequences = response.data.length
                    if (sequences) {
                        this.setState({mostrarSeleccionSecuencias: true, secuenciasParaElegir: response.data, errorPDBCode: false})
                    }
                    else {
                        this.setState({errorPDBCode: true})
                    }
                    
                })
        }
    }

    esPdbValido = () => {
        this.setState({mostrarErrorDeCodigoPdb: this.state.pdbCode === '' || this.state.pdbCode.length !== 4})
        const esPdbValido = !(this.state.pdbCode === '' || this.state.pdbCode.length !== 4)
        return esPdbValido
    }

    conseguirTodaLaInfo = (secuencia) => {
        this.setState({loading: true, mostrarSeleccionSecuencias: false, secuenciaElegida: secuencia})
        
        SequenceService().conseguirTodaLaInfo(secuencia, this.state.evalue, this.state.coverage).then((response) => {

            const dssps = response.data.map(info => {
                return   {
                    name: info['sequence']['pdbcode'],
                    sequence: info['dssp']['alignment']
                    }
            })

            const pbsAndChain = response.data.map(info => {
                return   {
                    name: info['sequence']['pdbcode'],
                    chain: info['dssp']['chain']
                    }
            })
    
            const sequences = response.data.map(info => {
              return   {
                name: info['sequence']['pdbcode'],
                sequence: info['sequence']['sequence']
                }
            })

            this.setState({mostrarInformacionAnalizada: true, 
                dssps: dssps, sequences: sequences, pbsAndChain: pbsAndChain, loading: false})

        }).catch((err) => {
            console.log(err)
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
                {this.state.mostrarSeleccionSecuencias &&  
                <div className="parametros">
                    
                    <label>Parametros Blast</label>
                    <br/>
                    
                    <div className="elementos-parametros">
                        <div className="columna-parametros">
                            <div className="elemento-parametro ">
                                <label>E-value:</label>
                                <input type='text'
                                    className={'evalue'}
                                    value={this.state.evalue}
                                    defaultValue={this.state.evalue}
                                    onChange={(event) => this.setState({evalue: event.target.value})}/>
                            </div>

                            <div className="elemento-parametro ">
                                <label>Gap open:</label>
                                <input type='number'
                                    value="11"
                                    defaultValue="11"
                                    disabled={true}/>
                            
                            </div>
                          
                        </div>
                        
                        <div className="columna-parametros">

                            <div className="elemento-parametro ">
                                <label>Coverage:</label>
                                <input type='text'
                                    className={'coverage'}
                                    value={this.state.coverage}
                                    defaultValue={this.state.coverage}
                                    onChange={(event) => this.setState({coverage: event.target.value})}/>

                            </div>
                            

                            <div className="elemento-parametro ">
                                <label>Gap extend:</label>
                                <input type='number'
                                    value='1'
                                    defaultValue='1'
                                    disabled={true}/>

                            </div>
                        </div>
                    </div>    
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

                <SeleccionSecuencia mostrarSeleccionSecuencias={this.state.mostrarSeleccionSecuencias}
                                    secuenciasParaElegir={this.state.secuenciasParaElegir}
                onSecuenciaSeleccionada={this.conseguirTodaLaInfo}/>

                
                {this.state.loading && <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>}
                {this.state.mostrarInformacionAnalizada && <InformacionSobreLaSecuencia sequence={this.state.secuenciaElegida} codigoPdb={this.state.pdbCode}
                sequences={this.state.sequences} dssps={this.state.dssps} pbsAndChain={this.state.pbsAndChain}/>}
                {this.state.errorPDBCode && 
                    <div className='pdb-id-error'>
                        <span>No tenemos registrado ese PDB code en nuestra base de datos, lo sentimos!</span>
                    </div>
                }
            </div>
        )
    }
}
