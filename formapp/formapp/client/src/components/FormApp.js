import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './Formapp.css';
const FormApp = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    rollnumber: '',
    phonenumber: '',
    password: '', // Add password field
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/add-registerform', formData);
      console.log(response.data);
      // Handle success, display a success message or perform any other necessary actions

      // Clear the form data after submission
      setFormData({
        name: '',
        email: '',
        rollnumber: '',
        phonenumber: '',
        password: '',
      });
    } catch (error) {
      console.error(error.message);
      // Handle error, display an error message or perform any other necessary actions
    }
  };

  return (
    <div className="form-group">
      <h1>Form Application</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="rollnumber">id No:</label>
          <input
            type="text"
            id="rollnumber"
            name="rollnumber"
            value={formData.rollnumber}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="phonenumber">Mobileno:</label>
          <input
            type="text"
            id="phonenumber"
            name="phonenumber"
            value={formData.phonenumber}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
            required
          />
        </div>
        <button type="submit">Register</button>
        <Link to="/login"><center>
          <button type="button">Login</button></center>
        </Link>
      </form>
    </div>
  );
};

export default FormApp;
