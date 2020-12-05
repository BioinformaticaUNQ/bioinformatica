import axios from 'axios';
const SERVICE_URL = 'http://localhost:5000/';

const SequenceService = () => {

    const getSequence = (pdbCode) => {
        return axios.post(`${SERVICE_URL}sequences`,
            {
                pdbcode: pdbCode.toUpperCase()
            })
    }

    return {
        getSequence: getSequence
    }
}

export default SequenceService;
