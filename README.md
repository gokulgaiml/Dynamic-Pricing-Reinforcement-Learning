# Dynamic Pricing using Reinforcement Learning

A Reinforcement Learning project for developing a dynamic pricing system using hotel booking demand data. The project combines data preprocessing, exploratory data analysis, pricing-oriented feature engineering, a custom Gymnasium reinforcement learning environment, Q-Learning, trained model persistence, pricing prediction, and evaluation of pricing decisions.

---

# Overview

Dynamic pricing is the process of adjusting prices based on changing market and customer conditions.

In this project, Reinforcement Learning is used to learn pricing decisions from hotel booking data. The system observes the current booking state and chooses one of three pricing actions:

- Decrease Price
- Keep Price
- Increase Price

The Reinforcement Learning agent learns which action provides a better reward for different booking conditions.

The project was developed in multiple stages, starting with data preparation and analysis and progressing toward a working Q-Learning based dynamic pricing system.

---

# Project Objectives

The main objectives of this project are:

- Build a modular Dynamic Pricing project structure
- Load and process hotel booking data
- Clean and preprocess the dataset
- Perform Exploratory Data Analysis
- Analyze missing values and duplicate records
- Create pricing-related features
- Prepare data for Reinforcement Learning
- Build a custom pricing environment
- Define states, actions, and rewards
- Implement a Q-Learning agent
- Train the Reinforcement Learning agent
- Save and load the trained model
- Generate pricing decisions using the trained Q-table
- Evaluate the learned pricing policy
- Analyze the distribution of pricing decisions
- Maintain the project using Git and GitHub
- Create a reusable and modular codebase

---

# Business Problem

Hotels need to decide the appropriate room price based on factors such as:

- Current demand
- Lead time
- Number of bookings
- Customer behavior
- Hotel type
- Length of stay
- Market segment
- Seasonal patterns
- Existing pricing conditions

A fixed pricing strategy may not respond effectively to changing demand.

The objective of this project is to create an intelligent pricing system that learns from historical booking information and recommends whether the current price should be:

**Decreased, Kept, or Increased.**

---

# Dataset

The project uses the **Hotel Booking Demand Dataset**.

The dataset contains approximately:

**119,390 records and 32 columns.**

Important attributes include:

- Hotel
- Is Canceled
- Lead Time
- Arrival Date
- Arrival Year
- Arrival Month
- Arrival Week Number
- Arrival Day
- Stays in Weekend Nights
- Stays in Week Nights
- Adults
- Children
- Babies
- Meal
- Country
- Market Segment
- Distribution Channel
- Is Repeated Guest
- Previous Cancellations
- Previous Bookings
- Booking Changes
- Deposit Type
- Agent
- Company
- Days in Waiting List
- Customer Type
- ADR
- Required Car Parking Spaces
- Total of Special Requests
- Reservation Status
- Reservation Status Date

---

# Project Architecture

