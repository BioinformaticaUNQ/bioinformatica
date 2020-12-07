import React from "react";
import "./informacion-secuencia.scss"
import MSAViewer, {Labels, OverviewBar, PositionBar, SequenceOverview, SequenceViewer} from "react-msa-viewer";

const sequences = [
    {name: "2NRL", sequence:
            "--------------------------------------------------------------------------------------------------------------------------------------------------DFDAVLKCWGPVEAD-YTTIGGLVLTRLFKEHPETQKLFPKFA-GIA-QADIAGNAAVSAHGATVLKKLGELLKAK---GSHAAILKPLANS--HATKHKIPINNFKLISEVLVKVMQEKAG---LDAGGQTALRNVMGIIIADLEANYKELGFSG"},
    {name: "3QM5", sequence:
            "--------------------------------------------------------------------------------------------------------------------------------------------------DFDAVLKCWGPVEAD-YTTIGGLVLTRLFKEHPETQKLFPKFA-GIA-QADIAGNAAVSAHGATVLKKLGELLKAK---GSHAAILKPLANS--HATKHKIPINNFKLISEVLVKVMQEKAG---LDAGGQTALRNVMGIIIADLEANYKELGFS-"},
    {name: "2NRM", sequence:
            "--------------------------------------------------------------------------------------------------------------------------------------------------DFDAVLKXWGPVEAD-YTTIGGLVLTRLFKEHPETQKLFPKFA-GIA-QADIAGNAAVSAHGATVLKKLGELLKAK---GSHAAILKPLANS--HATKHKIPINNFKLISEVLVKVMQEKAG---LDAGGQTALRNVMGIIIADLEANYKELGFSG"},
]

const options = {
    sequences
};


export class InformacionSobreLaSecuencia extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            opcionSeleccionada: 1
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
                    {this.state.opcionSeleccionada === 1 && <MSAViewer {...options}/>}
                    {this.state.opcionSeleccionada === 2 && <span>aca va la info de estructura secundaria</span>}
                    {this.state.opcionSeleccionada === 3 && <span>aca va la info de estructura terciaria</span>}
                </div>
            </div>
        )
    }
}
