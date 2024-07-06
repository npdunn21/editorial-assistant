# editorial-assistant

## Tech Stack
- FastApi
- Gradio
- Postgresql
- Flyway


Feature Requests from Ben:
1) reliably produce copy in the tone and style of various specific people - if it incorporates actual quotes, even better 
2) understand how to produce different types of content formats 
3) be able to do basic data analysis to identify trending content topics or content formats (based on our data inputs)
4) be able to produce basic monthly reports identifying high-level performance and platform trends 
5) designed so it can easily ingest new material as it’s created (ie, adding new interviews and keynotes to the data set)

## Backend endpoints
Add a client
- client name
- description of client for use in prompting

Generate a post
- Should have drop down options for type of post
- Then a text field for user to type it in

Upload new content
- Should store it associated with a client id
- Anytime something new is updated we should retrain the model
- Differentiate between types of content added

Add metrics for a post
- Store it associated with a post id

Get Posts with ids for clients
- return the posts from the last X months/days/years with their ids

## Frontend features
MVP
- Add a new client with a description
- Select a client from a dropdown
- Type in a prompt and get content that is shown on the UI
- Enter content
- Add metrics about a post that are stored
- Very basic metrics display - best posts

Later:
- Produce reports
- More advanced metrics

### Database Management
To run migrations: `sh scripts/run_database_migrations.sh`

To Do List:
- Set up the database + use flyway migration to set it up
- Write the endpoints
- Write the frontend