```text
Dynamic-Pricing-Reinforcement-Learning/
│
├── notebooks/
│   ├── Data analysis notebooks
│   ├── Feature engineering notebooks
│   ├── Pricing environment experiments
│   ├── Q-Learning training
│   ├── Price prediction
│   └── Pricing evaluation
│
├── reports/
│   ├── models/
│   │   ├── pricing_agent.pkl
│   │   └── q_learning_agent.pkl
│   │
│   ├── training_history.csv
│   ├── training_rewards.csv
│   └── training_report.txt
│
├── src/
│   ├── data/
│   │   └── data_loader.py
│   │
│   ├── features/
│   │   └── feature engineering modules
│   │
│   ├── rl/
│   │   ├── pricing_environment.py
│   │   ├── pricing_data_environment.py
│   │   ├── q_learning_agent.py
│   │   ├── price_predictor.py
│   │   └── pricing_evaluation.py
│   │
│   └── utils/
│
├── config.py
├── requirements.txt
├── PROJECT_OVERVIEW.md
└── README.md                      

---

# Week 1 — Project Setup, Data Loading & Initial Preprocessing

## Overview

During Week 1, I started the Dynamic Pricing using Reinforcement Learning project. The main focus was to understand the Hotel Booking Demand Dataset, set up the project structure, configure Git and GitHub, and develop the initial data loading and preprocessing pipeline.

## Objectives

- Initialize the Dynamic Pricing Reinforcement Learning project
- Understand the hotel booking dataset
- Create a modular project structure
- Implement a reusable data loading module
- Perform initial data cleaning
- Analyze missing and duplicate records
- Perform initial exploratory data analysis
- Set up Git and GitHub for version control

## Work Completed

### 1. Project Initialization

- Created the Dynamic-Pricing-Reinforcement-Learning project repository.
- Created the required project directories.
- Configured Git and connected the project with GitHub.
- Added project configuration files.
- Added requirements and project documentation.
- Organized the code into separate modules for better maintainability.

### 2. Dataset Understanding

The project uses the Hotel Booking Demand Dataset.

The dataset contains 119,390 records and 32 columns.

Important attributes include:

- Hotel type
- Is canceled
- Lead time
- Arrival date
- Number of adults
- Number of children
- Number of weekend nights
- Number of week nights
- Market segment
- Customer type
- ADR (Average Daily Rate)
- Booking changes
- Previous cancellations
- Special requests
- Reservation status

I studied the dataset structure and identified the important variables that could later be used for dynamic pricing and reinforcement learning.

### 3. Data Loading

Implemented a reusable DataLoader class using Python and Pandas.

The DataLoader was designed to:

- Locate the hotel booking dataset
- Read the CSV file
- Load the dataset into a Pandas DataFrame
- Display basic dataset information
- Return the loaded dataset for further processing

The dataset was successfully loaded with:

119,390 rows × 32 columns

### 4. Data Cleaning

Performed the initial data cleaning process.

The following activities were completed:

- Checked the dataset for duplicate records
- Removed duplicate records
- Checked missing values in each column
- Identified columns containing missing information
- Handled missing values appropriately
- Checked data types
- Verified the cleaned dataset
- Ensured the dataset was suitable for further analysis

### 5. Exploratory Data Analysis

Performed initial exploratory analysis to understand the characteristics of the booking data.

The analysis included:

- Dataset shape
- Column information
- Numerical and categorical variables
- Missing-value distribution
- Booking patterns
- Cancellation information
- Customer information
- Market segments
- Pricing-related information

This analysis helped identify the variables that could be useful for the future dynamic pricing model.

### 6. Project Structure

Created a modular project structure so that different parts of the system could be developed independently.

The structure included:

Dynamic-Pricing-Reinforcement-Learning/

├── notebooks/
├── reports/
├── src/
│   ├── data/
│   ├── features/
│   ├── rl/
│   └── utils/
├── config.py
├── requirements.txt
├── PROJECT_OVERVIEW.md
└── README.md

### 7. Git and GitHub

Configured Git for project version control.

The development work was tracked using Git commits and pushed to the GitHub repository regularly.

This helped maintain a history of changes and allowed the project development progress to be monitored.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git
- GitHub

## Techniques Used

- Data Loading
- Data Cleaning
- Duplicate Removal
- Missing Value Analysis
- Data Type Validation
- Exploratory Data Analysis
- Modular Programming
- Version Control

## Week 1 Outcome

By the end of Week 1, the project foundation was successfully created. The Hotel Booking Demand Dataset was loaded and analyzed, duplicate and missing-value issues were investigated and addressed, and the initial preprocessing pipeline was implemented.

The cleaned and structured dataset was prepared for the next stage of the project, which involved feature engineering and preparation of pricing-related information for the Reinforcement Learning environment.

---

# Week 2 — Feature Engineering & Reinforcement Learning Preparation

## Overview

During Week 2, I focused on preparing the cleaned Hotel Booking Demand Dataset for the Dynamic Pricing Reinforcement Learning system. The main activities included detailed data analysis, feature engineering, identification of pricing-related variables, and preparation of the data for the Reinforcement Learning environment.

## Objectives

- Perform detailed data preprocessing
- Analyze missing values and important dataset features
- Perform feature engineering
- Identify pricing-related variables
- Prepare data for Reinforcement Learning
- Create reusable feature engineering modules
- Improve the modular project structure

## Work Completed

### 1. Missing Value Analysis

Performed detailed analysis of missing values in the hotel booking dataset.

The following activities were completed:

- Identified columns containing missing values
- Analyzed the distribution of missing data
- Selected appropriate methods for handling missing values
- Validated the dataset after preprocessing
- Ensured the processed data was suitable for further development

### 2. Feature Engineering

Performed feature engineering to transform the raw hotel booking data into useful information for the dynamic pricing system.

The following variables were analyzed and prepared:

- Lead time
- Number of adults
- Number of children
- Number of guests
- Stay duration
- Weekend nights
- Week nights
- Hotel type
- Market segment
- Customer type
- ADR (Average Daily Rate)
- Cancellation information
- Booking changes
- Special requests
- Arrival-related information

These features were selected because they can provide useful information about customer behavior, booking patterns, demand, and pricing conditions.

### 3. Pricing-Related Feature Preparation

Identified the important factors that can influence a hotel pricing decision.

For example:

- Lead time provides information about how early a customer makes a booking.
- Number of guests provides information about booking demand.
- Stay duration provides information about the expected occupancy period.
- Market segment provides information about the type of customer.
- ADR provides information about the current average room price.
- Hotel type provides information about the property category.
- Cancellation information provides additional information about booking behavior.

These variables were prepared to support the future pricing decision process.

### 4. Data Transformation

Converted and organized relevant raw dataset information into a structured format that could be used by the Reinforcement Learning environment.

The objective was to make the data easier to process during the later stages of:

- State creation
- Action selection
- Reward calculation
- Agent training

### 5. Feature Engineering Module

Created reusable feature engineering code inside the project source structure.

The feature engineering logic was separated from the data loading and Reinforcement Learning components.

This modular approach made the project easier to:

- Maintain
- Debug
- Test
- Reuse
- Extend

### 6. Reinforcement Learning Problem Formulation

Started converting the dynamic pricing problem into a Reinforcement Learning problem.

The basic Reinforcement Learning workflow was defined as:

State → Action → Reward → Next State

The pricing agent was designed to select one of three possible actions:

0 → Decrease Price

1 → Keep Price

2 → Increase Price

The goal of the agent is to learn which pricing action can provide a higher reward for different observed states.

### 7. Project Structure Improvement

Organized the source code into separate modules for different responsibilities.

The project structure included:

src/

├── data/

├── features/

├── rl/

└── utils/

This separation allowed the data processing and Reinforcement Learning components to be developed independently.

### 8. Preparation for RL Environment

Prepared the project for the next development stage, where the processed hotel booking data would be connected to a Gymnasium-based pricing environment.

The planned interaction was:

Customer/Booking Data
        ↓
State
        ↓
RL Agent
        ↓
Pricing Action
        ↓
Reward
        ↓
Next State

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git
- GitHub

## Techniques Used

- Data Preprocessing
- Missing Value Analysis
- Feature Engineering
- Data Transformation
- Exploratory Data Analysis
- Pricing Feature Identification
- Reinforcement Learning Problem Formulation
- State and Action Design
- Modular Programming
- Git Version Control

## Week 2 Outcome

By the end of Week 2, the hotel booking dataset had been further processed and transformed into useful pricing-related information. Important features influencing hotel pricing were identified and prepared for the Reinforcement Learning stage.

The project was successfully prepared to move from data preprocessing and feature engineering into the development of the Dynamic Pricing Reinforcement Learning environment.

---

# Week 3 — Reinforcement Learning Environment & Q-Learning Agent

## Overview

During Week 3, I moved the project from data preprocessing and feature engineering into the Reinforcement Learning development stage. The main focus was to build the Dynamic Pricing environment, connect the hotel booking data with the environment, define pricing actions and states, and implement and train a Q-Learning agent.

## Objectives

- Build the Dynamic Pricing Reinforcement Learning environment
- Define the state and action spaces
- Implement pricing actions
- Design the reward mechanism
- Connect hotel booking data to the RL environment
- Implement a Q-Learning agent
- Implement exploration and exploitation
- Train the RL agent
- Save the trained model and training results

## Work Completed

### 1. Dynamic Pricing Environment

Created the Dynamic Pricing environment using Gymnasium.

The environment represents the interaction between the pricing agent and the hotel booking data.

The basic Reinforcement Learning workflow was implemented as:

State → Action → Reward → Next State

The environment allows the agent to observe the current state, select a pricing action, receive a reward, and move to the next state.

### 2. Action Space

Defined three possible pricing actions for the agent:

0 → Decrease Price

1 → Keep Price

2 → Increase Price

The environment uses a discrete action space:

Discrete(3)

This allows the Q-Learning agent to select one of the three pricing decisions at every step.

### 3. Observation Space

Created the observation space using Gymnasium's Box space.

The environment represents important pricing-related information as the current state.

The state information includes values related to:

- Hotel/booking information
- Current price
- Lead time
- Demand-related information

The observation space was tested successfully with the pricing environment.

### 4. Reward Mechanism

Implemented a reward mechanism to measure the outcome of the selected pricing action.

The reward is used by the Q-Learning agent to understand whether an action is beneficial.

The agent attempts to learn actions that provide higher future rewards.

The learning process can be represented as:

State → Action → Reward → Next State

### 5. Hotel Booking Data Integration

Connected the Hotel Booking Demand Dataset to the Reinforcement Learning environment.

The reusable DataLoader module was used to load the dataset.

The dataset contains:

119,390 rows × 32 columns

The booking data was passed into the pricing environment so that the agent could interact with data-driven states.

### 6. Pricing Data Environment

Created a separate pricing data environment to connect the actual hotel booking records with the previously developed pricing environment.

This helped move the project from a simulated environment toward a data-driven Reinforcement Learning workflow.

The data flow became:

Hotel Booking Dataset
        ↓
DataLoader
        ↓
Pricing Data Environment
        ↓
State
        ↓
Pricing Agent
        ↓
Action
        ↓
Reward
        ↓
Next State

### 7. Q-Learning Agent

Implemented a Q-Learning agent for learning the best pricing action for each state.

The agent maintains a Q-table containing the expected reward for every state-action combination.

The basic concept used was:

State → Action → Q-value

A higher Q-value indicates that the corresponding action is expected to provide a better future reward for that state.

### 8. Epsilon-Greedy Strategy

Implemented an epsilon-greedy strategy to balance exploration and exploitation.

During the beginning of training, the agent explores different pricing actions.

As training progresses, epsilon gradually decreases, allowing the agent to use the actions that it has learned to be more rewarding.

This allows the model to avoid selecting only one action from the beginning and provides opportunities to discover better pricing decisions.

### 9. Q-Table Training

Trained the Q-Learning agent using the Dynamic Pricing environment.

The agent learned Q-values for different states and pricing actions.

The Q-table contained values for:

- Decrease Price
- Keep Price
- Increase Price

The training process showed that the agent was learning different pricing preferences for different states.

### 10. Training Results

The Q-Learning agent was trained for:

100 Episodes

Example training results included:

Episode 10 → Reward: 520.00

Episode 20 → Reward: 572.90

Episode 30 → Reward: 593.80

Episode 40 → Reward: 566.70

Episode 50 → Reward: 546.20

Episode 60 → Reward: 556.00

Episode 70 → Reward: 575.60

Episode 80 → Reward: 584.50

Episode 90 → Reward: 580.30

Episode 100 → Reward: 582.20

Total Training Reward:

56271.5

Final Epsilon:

0.6057

### 11. Model Saving

Saved the trained Q-Learning agent so that it could be reused for prediction and evaluation without retraining.

The trained model was stored in:

reports/models/q_learning_agent.pkl

Training results were also stored in the reports directory for later analysis.

### 12. Git Version Control

Tracked the development using Git and GitHub.

Created commits for:

- Dynamic Pricing environment
- Hotel booking data integration
- Q-Learning implementation
- Training components
- Model outputs

The changes were committed and pushed to the GitHub repository.

## Technologies Used

- Python
- Pandas
- NumPy
- Gymnasium
- Scikit-learn
- Git
- GitHub
- Pickle

## Techniques Used

- Reinforcement Learning
- Q-Learning
- Q-Table
- Epsilon-Greedy Strategy
- Exploration vs Exploitation
- State Representation
- Action Space Design
- Observation Space Design
- Reward Engineering
- Environment Simulation
- Data-Driven RL Environment
- Model Serialization
- Modular Programming
- Git Version Control

## Week 3 Outcome

By the end of Week 3, the project had successfully progressed from data preprocessing into a working Reinforcement Learning system.

The Dynamic Pricing environment was created, hotel booking data was connected to the environment, the three pricing actions were implemented, and a Q-Learning agent was trained for 100 episodes.

The trained Q-Learning model and training results were saved and prepared for the next stage: generating pricing predictions and evaluating the learned pricing policy.

---

# Week 4 — Price Prediction, Model Evaluation & Project Finalization

## Overview

During Week 4, I focused on completing the Dynamic Pricing Reinforcement Learning system by using the trained Q-Learning agent to generate pricing decisions, analyzing the learned Q-table, evaluating the pricing policy, and finalizing the project.

## Objectives

- Load the trained Q-Learning model
- Generate pricing predictions
- Convert Q-values into pricing decisions
- Analyze the learned Q-table
- Evaluate the pricing decision distribution
- Test the trained agent
- Handle and resolve implementation errors
- Save the required project outputs
- Complete the project structure and documentation
- Maintain the final project using Git and GitHub

## Work Completed

### 1. Trained Model Loading

Loaded the previously trained Q-Learning agent from the saved model file:

reports/models/q_learning_agent.pkl

The saved agent was successfully restored and used for generating pricing decisions without retraining the model.

### 2. Price Prediction Module

Created a price prediction module to use the trained Q-Learning agent for making pricing decisions.

The prediction system evaluates the Q-values for a given state and selects the action with the highest expected reward.

The three possible pricing decisions are:

0 → Decrease Price

1 → Keep Price

2 → Increase Price

The prediction workflow is:

State → Q-Table → Highest Q-value → Pricing Action

### 3. Pricing Predictions

Tested the trained agent with different states and generated pricing recommendations.

Example predictions included:

State 0 → Keep Price

State 1 → Increase Price

State 2 → Increase Price

State 3 → Keep Price

State 4 → Keep Price

This demonstrated that the trained agent could convert learned Q-values into practical pricing decisions.

### 4. Q-Table Analysis

Analyzed the learned Q-table to understand the behavior of the trained agent.

Example Q-values:

State 0 | Decrease: 213.99 | Keep: 266.08 | Increase: 205.66

State 1 | Decrease: 202.69 | Keep: 229.06 | Increase: 278.14

State 2 | Decrease: 202.20 | Keep: 205.43 | Increase: 271.29

State 3 | Decrease: 207.33 | Keep: 265.57 | Increase: 205.50

State 4 | Decrease: 190.25 | Keep: 264.02 | Increase: 215.43

The highest Q-value for each state indicates the preferred pricing action learned by the agent.

### 5. Pricing Policy Evaluation

Created a pricing evaluation module to analyze the decisions produced by the trained agent.

The evaluation counted how many states selected each pricing action.

The final decision distribution was:

Decrease Price → 1 state (10%)

Keep Price → 7 states (70%)

Increase Price → 2 states (20%)

This analysis helped understand the overall behavior of the learned pricing policy.

### 6. Model Evaluation

Evaluated the trained agent using:

- Q-value analysis
- Pricing predictions
- Pricing decision distribution
- Training rewards
- Learned pricing policy

The evaluation confirmed that the agent was producing different pricing actions depending on the state rather than selecting actions randomly.

### 7. Debugging and Error Resolution

During Week 4, several implementation issues were encountered and resolved.

These included:

- Python module import errors
- Circular import issues
- Incorrect DataLoader method usage
- Q-Learning model loading issues
- Object access errors while loading the trained agent
- Git tracking and commit issues
- GitHub connection problems

For example, the trained Q-Learning model was stored as a Python object, so it had to be accessed through its object attributes rather than treating it as a dictionary.

These debugging activities improved the reliability of the final project.

### 8. Project Output Files

The final project contains important model and evaluation outputs.

The reports directory contains:

reports/
├── models/
│   ├── pricing_agent.pkl
│   └── q_learning_agent.pkl
├── training_history.csv
├── training_rewards.csv
└── training_report.txt

These files provide the trained models and training/evaluation results required for demonstrating the project.

### 9. Final Reinforcement Learning Workflow

The complete project workflow was finalized as:

Hotel Booking Dataset
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Pricing Environment
        ↓
State Representation
        ↓
Pricing Actions
        ↓
Reward Calculation
        ↓
Q-Learning Agent
        ↓
Training
        ↓
Q-Table
        ↓
Trained Agent
        ↓
Price Prediction
        ↓
Pricing Policy Evaluation

### 10. Final Project Structure

The project was organized into separate modules for data processing, Reinforcement Learning, prediction, and evaluation.

Dynamic-Pricing-Reinforcement-Learning/

├── notebooks/
│   ├── 20_pricing_environment.py
│   ├── 21_pricing_data_environment.py
│   ├── 23_train_q_learning.py
│   ├── 25_price_prediction.py
│   └── 26_pricing_evaluation.py
│
├── reports/
│   ├── models/
│   │   ├── pricing_agent.pkl
│   │   └── q_learning_agent.pkl
│   ├── training_history.csv
│   ├── training_rewards.csv
│   └── training_report.txt
│
├── src/
│   ├── data/
│   │   └── data_loader.py
│   ├── features/
│   ├── rl/
│   │   ├── pricing_environment.py
│   │   ├── pricing_data_environment.py
│   │   ├── q_learning_agent.py
│   │   ├── price_predictor.py
│   │   └── pricing_evaluation.py
│   └── utils/
│
├── config.py
├── requirements.txt
├── PROJECT_OVERVIEW.md
└── README.md

### 11. Git and GitHub Finalization

Used Git throughout the final development stage to track all changes.

The final commits covered:

- Price prediction implementation
- Trained agent integration
- Pricing evaluation
- Q-table analysis
- Model outputs
- Project improvements
- Documentation

The final changes were committed and successfully pushed to the GitHub repository.

## Technologies Used

- Python
- Pandas
- NumPy
- Gymnasium
- Scikit-learn
- Matplotlib
- PyTorch
- Pickle
- Git
- GitHub

## Techniques Used

- Reinforcement Learning
- Q-Learning
- Q-Table
- Epsilon-Greedy Strategy
- State Representation
- Action Selection
- Reward Engineering
- Pricing Policy Learning
- Price Prediction
- Q-Value Analysis
- Policy Evaluation
- Decision Distribution Analysis
- Model Serialization
- Data Preprocessing
- Feature Engineering
- Modular Programming
- Debugging
- Git Version Control

## Week 4 Outcome

By the end of Week 4, the Dynamic Pricing Reinforcement Learning project was completed as an end-to-end working prototype.

The final system can:

- Load hotel booking data
- Process and prepare the data
- Create pricing-related states
- Generate pricing actions
- Calculate rewards
- Train a Q-Learning agent
- Store the learned Q-table
- Save and load the trained model
- Generate pricing recommendations
- Analyze Q-values
- Evaluate the learned pricing policy
- Calculate the distribution of pricing decisions

The final pricing system demonstrates how Reinforcement Learning can be applied to dynamic hotel pricing by learning whether to decrease, keep, or increase the price based on the observed state.

## Final Project Learning

Through this project, I gained practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Reinforcement Learning
- Q-Learning
- Gymnasium environment development
- State and action design
- Reward design
- Epsilon-greedy exploration
- Model training
- Model evaluation
- Price prediction
- Policy evaluation
- Q-table interpretation
- Python modular programming
- Debugging
- Git and GitHub
- End-to-end Machine Learning project development