# Test_site

## Features
1. authenticated users can get tests
2. authenticated users can get results 

## Tables
1. Test
2. Results

## Schema

User:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| first_name | str | firstname |
| last_name | str | lastname |
| gmail | str | gmail |
| username | str  | unique username |
| password | str  | password |

Test:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| question_str | str  | question |
| question_img | img  | img |
| question_type1 | str | question type |
| question_subject | str | question subject |
| option1 | str | True answer |
| option2 | str | False answer |
| option3 | str | False answer |
| option4 | str | False answer |

Result:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| check | int  | count answer |
| user | fk | user id |
| start_time | date  | start time |
| end_time | date  | auto now |

## Endpoints

Users endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | /register   | Create a user |
| GET | /register | get a user |

Tests endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /test   | Get all tests |
| GET   | /test/< int:pk>  | Get a test |
| GET    | /test/< str:q_type>/ | Get form type |
| GET    | /test/< str:q_type>/< str:q_subject>| Get filter |

Results endpoints:

|Method| Endpoint | Description|
|------|----------|------------|
|POST  | result/  | Create a result |
|GET  | result/  | Get all results |
|GET  | result/< int:pk>  | Get a result |


