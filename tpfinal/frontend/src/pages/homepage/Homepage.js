import {withRouter} from "react-router-dom";
import React from "react";
import './homepage.scss'

class Homepage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            codigoPDB: ''
        }
    }

    actualizarCodigo = (nuevoCodigo) => {
        this.setState({codigoPDB: nuevoCodigo})
    }

    render() {
        return (
            <div className='homepage'>
                <div className='archivo-pdb'>

                </div>
                <div className='codigo-pdb'>
                    <label className='label-codigo'>
                        Inserte su código PDB
                    </label>
                    <input type="text" value={this.state.codigoPDB} id="codigo" name="codigo"
                           onChange={(event) =>this.actualizarCodigo(event.target.value)} />
                </div>
                <div>
                    <button>mandale mecha</button>
                </div>
            </div>
        );
    }
}
export default withRouter(Homepage);
