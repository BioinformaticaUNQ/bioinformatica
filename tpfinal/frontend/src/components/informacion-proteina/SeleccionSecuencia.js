import React from "react";
import "./seleccion-secuencias.scss"
import { Card , Accordion, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

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
                    <p>Hace click en la secuencia para analizarla con estos parametros.</p>
                    <div className='contenedor-secuencias'>
                        <div>
                            {
                                <Accordion defaultActiveKey="0">
                                    {this.props.secuenciasParaElegir.map(secuencia => {
                                        let eventKey = this.props.secuenciasParaElegir.indexOf(secuencia) +1;
                                        return (
                                        <div className='contenedor-secuencia'>
                                            <Card>
                                                <Card.Header>
                                                    <Accordion.Toggle as={Button} variant="link" eventKey={eventKey}>
                                                        {secuencia.split('|')[0].replace('>', '')} - {secuencia.split('|')[2]} - {secuencia.split('|')[3].split('\n')[0]}
                                                    </Accordion.Toggle>
                                                </Card.Header>
                                                <Accordion.Collapse eventKey={eventKey} onClick={() => this.props.onSecuenciaSeleccionada(secuencia)}>
                                                    <Card.Body>
                                                        {secuencia.split('|')[1]}
                                                        <p className='texto-secuencia'>{secuencia.split('|')[3].split('\n')[1]}</p>
                                                    </Card.Body>
                                                </Accordion.Collapse>
                                            </Card>
                                        </div>)
                                })}
                                </Accordion>
                            }
                        </div>
                    </div>
                </div>
                }
            </div>

        )
    }
}
