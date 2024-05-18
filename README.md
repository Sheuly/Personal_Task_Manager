# Personal_Task_Manager
This repository conatains an application which is done as a requirement for the completion of the course 'Advanced Software Engineering'. This is a GUI based application system built on python. 'tkinter' library is used for creating the graphical user interface (GUI).
- Project proposal link:  [Proposal.pdf](https://github.com/Sheuly/Personal_Task_Manager/blob/main/Project_Proposal.pdf)

## 1. Git
GitHub is used as a web-based platform that uses Git for version control and provides a collaborative environment. It hosts Git repositories and offers additional features like issue tracking, pull requests, code review, and continuous integration/continuous deployment (CI/CD) pipelines, enhancing the workflow and collaboration with Sonarcloud. 
- The whole project can be found [Here](https://github.com/Sheuly/Personal_Task_Manager)

## 2. UML
UML diagrams are used to visualize, document, and design the architecture and behavior of software systems.  I used two different softwares StarUml and draw.io to build those. Here I have used three uml diagrams.  

  **1. Use Case diagram:** Use case diagrams show the interactions between users and a system's functionalities.
     - [Use Case Diagram link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/2.%20UML/1.%20UseCaseDiagram.JPG)  
  **2. Activity diagram:** Activity diagram illustrates the flow of control or activities within a system.
     - [Activity Diagram Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/2.%20UML/2.%20ActivityDiagram.JPG)  
  **3. Class diagram:** Class diagram represents the static structure of a system by showing its classes, attributes, methods, and relationships.
     - [Class Diagram Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/2.%20UML/3.%20ClassDiagram.JPG)  
## 3. DDD
In this project, I chose a Domain-driven design (DDD) in order to identifying the problem domains to create a software solution according to the domain inputs. It provides a structured approach to prioritize the domains and build software that closely reflects that understanding. 

 The following steps are listed below: 
 
   **A)** Various possible fields and events are gathered through brain storming and significant domains are listed. [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/3.%20DDD/1.%20EventStorming.JPG)    
   **B)** A clear strategic design of the domains is provided coming from event storming. [Link 1](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/3.%20DDD/2.%20StrategicDesign.JPG) and [Link 2](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/3.%20DDD/2.%20StrategicDesign-2.JPG)  
   **C)** Core domain Chart. [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/3.%20DDD/3.%20CoreDomainChart.JPG)    
   **D)** Bounded context to create boundary where each domain is applied. [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/3.%20DDD/4.%20Context%20Mapping.JPG)


## 4. Metrics
 I have used Sonarcloud to perform the analysis and calculate the metrics. I have measured the following metrices.

   1. Vulnerabilities: 0
   2. Hotspots Reviewed: 100%
   3. Code Smells: 0
   4. Duplications: 0%
   5. Quality Gate Status(Passed):Status - [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/4.%20Metric/QualityGate.JPG)

The overall metrics measurement overview is provided [here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/4.%20Metric/Metric.JPG)

## 5. Clean Code Development:
My project seems to satisfy as a clean code development based on the following criteria:  

**(A)**  
1. Reliability : Easy and reliable to import and integrate. Reliability [check](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/5.%20CleanCodeDevelopment/1.%20Reliability%20Rating.JPG)   
2. Comments: Use clear and concise comments that explain the  the code. Comments [check](https://github.com/Sheuly/Personal_Task_Manager/blob/main/src/PersonalTaskManager.py) 
3. Naming conventions: Use of descriptive names for functions. [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/src/PersonalTaskManager.py)
4. Duplication: Sonarcloud metrics duplication is 0. [Duplications check](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/5.%20CleanCodeDevelopment/2.Duplication.JPG)
5. Modularity: Codes are written Using indentation, spacing, and line breaks to improve the code quality. [Check_here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/src/PersonalTaskManager.py)

**(B)**
Clean code development [Cheatsheet](https://github.com/Sheuly/Personal_Task_Manager/blob/main/Clean%20Code%20Development%20cheat%20sheet%20for.pdf)


## 6. Build and 7. Continuous Delivery

Since my project is on python that is why I used Github Action for continuous analysis and deployment.

- Build: The project pipeline starts with building the project, compiling source code, bundling assets, and generating artifacts for deployment. 
Link is provided [here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/6.%20Build/build.JPG).

- Test: Unit tests and integration tests are executed to ensure the task execution, quality measure and reliability of the codebase.
Link is provided [here](https://github.com/Sheuly/Personal_Task_Manager/actions/runs/9140769393/job/25134469737).

- GitHub Actions: Github Actions let us to collaborate between Continuous Integration (CI) and Continuous Deployment (CD) pipelines directly within your GitHub repository. I used a YAML-based file to define my CI/CD pipeline.
Link is provided [here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/.github/workflows/build.yml).

## 8. UnitTest

I have used pytest to perform unittest. There I have checked several measures to check my task execution and bug free. The following functions seemed to behave exactly when the were passed through Github Action. 

The test file is provided [here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/src/test_PersonalTaskManager.py)

Three of them is listed below:

- test_add_task: This function checks by adding some random text. It's then passed through the listbox to get inserted.
- test_delete_task: This function checks the functionality after selecting a data from listbox. MagicMock invoked to access the deletion.
- test_mark_complete: this function selects the value retrurned by listbox thorugh MagicMoick. It then update the task as completed and removes the previous input.

The functions were performed as expected and the tese parformance got passed. The test result is provided [here](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/8.%20Unittest/unitTest.JPG)

## 9. IDE
I used visual studio code as an IDE to run my python project and test the work. I also prefer to implement on jupyter notebook but I found it hard to apply the untitesting.
My favourite shortcuts are provided.

- Alt+Click : It Inserts a cursor
- Ctrl+Shift+N: It allows navigate to a file
- ctrl + L: Clear Console
- Ctrl+Shift+W : Close window/instance
- Ctrl + Shift + K: delete the selected line.
- Ctrl + Shift + T: for navigating to a test.
- F5: Start Debugging
- Shift + F5: Stop Debugging

## 10. DSL
Below is a sample DSL code for my project application. Although it does not contribute to my project still I decided to learn and implement it in my problem context so that I can observe the change and benefits it can provide with. I understood that it can provide provide a concise and expressive way to solve problems within a specific domain, making it easier for domain understand, communicate ideas and solutions effectively. This can be very helpful while working with large problems.

My sample DSL is provided with [this](https://github.com/Sheuly/Personal_Task_Manager/blob/main/src/DSL_sample.py) link.

## 11. Functional Programming
My project is covered with all the functional aspects mentioned.  
- Side effect free functions: All of my codes are well side effect free and can be implimented and also extended. [Link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/11.%20FunctionalProgramming/SideEffectFree.JPG) is provided
- Use of Higher oder function: The project uses significant but not that of higher ordered. This project designed in [proposal](https://github.com/Sheuly/Personal_Task_Manager/blob/main/Project_Proposal.pdf) is big and yet to impliment some significant functions.
- functions as parameters and return values: My functiones are used for passing as parameters. The tasks are invoked functions and passed to the listbox. The corresponding [link](https://github.com/Sheuly/Personal_Task_Manager/blob/main/TASK_Folder/11.%20FunctionalProgramming/SideEffectFree.JPG) is provided.







      


     

