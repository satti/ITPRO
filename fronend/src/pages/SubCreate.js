import React, { useState } from "react";
import { Form } from "react-bootstrap";
import FloatingLabel from "react-bootstrap/FloatingLabel";
import Button from "react-bootstrap/Button";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const SubCreate = () => {
    const years = ['Select Year','I-Year','II-Year','III-Year','IV-Year']
    const [firstSelectedValue,setFirstSelectedValue] = useState('')
    const [secondSelectedValue,setSecondSelectedValue] = useState('')
    const [subCode,setSubCode] = useState('')
    const [subName,setSubName] = useState('')
    const navigate = useNavigate()
    const getSecondSelectOptions = () => {
        if (firstSelectedValue === 'I-Year'){
            return ['Select Semester','I-Semester','II-Semester']
        }
        else if (firstSelectedValue === 'II-Year') {
            return ['Select Semester','III-Semester','IV-Semester']
        }
        else if (firstSelectedValue === 'III-Year') {
            return ['Select Semester','V-Semester','VI-Semester']
        }
        else if (firstSelectedValue === 'IV-Year') {
            return ['Select Semester','VII-Semester','VIII-Semester']
        }
        else {
            return []
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        try{
            axios('http://127.0.0.1:8000/api/create/',
                {method: 'POST',
                headers: {
                    "Content-Type": 'application/json'},
                data: JSON.stringify({year:firstSelectedValue,
                sem:secondSelectedValue,
                subject_code: subCode,
                subject_name: subName
            }),
            });
        navigate('/')
        }
        catch(error){
            console.log("Error Occured");
        }
    }
    
    const handleFirstSelectChange = (event) => {
        const value = event.target.value
        setFirstSelectedValue(value)
    }
    const handleSecondSelectedChange = (event) => {
        const value = event.target.value
        setSecondSelectedValue(value)
    }
    return (
        <div className="container w-50">
            <h1>Subject Entry Form</h1>
            <Form onSubmit={handleSubmit}>
            <Form.Select id="firstSelect" value={firstSelectedValue} onChange={handleFirstSelectChange}>
                {years.map((year,index) => {
                return (<option key={index} value={year}>{year}</option>)
                 })}   
            </Form.Select><br/>
            <Form.Select 
            id='secondSelect' 
            value={secondSelectedValue} 
            onChange={handleSecondSelectedChange}>
                 {getSecondSelectOptions().map((year,index)=>(
                    <option key={index} value={year}>{year}</option>
                 ))}
            </Form.Select><br/>
            <FloatingLabel
            controlId="floatingInput"
            label = "Enter Subject Code"
            className="mb-3"
            >
            <Form.Control type="text" 
            placeholder="Enter Subject Code" 
            value={subCode} 
            onChange={(e)=>setSubCode(e.target.value)}/>
            </FloatingLabel>
            <FloatingLabel
                controlId="floatingInput"
                label = "Enter Subject"
                className="mb-3"
                >
                <Form.Control 
                type="text" 
                placeholder="Enter Subject" 
                value={subName}
                onChange={(e)=>setSubName(e.target.value)}/>
            </FloatingLabel>
            <Button type="submit">Submit</Button>
        </Form>
        </div>
    )
}

export default SubCreate