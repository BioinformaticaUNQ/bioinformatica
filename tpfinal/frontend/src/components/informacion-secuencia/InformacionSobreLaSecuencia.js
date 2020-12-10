import React from "react";
import "./informacion-secuencia.scss"
import MSAViewer from "react-msa-viewer";
import Viewer from "../viewer/Viewer";
import { Card, Accordion , Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


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
                    {this.state.opcionSeleccionada === 1 && <MSAViewer sequences={this.props.sequences}/>}
                    {this.state.opcionSeleccionada === 2 && <MSAViewer sequences={this.props.dssps}/>}
                    {this.state.opcionSeleccionada === 3 && <Viewer protein={this.props.codigoPdb}> </Viewer>}
                </div>
              

            </div>
        )
    }
}
