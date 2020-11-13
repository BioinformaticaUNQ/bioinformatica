import axios from 'axios';
const SERVICE_URL = 'http://localhost:5000/';

const CuloService = () => {

    const unaFuncion = () => {
        return axios.get(`${SERVICE_URL}models`)
    }

    return {
        unaFuncion: unaFuncion
    }
}

export default CuloService;
