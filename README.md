**PROJECT NAME:** 
                   **Note -Taking Application**
            
**TECHNOLOGIES USED:** 

      •Frontend: React.Js
     
      •Backend: Fast API
      
      •DataBase: Mongodb
      
**Over View Of the PROJECT:**

This project involves developing a is a full-stack note-taking application that provides a secure and user-friendly platform for managing personal notes. Built with FastAPI for the backend, React for the frontend, and MongoDB for the database, it offers functionalities such as user authentication, note creation, updating, and deletion, ensuring data security with JWT-based authentication.

**PROJECT STRUCTURE:**
 
![WhatsApp Image 2024-07-19 at 21 27 07_98fb58d8](https://github.com/user-attachments/assets/a9eb4246-669f-4c7f-9351-5402f9109348)


**KEY FEATURES:**

**>>>Backend (FastAPI)**

1. **_User Authentication_**
	
      o	Registration: Users can create an account by providing a username and password. The password is hashed before storing it in the database for security.

      o	Login: Users can log in with their credentials. Upon successful login, a JWT token is generated and returned to the user. This token is used to authenticate subsequent requests.

      o	JWT Tokens: JSON Web Tokens (JWT) are used for securing the authentication process. Tokens are signed with a secret key and include user information, etc.

2._**CRUD Operations for Notes:**___
   
      o	Create Note: Users can create new notes. Each note includes a title and content and is associated with the user who created it.

      o	Read Notes: Users can retrieve their notes. The API will return a list of notes associated with the authenticated user.

      o	Update Note: Users can update the content of their notes. This requires the note ID and updated content.

      o	Delete Note: Users can delete their notes by providing the note ID.

_3.__**Database:**____
   
      o	MongoDB: Used to store user data and notes. MongoDB is chosen for its flexibility and scalability. Each user and note is represented as a document in their respective collections.

 **>>>Frontend (React)**
 
_1.**User Interface:**__
   
     o	Authentication Pages: Simple forms for user registration and login. These pages interact with the backend to authenticate users and store JWT tokens.

     o	Notes Management:
          	Note List: Displays a list of notes created by the authenticated user.
          	Note Form: A form to create new notes or update existing ones.
          	Note Item: Individual note display with options to edit or delete.
	  
2._**User Authentication:**_

         o Token Management: JWT tokens received upon login are stored in the browser's local storage. These tokens are included in the headers of authenticated requests to the backend.
         o Protected Routes: Routes that require authentication are protected by checking the presence of a valid JWT token.
	 
3._**Styling:**_

         o Basic CSS: CSS to style the application. This includes layout styling for the forms, note lists, and buttons.


**INSTALLATION INSTRUCTION:**

_**>>>Backend**_

 **Create and Navigate to the Project Directory**

       Cd server
    
 **Create a Virtual Environment and Install Dependencies**

    python -m venv venv
    
    pip install fastapi uvicorn pymongo python-jose
    
    uvicorn main:app --reload
    
 **Configure MongoDB connection.**


_**>>>Frontend**_

**Create a React application**

    npx create-react-app frontend 
   
    cd frontend
   
 **Install necessary npm packages**

    npm install axios react-router-dom
   
 **Run the React Development Server**

     npm start



![WhatsApp Image 2024-07-19 at 21 43 06_9b2514ff](https://github.com/user-attachments/assets/9409c867-485d-4681-a911-d5138c1c05d0)



**API ENDPOINTS:**

**Authentication:**

      o	POST /register: Register a new user.

      o	POST /login: Authenticate a user and return a JWT token.

 **Notes:**

      o	GET /notes: Retrieve all notes for the authenticated user.
    
      o	POST /notes: Create a new note.
    
      o	PUT /notes: Update an existing note.
    
      o	DELETE /notes: Delete a note.

**OUTPUT IMAGES:**

**Login page:** The login page allows users to enter their credentials to access their account
 

 
![WhatsApp Image 2024-07-19 at 21 40 19_857dbb96](https://github.com/user-attachments/assets/25a5c8b6-8205-4513-92f7-8f3942996604)



![WhatsApp Image 2024-07-19 at 21 39 52_25cef47b](https://github.com/user-attachments/assets/a4057a65-0879-48e9-ac01-f9d8b529701b)


**Note Creation Page:** The note creation page allows users to input new note details and save them.



![WhatsApp Image 2024-07-19 at 21 39 14_201021ae](https://github.com/user-attachments/assets/e0849d64-2e13-4b0c-acc6-7ca2e4dfc07e)


---> This documentation provides an in-depth guide for setting up and  running Secure Note-taking application.This is a full-stack note-taking application built with FastAPI for the backend, React for the frontend, and MongoDB for the database. This guide includes detailed instructions and commands for configuring both the backend and frontend environments, along with information API endpoints.

     
