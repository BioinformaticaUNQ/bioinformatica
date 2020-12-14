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

    const analisisPymol = (mobile, reference) => {
        return axios.post(`${SERVICE_URL}alignStructures`,
            {
                mobile: mobile,
                reference: reference    
            })
        }



    return {
        getSequence: getSequence,
        conseguirTodaLaInfo: conseguirTodaLaInfo,
        analisisPymol: analisisPymol
    }

    
}

export default SequenceService;
