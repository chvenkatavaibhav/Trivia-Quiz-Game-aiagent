# Triviza Quiz Game Ai Agent

## Overview
The **Triviza Quiz Game** is an interactive trivia quiz application that allows users to:
- Select a **category** and **difficulty level** for the quiz.
- Answer multiple-choice questions fetched from the **Open Trivia Database API**.
- Receive immediate feedback on their answers.
- Track their score throughout the quiz.
- Restart the quiz with the same set of questions or reset to fetch new questions.

## Features
### Multiple Categories
- Users can choose from categories like General Knowledge, Science, History, etc.

### Difficulty Levels
- Questions can be set to **easy**, **medium**, or **hard** difficulty.

### Dynamic Question Fetching
- Questions are fetched from the **Open Trivia Database API** based on user selections.

### Score Tracking
- The user’s score is displayed and updated after each question.

### Shuffled Questions and Answers
- Questions and answer choices are shuffled to make the quiz more engaging.

### Restart and Reset Options
- Users can restart the quiz with the same questions or reset to fetch new questions.

## Technologies Used
### Backend
- **Flask**: A lightweight Python web framework for handling HTTP requests and serving the frontend.
- **Requests**: A Python library for making HTTP requests to the Open Trivia Database API.

### Frontend
- **HTML/CSS**: For the user interface and styling.
- **JavaScript**: For dynamic interactions and handling user input.

### APIs
- **Open Trivia Database API**: Provides trivia questions and answers.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/chvenkatavaibhav/triviza-quiz-game.git
