import axios from 'axios';
const SERVICE_URL = 'http://localhost:5000/';

const SequenceService = () => {

    const getSequence = (pdbCode) => {
        return axios.post(`${SERVICE_URL}sequences`,
            {
                pdbcode: pdbCode.toUpperCase()
            })
    }

    const conseguirTodaLaInfo = (secuencia, evalue, coverage) => {
        return axios.post(`${SERVICE_URL}analyze`,
            {
                sequence: secuencia,
                evalue: evalue,
                coverage: coverage 
            })
    }


    return {
        getSequence: getSequence,
        conseguirTodaLaInfo: conseguirTodaLaInfo
    }
}

export default SequenceService;
