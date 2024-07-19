const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const RegisterForm = require('./Model/registerform');

const app = express();
const PORT = 8080;

app.use(express.json());
app.use(cors());
app.listen(PORT, () => {
  console.log(`Server is running on PORT ${PORT}...`);
});

mongoose.connect("mongodb://0.0.0.0:27017/registerform", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Database connected..');
});

app.post('/add-registerform', async (req, res) => {
  try {
    const registerForm = new RegisterForm(req.body);
    await registerForm.save();
    res.status(201).json({
      status: 'Success',
      data: {
        registerForm,
      },
    });
  } catch (error) {
    res.status(500).json({
      status: 'Failed',
      message: error.message,
    });
  }
});