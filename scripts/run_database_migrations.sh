#!/bin/sh

flyway -url="jdbc:postgresql://127.0.0.1:5432/editorial_assistant" -user="postgres" -password="postgres" -locations="migrations" migrate