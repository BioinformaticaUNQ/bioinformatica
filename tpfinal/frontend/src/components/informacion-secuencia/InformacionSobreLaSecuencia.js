import React from "react";
import "./informacion-secuencia.scss"
import MSAViewer from "react-msa-viewer";
import Viewer from "../viewer/Viewer";
import { Card, Accordion , Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

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
        }
    }

    downloadPrimaryStructure(){
        download(JSON.stringify(this.props.sequences), 'primary_structures.json')
    }

    downloadSecondaryStructure(){
        download(JSON.stringify(this.props.dssps), 'secondary_structures.json')
    }

    downloadPymolAnalyze(){
        const data = []
        download(JSON.stringify(data), 'thirty_structures.json')
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
                            <Button onClick={()=>this.downloadPrimaryStructure()}> Descargar data</Button>
                        </div>}
                    {this.state.opcionSeleccionada === 2 &&
                        <div>
                            <MSAViewer sequences={this.props.dssps}/>
                            <Button onClick={()=>this.downloadSecondaryStructure()}> Descargar data</Button>
                        </div>}
                    {this.state.opcionSeleccionada === 3 &&
                        <div>
                            <Viewer protein={this.props.codigoPdb}> </Viewer>
                            <Button onClick={()=>this.downloadPymolAnalyze()}> Descargar analisis pymol</Button>
                        </div>
                        }
                </div>
              

            </div>
        )
    }
}
