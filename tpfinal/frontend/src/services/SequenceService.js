import axios from 'axios';
const SERVICE_URL = 'http://localhost:5000/';

const SequenceService = () => {

    const getSequences = (pdbCode) => {
        return axios.post(`${SERVICE_URL}sequence`,
            {
                pdbcode: pdbCode
            })
    }

    return {
        getSequences: getSequences
    }
}

export default SequenceService;
