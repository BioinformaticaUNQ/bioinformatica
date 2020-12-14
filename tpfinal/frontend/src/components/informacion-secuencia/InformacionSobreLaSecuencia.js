import React from "react";
import "./informacion-secuencia.scss"
import MSAViewer from "react-msa-viewer";
import Viewer from "../viewer/Viewer";
import { Card, Accordion , Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import DropdownMultiselect from "react-multiselect-dropdown-bootstrap";
import SequenceService from "../../services/SequenceService";

const  download = (data, filename) => {
    const element = document.createElement("a");
    const file = new Blob([data], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = filename;
    document.body.appendChild(element); // Required for this to work in FireFox
    element.click();
}
export class InformacionSobreLaSecuencia extends React.Component {
    constructor(props) {
        
        super(props);
        this.state = {
            opcionSeleccionada: 1,
            analisisPymol: [],
            data: [],
            loading: false
        }
    }

    downloadPrimaryStructure(){
        download(JSON.stringify(this.props.sequences), 'primary_structures.json')
    }

    downloadSecondaryStructure(){
        download(JSON.stringify(this.props.dssps), 'secondary_structures.json')
    }

    downloadPymolAnalyze(){

        this.setState({loading: true})
        
        SequenceService().analisisPymol(this.props.pbsAndChain.find((seq) => seq.name.toUpperCase() == this.props.codigoPdb.toUpperCase()), 
        this.state.analisisPymol).then((response) => {
            this.setState({loading: false})
            response.data.forEach((element) => {
                
             download(element.result, element.name+'.json')
        } )})
        
    }

    render() {
        return(
            <div className='informacion-secuencia'>
                <div>
                    <Accordion defaultActiveKey="0">
                        <Card>
                            <Card.Header>
                                <Accordion.Toggle as={Button} variant="link" eventKey="1">
                                    {this.props.sequence.split('|')[0].replace('>', '')} - {this.props.sequence.split('|')[2]} - {this.props.sequence.split('|')[3].split('\n')[0]}
                                </Accordion.Toggle>
                            </Card.Header>
                            <Accordion.Collapse eventKey='1'>
                                <Card.Body>
                                    {this.props.sequence.split('|')[1]}
                                    <p className='texto-secuencia'>{this.props.sequence.split('|')[3].split('\n')[1]}</p>
                                </Card.Body>
                            </Accordion.Collapse>
                        </Card>
                    </Accordion>
                </div>
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
                    {this.state.opcionSeleccionada === 1 &&
                        <div>
                            <MSAViewer sequences={this.props.sequences}/>
                            <Button className="mt-2" variant="success" onClick={()=>this.downloadPrimaryStructure()}> Descargar json</Button>
                        </div>}
                    {this.state.opcionSeleccionada === 2 &&
                        <div>
                            <MSAViewer sequences={this.props.dssps}/>
                            <Button className="mt-2" variant="success"  onClick={()=>this.downloadSecondaryStructure()}> Descargar json</Button>
                        </div>}
                    {this.state.opcionSeleccionada === 3 &&
                        <div>
                            <Viewer protein={this.props.codigoPdb}> </Viewer>
                            <DropdownMultiselect style={{paddingTop: "3%"}}
                                options={this.props.pbsAndChain.filter((seq) => this.props.codigoPdb.toUpperCase() !== seq.name.toUpperCase()).map((seq) => {
                                    return {key: [seq.name, seq.chain], label: seq.name}  
                                    })
                                }
                                name="countries"
                                placeholder="Seleccionar PDBs"
                                handleOnChange={(selected) => {
                                    this.setState({analisisPymol: selected})
                                }}
                            />
                            {!this.state.loading && <Button disabled={this.state.analisisPymol.length == 0} className="mt-3 h-25" variant="success"   onClick={()=>this.downloadPymolAnalyze()}> Descargar analisis de estructura terciaria</Button>}
                            {this.state.loading && <div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>}
                        </div>
                        }
                </div>
              

            </div>
        )
    }
}
