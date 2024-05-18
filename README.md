# Django-RestApi: NoteTakingApp
 
### Description

This project provides a user-friendly RESTful API for managing your notes, complete with a graphical interface built using Django REST Framework's brows able API. Perfect for creating personal note-taking applications or integrating notes into other projects.

## Installation

1. **Clone the Repository:**
```
git clone https://github.com/encode/django-rest-framework
```
2. **Install Dependencies:**
<br><br>Navigate to the project directory and install the required dependencies using pip:
```
cd Django-RestApi  # Assuming the project directory is named Django-RestApi
pip install -r requirements.txt
```
3. **Set up the Database:**
   <br><br>Run the following commands to create and apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
4. **Run the Development Server:**
   <br><br>Start the development server to test your API locally:
```
python manage.py runserver
```
This will typically run the server at http://127.0.0.1:8000/.

## Usage
**Graphical Interface:**
The Django REST Framework brows able API allows you to explore and interact with your API endpoints directly from your web browser. Navigate to http://127.0.0.1:8000/ in your browser after running the development server with debug=True. You'll see a user-friendly interface for listing, creating, retrieving, updating, and deleting notes.

**Making Requests:**
Use an HTTP client or REST client tool to interact with the API endpoints. Authentication is not included in this basic example, but you can implement it for production use.

| Method | URL Path | Description |
| :--: | :--: | :--: |
| GET | `/api/notes` | Retrieves all notes belonging to the current user or shared with |
| POST | `/api/notes` | Creates a new note for the current user |
| DELETE | `api/notes` | Deletes all notes belonging to the current user |
| GET | `/api/notes/<int:id>` | Retrieves a specific note by its ID (belonging to the current user or shared with) |
| PUT | `/api/notes/<int:id>` | Updates an existing note by its ID (belonging to the current user) |
| DELETE | `/api/notes/<int:id>` | Deletes a specific note by its ID (belonging to the current user) |

**Notes:**
- The `/api/note` endpoint currently retrieves all notes for the current user. You may want to implement user authentication and authorization in production for better security.
- The ID in the `/api/notes/<int:id>` endpoint refers to the unique identifier of a specific note.
