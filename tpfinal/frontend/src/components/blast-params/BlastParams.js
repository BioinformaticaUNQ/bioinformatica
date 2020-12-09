import React from "react";
import { Dropdown } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { matrixParams } from '../../constants/constants'

export class BlastParams extends React.Component {
    constructor(props) {
        debugger
        super(props);
    }



    render() {
        return(
            <div>
                Parametros Blast
                <div>
                    <label>evalue:</label>
                    <input type='text'
                           className={'evalue'}
                           value={}
                           defaultValue={0.001}
                           onChange={(event) => this.props.setEvalue({evalue: event.target.value})}/>

                    <label>matrix:</label>
                    <Dropdown>
                        <Dropdown.Toggle variant="success" id="dropdown-basic">
                            Dropdown Button
                        </Dropdown.Toggle>
                        <Dropdown.Menu>
                            {
                                matrixParams.map( param => <Dropdown.Item eventKey={param.value} onClick={ () =>{console.log(param.value)}}>{param.name}</Dropdown.Item> )
                            }
                        </Dropdown.Menu>
                    </Dropdown>

                </div>
            </div>
        )
    }
}
