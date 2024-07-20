**Project Name** 

            Note -Taking Application
            
Technologies Used: 

     •Frontend: React.Js
     
      •Backend: Fast API
      
      •DataBase: Mongodb
      
Over View Of the Project:

This project involves developing a is a full-stack note-taking application that provides a secure and user-friendly platform for managing personal notes. Built with FastAPI for the backend, React for the frontend, and MongoDB for the database, it offers functionalities such as user authentication, note creation, updating, and deletion, ensuring data security with JWT-based authentication.

Project Structure :
 

Key features:

Backend (FastAPI)

1.	User Authentication:
	
o	Registration: Users can create an account by providing a username and password. The password is hashed before storing it in the database for security.

o	Login: Users can log in with their credentials. Upon successful login, a JWT token is generated and returned to the user. This token is used to authenticate subsequent requests.

o	JWT Tokens: JSON Web Tokens (JWT) are used for securing the authentication process. Tokens are signed with a secret key and include user information, etc.

2.	CRUD Operations for Notes:
   
o	Create Note: Users can create new notes. Each note includes a title and content and is associated with the user who created it.

o	Read Notes: Users can retrieve their notes. The API will return a list of notes associated with the authenticated user.

o	Update Note: Users can update the content of their notes. This requires the note ID and updated content.

o	Delete Note: Users can delete their notes by providing the note ID.

3.	Database:
   
o	MongoDB: Used to store user data and notes. MongoDB is chosen for its flexibility and scalability. Each user and note is represented as a document in their respective collections.

 Frontend (React)
 
1.	User Interface:
   
o	Authentication Pages: Simple forms for user registration and login. These pages interact with the backend to authenticate users and store JWT tokens.

o	Notes Management:
          	Note List: Displays a list of notes created by the authenticated user.
          	Note Form: A form to create new notes or update existing ones.
          	Note Item: Individual note display with options to edit or delete.
2.	User Authentication:
         o	Token Management: JWT tokens received upon login are stored in the browser's local storage. These tokens are included in the headers of authenticated requests to the backend.
         o	Protected Routes: Routes that require authentication are protected by checking the presence of a valid JWT token.
3.	Styling:
         o	Basic CSS: CSS to style the application. This includes layout styling for the forms, note lists, and buttons.


Installation Instructions:

	Backend

	Create and Navigate to the Project Directory

    Cd server
    
	Create a Virtual Environment and Install Dependencies

    python -m venv venv
    
    pip install fastapi uvicorn pymongo python-jose
    
    uvicorn main:app --reload
    
	Configure MongoDB connection.

	Frontend

	Create a React application

   npx create-react-app frontend 
   
   cd frontend
   
	Install necessary npm packages

   npm install axios react-router-dom
   
	Run the React Development Server

      npm start

![WhatsApp Image 2024-07-19 at 21 43 05_e7574025](https://github.com/user-attachments/assets/83e1dc3b-710e-49cd-9c35-0d31f9375a3f)

	 



API Endpoints:

	Authentication:
o	POST /register: Register a new user.
o	POST /login: Authenticate a user and return a JWT token.

	 Notes:
o	GET /notes: Retrieve all notes for the authenticated user.
o	POST /notes: Create a new note.
o	PUT /notes: Update an existing note.
o	DELETE /notes: Delete a note.

Output Images:

Login page: The login page allows users to enter their credentials to access their account
 

 ![WhatsApp Image 2024-07-19 at 21 40 18_5baa3d44](https://github.com/user-attachments/assets/5dd6a9d0-8bc8-4c08-ac94-0f7673d472d4)



![WhatsApp Image 2024-07-19 at 21 39 51_f852abfe](https://github.com/user-attachments/assets/49ae89af-53ee-44c8-95a7-13cd2e8d55da)

Note Creation Page:The note creation page allows users to input new note details and save them.

 

 	![WhatsApp Image 2024-07-19 at 21 43 06_4c8854c7](https://github.com/user-attachments/assets/44ee1275-bc95-4ecd-946f-e713ba1ca397)


  
  This documentation provides an in-depth guide for setting up and  running Secure Note-taking application.This is a full-stack note-taking application built with FastAPI for the backend, React for the frontend, and MongoDB for the database. This guide includes detailed instructions and commands for configuring both the backend and frontend environments, along with information API endpoints.

     
