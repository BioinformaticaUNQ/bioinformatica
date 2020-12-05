import React from "react";
import "./informacion-proteina.scss"

export class InformacionProteina extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            mostrarInfo: false
        }
    }

    render() {
        return(
            <div className='informacion-proteina'>
                <div className='fila-info'>

                </div>
            </div>
        )
    }
}
