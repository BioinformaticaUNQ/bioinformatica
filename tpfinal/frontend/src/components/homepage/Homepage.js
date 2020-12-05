import React from "react";
import "./homepage.scss"
import {InformacionProteina} from "../informacion-proteina/InformacionProteina";
import SequenceService from "../../services/SequenceService";

export class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pdbCode: ''
        }
    }

    getSequences = () => {
        SequenceService().getSequences(this.state.pdbCode).then((response) => console.log(response))
    }

    render() {
        return(
            <div className='homepage'>
                <div className='titulo'>
                    <span>¿Qué proteína analizamos hoy?</span>
                </div>
                <div className='input-codigo-pdb'>
                    <input type='text'
                           value={this.state.pdbCode}
                           onChange={(event) => this.setState({pdbCode: event.target.value})}/>
                    <button className='boton-consulta-pdb' onClick={this.getSequences}>
                        ¡Vamos!
                    </button>
                </div>
                <InformacionProteina/>
            </div>
        )
    }
}
