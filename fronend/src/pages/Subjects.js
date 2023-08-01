import Button from 'react-bootstrap/Button'
import React,{useState,useEffect} from "react";
import './subjects.css'
import axios from "axios";
const Subjects = () => {
    const [subjects, setSubjects] = useState([])
    useEffect(()=> {
        getsubjects()
    },[])
    let getsubjects = async () => {
        let response = await axios.get('http://127.0.0.1:8000/api/all/')
        //console.log(response.data)
        setSubjects(response.data)
    }
    const handleDelete = (id) => {
        const updatedSubjects = subjects.filter((subject)=>subject.id !== id)
        setSubjects(updatedSubjects)
        axios.delete('http://127.0.0.1:8000/api/'+id)
        .catch((error) => {
            console.log("error occured")
        })       
    }
    
    return (
        <div>
            <h1>Subject Details</h1>
            <table className="table table-border table-striped w-75 mx-auto">
                <thead>
                    <th>Sl No.</th>
                    <th>Year</th>
                    <th>Semester</th>
                    <th>Subject Code</th>
                    <th>Name of the Subject</th>
                    <th>Actions</th>    
                </thead>
                <tbody>
                    {subjects.map((subject,index) => (
                            <tr key={index}>
                                <td>{index+1}</td>
                                <td>{subject.year}</td>
                                <td>{subject.sem}</td>
                                <td>{subject.subject_code}</td>
                                <td>{subject.subject_name}</td>
                                <td>
                                    <Button variant='outline-success'>Update</Button>{' '}
                                    <Button variant='outline-danger' onClick={()=>handleDelete(subject.id)}>Delete</Button>
                                </td>
                            </tr>
                    ))}
                </tbody>    
            </table>    
        </div>
    )
}
export default Subjects