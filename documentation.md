Video Surveillance Enhancement Using Deep Learning
 
Project ID: FYP-F25-32
 Session: BSCS Fall 2022 to 2026
Project Advisor: Mr. Najaf Ali

Submitted By

Umar Farooq   	70140696
Muhammad Zain 	70135357
Zarnab Waheed 	70140570



BACHELOR OF SCIENCE IN SOFTWARE ENGINEERING
UNIVERSITY OF LAHORE
Declaration
We have read the project guidelines and we understand the meaning of academic dishonesty, in particular plagiarism and collusion. We hereby declare that the work we submitted for our final year project, entitled Video Surveillance Enhancement using deep learning is original work and has not been printed, published or submitted before as final year project, research work, publication or any other documentation.


Group Member 1 Name: Umar Farooq
SAP No: 70140696
Signature: .......................................


Group Member 2 Name: Muhammad Zain
SAP No: 70135357
Signature: .......................................


Group Member 3 Name: Zarnab Waheed
SAP No: 70140570
Signature: .......................................









Statement Of Submission
This is to certify that Umar Farooq (Roll No. 70140696), Muhammad Zain (Roll No. 70135357), and Zarnab Waheed (Roll No. 70140570) have successfully submitted the final project titled Video Surveillance Enhancement using deep learning at the Computer Science & IT Department, The University of Lahore, Lahore, Pakistan, in partial fulfillment of the requirements for the award of the degree of Bachelor of Science in Software Engineering (BSSE).























Supervisor Name:   ……………………… 
Signature:                ……………………… 
Date:                         ……………………… 
 

Dedication
This project is dedicated to our parents, who have always been a source of inspiration and strength. Their endless love, support, and prayers have been the driving force behind our success. We also dedicate this work to our respected teachers, whose guidance and encouragement paved the way for us to achieve this milestone.













Acknowledgement
We truly acknowledge the cooperation and help provided by Mr. Muhammad Najaf, Project Supervisor, Department of Software Engineering. He has been a constant source of guidance throughout the course of this project. His technical expertise and feedback were invaluable in shaping the direction of our work.
We would also like to thank the Faculty of Information Technology at The University of Lahore for providing the necessary resources and environment to complete this research. Finally, we are thankful to our friends and families whose silent support led us to complete our project successfully.
Date:
May 20, 2025


















Abstract
Public safety and security have become paramount concerns in rapidly urbanizing environments. Traditional surveillance methods, which rely heavily on manual monitoring of Closed-Circuit Television (CCTV) feeds, are often reactive, labor-intensive, and prone to human error due to fatigue. This project, "Video Surveillance Enhancement using deep learning," presents an automated, intelligent surveillance solution designed to address these limitations.
The proposed system leverages state of the art Deep Learning techniques, specifically the YOLOv8 architecture, to analyze real-time video streams. Unlike standard motion detection systems that generate frequent false alarms, this framework is trained to recognize specific behavioral anomalies, including fighting, weapon detection, and sudden panic. Upon detecting a threat, the system instantly logs the incident and triggers real time alerts on a centralized web dashboard, enabling security personnel to intervene proactively. The system is implemented using Python and OpenCV for video processing, with a web-based frontend for user interaction. Testing results demonstrate that the model achieves high accuracy in distinguishing between normal daily activities and aggressive behaviors, offering a scalable and cost-effective solution for modern security needs.















Area of Project
Artificial Intelligence (AI), Computer Vision, Deep Learning, Web Development, and Real-Time Surveillance Systems.

Technologies used
Python
OpenCV
YOLOv8
TensorFlow/PyTorch,
Flask (Backend)
React.js/HTML5 (Frontend),
MySQL/Firebase (Database)
Docker.















Table of Contents

Chapter 1: Introduction	1
1.1 Introduction	2
1.2 Types of Behavioral Anomalies	2
1.2.1 Aggressive Behavior (Violence/Fighting)	2
1.2.2 Weapon Detection	2
1.2.3 Loitering and Suspicious Movement	3
1.3 Project Purpose	3
1.4 Why Surveillance is Challenging	3
1.4.1 Role of AI in Surveillance	4
1.5 Objectives	4
1.6 Competitive Analysis	5
1.6.1 Existing Systems:	5
1.6.2 Proposed System Advantage:	5
2.1 SRS Introduction	7
2.2 Purpose	7
2.2.1 Key Goals:	7
2.2.2 Intended users:	7
2.3 Scope	8
2.4 What the system will do:	8
2.5 What the system will not do:	8
2.6 System Boundaries:	9
2.7 Deployment Scope:	9
2.7.1 Definitions, Acronyms, and Abbreviations	9
2.8 References	9
2.9 Overview	10
2.10 Overall description	10
2.10.1 Product perspective	10
2.10.2 Product Functions	11
2.11 User Characteristics	12
2.12 Constraints	12
2.13 Assumptions and Dependencies	12
2.13.1 Assumptions	12
2.13.2 Dependencies	13
2.14 Apportioning of Requirements	13
2.14.1 High-Priority Requirements	13
2.14.2 Medium-Priority Requirements	13
2.14.3 Low-Priority Requirements	13
2.15 Functional Requirements	14
2.15.1 User Authentication	14
2.15.2 Video Processing	14
2.15.3 AI-Based Prediction	14
2.15.4 Results Display	14
2.15.5 Data Privacy	14
2.15.6 Admin Panel	14
2.16 Non-Functional Requirements	15
2.16.1 Performance Requirements	15
2.16.2 Reliability and Availability	15
2.16.3 Security Requirements	15
2.16.4 Usability Requirements	15
2.16.5 Maintainability Requirements	15
Chapter 3: USE CASE ANALYSIS	16
3.1 Usecase Diagram User Login	17
3.2 Usecase Diagram Add Camera Feed	18
3.3 Usecase Diagram Detect Anomaly	19
3.4 Usecase Diagram Receive Real-Time Alert	20
3.5 Usecase Diagram View History Logs	21
3.6 Usecase Diagram Flag False Alarm	22
3.8 Usecase Diagram Monitor System Health	24
CHAPTER 4: SYSTEM DESIGN	25
4.1 Architecture Diagram	26
4.1.1 Layers in the Architecture:	26
4.1.2 Flow of Data:	26
4.2 Entity Relationship Diagram (ERD)	28
4.2.1 Main Entities and Their Descriptions:	28
4.2.2 Relationships Between Entities:	28
4.2.3 Data Dictionary	30
4.3 Class Diagram	32
4.3.1 Main Classes in the System:	32
Figure 11 Class Diagram	33
4.4 Activity Diagram	34
4.4.1 Use Case: "Detect Threat in Live Feed"	34
4.5 Sequence Diagram	36
Figure 13 Sequence Diagram	36
4.6 Collaboration Diagram	37
Figure 14 Collaboration Diagram	37
4.7 State Transition Diagram	38
4.8 Component Diagram	39
Figure 16 Component Diagram	39
4.9 Deployment Diagram	40















LIST OF FIGURE

FIGURE 1 USECASE DIAGRAM USER LOGIN	17
FIGURE 2 USECASE DIAGRAM ADD CAMERA FEED	18
FIGURE 3 USECASE DIAGRAM DETECT ANOMALY	19
FIGURE 4  USECASE DIAGRAM RECEIVE REAL-TIME ALERT	20
FIGURE 5 USECASE DIAGRAM VIEW HISTORY LOGS	21
FIGURE 6 USECASE DIAGRAM FLAG FALSE ALARM	22
FIGURE 7 USECASE DIAGRAM MANAGE USERS	23
FIGURE 8 USECASE DIAGRAM MONITOR SYSTEM HEALTH	24
FIGURE 9 SYSTEM ARCHITECTURE	27
FIGURE 10 ENTITY RELATIONSHIP DIAGRAM	29
FIGURE 11 CLASS DIAGRAM	33
FIGURE 12 ACTIVITY DIAGRAM	35
FIGURE 13 SEQUENCE DIAGRAM	36
FIGURE 14 COLLABORATION DIAGRAM	37
FIGURE 15 STATE-CHART DIAGRAM	38
FIGURE 16 COMPONENT DIAGRAM	39
FIGURE 17 DEPLOYMENT DIAGRAM	40










List Of Tables

TABLE 1  DEFINITIONS, ACRONYMS, AND ABBREVIATIONS	9
TABLE 2  SYSTEM COMPONENTS	11
TABLE 3 USER CHARACTERISTICS	12
TABLE 4 USECASE USER LOGIN	17
TABLE 5 USECASE ADD CAMERA FEED	18
TABLE 6 USECASE DETECT ANOMALY	19
TABLE 7 USECASE RECEIVE REAL-TIME ALERT	20
TABLE 8 USECASE VIEW HISTORY LOGS	22
TABLE 9 USECASE FLAG FALSE ALARM	23
TABLE 10 USECASE MANAGE USERS	24
TABLE 11 USECASE MONITOR SYSTEM HEALTH	25
TABLE 12 ERD SUMMARY	30
TABLE 13 USER TABLE 4.2.3.1 USER	30
TABLE 14 CAMERA TABLE 4.2.3.2 CAMERA	31
TABLE 15 ALERT TABLE 4.2.3.3 ALERT	31









 







Chapter 1: Introduction












1.1 Introduction
The problem of public safety is a burning issue in contemporary urban areas, where population growth and commercialization are ever rising. The conventional security systems are based largely on the use of Closed-Circuit Television (CCTV) systems that are used to track government areas, workplaces, and homes. But these systems are mainly used as passive tools of record keeping. They rely wholly on human operators to monitor video feeds and detect suspicious activity an activity that is labor intensive, expensive and open to human error. 
According to studies, the attention of a human operator would reduce considerably even after such a short period of constant monitoring as twenty minutes, causing him to miss the incidence and slow to react. In the vast majority of situations, CCTV is retrospectively checked to collect evidence after the crime or an accident has already taken place and is not used as a preventive device.
The integration of Artificial Intelligence (AI) and computer vision into surveillance infrastructure presents a transformative opportunity. By automating the detection of specific behavioral patterns, security systems can shift from reactive recording to proactive alerting. This project focuses on implementing a deep learning framework to automatically detect and classify abnormal human behaviors in real-time, thereby enhancing situational awareness and response efficiency.


1.2 Types of Behavioral Anomalies
There are three main categories of behavioral anomalies that this system focuses on, each representing a distinct security threat:
1.2.1 Aggressive Behavior (Violence/Fighting)
•	High-priority threat.
•	Involves rapid, chaotic movements between two or more individuals.
•	Early detection is crucial to prevent physical harm and property damage.
1.2.2 Weapon Detection
•	Critical security threat.
•	Involves the identification of specific objects such as handguns, knives, or rifles.
•	Requires high precision to distinguish between harmless objects (like a phone) and lethal weapons.

1.2.3 Loitering and Suspicious Movement
•	Preventive monitoring.
•	Involves an individual remaining in a restricted or sensitive area for an extended period without a clear purpose.
•	Often precedes theft, vandalism, or trespassing.

1.3 Project Purpose
This project is aimed at creating an AI-based surveillance system that can support security personnel through the application of computer vision and deep learning. The system will examine real-time video output of CCTV cameras to detect visual clues that can be associated with deviant behaviors. The system will provide a solution to the existing gap between manual surveillance and computer services in assistance of security, which will be easily reachable, precise, and effective in the case of the public and private institutions. The timely interventions to prevent incidences before they escalate is highly determined by the early detection.
This solution is designed to:
•	Grant security personnel a 24/7 supportive monitor.
•	Increase security coverage in places where it is not possible to utilize a permanent guard.
•	Provide real-time alert systems which are responsive.

1.4 Why Surveillance is Challenging
Effective surveillance traditionally involves continuous human monitoring, which is accurate but:
•	Physically exhausting
•	Costly due to salary requirements
•	Prone to "monitoring blindness" due to fatigue
This creates challenges in maintaining safety, especially in large complexes with hundreds of cameras. A single operator cannot effectively watch every screen simultaneously, meaning many threats go unnoticed until it is too late.



1.4.1 Role of AI in Surveillance
Advances in Artificial Intelligence (AI) and computer vision now offer new ways to assist in security. Deep learning models can process video frames at high speed to identify objects and actions that are difficult for a tired human eye to catch instantly. By training a deep learning model (YOLOv8) with labeled video data, we can create a system capable of:
•	Real-time detection of anomalies. 
•	Providing a confidence score for the detected threat
•	Assisting security staff in making informed decisions
This forms the foundation of our proposed AI-based anomaly detection system, which aims to offer a cost-effective, scalable, and robust tool for modern security needs.

1.5 Objectives
Problem: Conventional CCTV systems are based on a lot of manual-observation. Such processes are reactive and are resource-consuming and costly. The problem of limited security staff can be a burden to many organizations, creating blind spots and slow responses. Benefits of automated outreach through an AI-based solution that automates the initial screening on the basis of recognizing actions can also be viewed as a way to increase the workload in terms of operational costs and prompt intervention at the initial stage.
The primary goals of this project are focused on increased accuracy, speed, and automation of threat detection by artificial intelligence. Specific objectives are:
 Create an AI-Based Detection Model: Implement and train a Deep Learning model (YOLOv8n) that can recognize such human behaviors as fighting, weapon holding, and loitering by using high-quality video data.
 Create a Web Dashboard: Enact a safe, user-friendly online interface by which administrators can see live feeds and get automatic notifications.
 Make sure it is Real-Time and Accurate: Combine the AI model with the services that would allow running the diagnosis in real time, but with an extremely high accuracy and few false alarms.
 Support Data Security: Enhance the privacy of the application by making sure that the video streams are secured and that the logs stored are encrypted.
 Cutting Time and Cost of Monitoring: Reduce the cost and effort commensurately in the traditional surveillance through the automation of the initial detection process.
 Improve Security Levels: Have an affordable solution to the areas that do not afford high security teams.
 Provision Data to Audit: Develop a formal mechanism of recording and archive of the incident data to aid in future investigations and security audit.
1.6 Competitive Analysis
In the field of AI surveillance, various solutions exist that attempt to identify threats using motion detection or facial analysis. However, these are often limited in scope, accuracy, or affordability. Below is a comparison of existing solutions and how this project provides a competitive advantage.

1.6.1 Existing Systems:
Competitor	Strengths		Weaknesses
Hikvision Smart AI	Advanced hardware, facial recognition, widely available.	Requires expensive proprietary cameras; complex setup for small users.
Google Nest / Ring	Easy to use, cloud integration, mobile apps.	Focused on home use; lacks specific behavior analysis (fighting/panic).
Sighthound Video	Strong object detection, software-based.	High licensing costs; resource-intensive for standard hardware.

1.6.2 Proposed System Advantage:
•	Specifically designed for behavioral anomaly detection (actions) rather than just object detection.
•	Web-based platform for centralized access without specialized monitors.
•	Cost-effective implementation using open-source technologies (Python, YOLO).
The proposed system stands out by combining the speed of YOLOv8 with the specific requirement of action recognition. Unlike general-purpose home cameras that alert on any motion, this system discriminates between normal movement and specific threats, reducing false alarms.
















Chapter 2: SOFTWARE REQUIREMENT SPECIFICATION (SRS)











2.1 SRS Introduction
This paper will present the Software Requirements Specification (SRS) of the web-based application Behavioral Anomaly Detection and Classifications Using Deep Learning. It gives an in-depth elaboration of the functional and non-functional requirements, scope, features and constraints, as well as system behavior that will form a guideline in the lifecycle of the project.
2.2 Purpose
This document is meant to specify the specifications of an AI-based system, which can process video feeds and give a preliminary notification of security events. This report is addressed to the developers, stakeholders, and the evaluators of the end year project. It will be a foundation of system design, development, testing and deployment.
The system is designed to:
•	Analyze video frames from connected CCTV cameras using computer vision.
•	Classify whether the scene contains an anomaly (fighting, weapon, panic).
•	Assist security professionals in identifying threats without the need for continuous manual observation.
This tool is not a replacement for human security judgment, but it serves as a supportive screening system that provides quick, automated alerts.

2.2.1 Key Goals:
•	Provide a simple interface to manage camera feeds.
•	Use AI to make real-time predictions based on video data.
•	Support early intervention by offering instant alerts.
2.2.2 Intended users:
•	Security Administrators managing a facility.
•	Security Guards monitoring live feeds.
•	System developers and researchers working on surveillance AI.



2.3 Scope
This software system will:
•	Accept live video streams via RTSP/IP protocols.
•	Use a pre-trained deep learning model (YOLOv8) to analyze frames.
•	Provide detection feedback with a confidence score.
•	Generate system logs for all detected events.
•	Be accessible via a web browser with secure authentication.
The project is designed for public and private security sectors, specifically for small to medium-scale deployments.

2.4 What the system will do:
•	Allow admins to add/remove camera feeds through a simple web interface.
•	Use image processing and AI techniques to:
o	Detect humans and objects.
o	Analyze interactions (e.g., fighting).
o	Predict if a weapon is present.
•	Display an alert (e.g., "Violence Detected") with a confidence score.
•	Include an admin panel to manage user access and review incident history.

2.5 What the system will not do:
•	It will not physically intervene or stop a crime (it is a detection tool only).
•	It will not guarantee 100% accuracy in all lighting conditions.
•	It will not make legal judgments on the intent of the individuals detected.
•	It does not store continuous 24/7 video footage (only event logs/snapshots) to save storage.



2.6 System Boundaries:
•	Input: Live video stream from CCTV.
•	Processing: AI-based analysis of video frames.
•	Output: Prediction of Anomaly likelihood and Dashboard Alert.

2.7 Deployment Scope:
•	The system will run on a web-based platform (accessed through a browser).
•	It is meant for security support and early detection, not for autonomous law enforcement.

2.7.1 Definitions, Acronyms, and Abbreviations
Table 1  Definitions, Acronyms, and Abbreviations
Term / Acronym		Definition
AI	Artificial Intelligence The simulation of human intelligence in machines.
YOLO	You Only Look Once A real-time object detection algorithm.
CCTV	Closed-Circuit Television Video surveillance system.
RTSP	Real-Time Streaming Protocol for streaming video.
CNN	Convolutional Neural Network Deep learning model for image analysis
Input Stream	The live video feed provided by the camera.
Anomaly	An irregular behavior such as fighting or weapon possession.
Confidence Score	A numerical value showing how sure the AI is about the prediction.
Admin Panel	Dashboard used by the administrator to manage system operations.

2.8 References
 IEEE 830-1998 – IEEE Recommended Practice for Software Requirements Specifications.
 YOLOv8 Documentation – Ultralytics framework for object detection.
 Flask Documentation – Python Web Framework for backend development.
 OpenCV Documentation – Library for real-time computer vision.




2.9 Overview
This Software Requirements Specification (SRS) document provides a comprehensive description of the Video Surveillance Enhancement using deep learning. The primary objective is to assist in the early detection of security threats through video analysis.
The remainder of this document is organized as follows:
•	Section 3 describes the specific functional requirements.
•	Section 4 outlines non-functional requirements (performance, reliability).
•	Section 5 presents system models and diagrams.
•	Section 6 provides appendices and definitions.

2.10 Overall description
2.10.1 Product perspective

The system is a web-based surveillance tool that uses a Deep Learning model to analyze CCTV feeds for signs of danger. The platform enables security professionals to monitor multiple cameras, receive real-time alerts, and review logs. The goal is to make advanced surveillance accessible and efficient.














2.10.2 Product Functions       
ID	Name	Description	Input	Output	Requirements	Basic Work Flow
SC_01	Camera Integration	Connects to IP cameras	RTSP Link	Video Stream	Stable Network	Admin adds link -> System connects
SC_02	Frame Processing	Extracts frames for AI	Video Stream	Individual Frames	OpenCV	Model computes score -> Generates result
SC_03	Detection Engine	Detects anomalies	Video Frame	Feature Map / Class	YOLOv8 Model	Model computes score -> Generates result
SC_04	Alert System	Notifies users	Prediction Result	Dashboard Alert	WebSocket	Anomaly found -> Alert sent to UI
SC_05	Dashboard	Visualization interface	Live Data	Video + Overlays	React/HTML	User views feed -> See boxes/alerts
SC_06	Logging Module	Saves event history	Event Data	Database Entry	MySQL/Firebase	Alert triggers -> Data saved to DB
Table 2  System Components







2.11 User Characteristics
User Type	Technical Knowledge	Usage Purpose
Administrator	Advanced	Manage cameras, users, and system settings
Security Guard	Basic	Monitor the dashboard and respond to alerts
System Developer	Expert	Maintain code and update AI models
Table 3 User Characteristics
2.12 Constraints
The development and deployment are subject to the following constraints:
 Hardware Resources
•	Deep learning models require high processing power (GPU) for real-time analysis.
•	Performance depends on the server's capability to handle multiple streams.
 Camera Quality
•	Low-resolution or poorly lit video feeds will degrade detection accuracy.
 Internet/Network Dependency
•	A stable local network or internet connection is required to transmit video data.
 Accuracy and Reliability
•	The AI may produce false positives (detecting a fight when people are dancing) or false negatives. It is a support tool, not a perfect solution.

2.13 Assumptions and Dependencies
2.13.1 Assumptions
 Camera Positioning
•	It is assumed that cameras are positioned correctly to capture clear views of human activity.
 Stable Connectivity
•	The system assumes a continuous network connection between the cameras and the server.
 Lighting Conditions
•	It is assumed that the environment has sufficient lighting for the computer vision model to function.
2.13.2 Dependencies
 Third-Party Libraries
•	Depends on Ultralytics (YOLO), OpenCV, and PyTorch for AI processing.
•	Real-time inference depends on access to GPU (CUDA) resources.
2.14 Apportioning of Requirements
The project is divided into phases to ensuring critical components are delivered first.
2.14.1 High-Priority Requirements
 Video Stream Acquisition
•	Requirement: Ability to connect and view live CCTV feeds.
•	Timeline: Phase 1.
 Anomaly Detection Model
•	Requirement: Trained YOLOv8 model to detect violence and weapons.
•	Timeline: Phase 1 (Parallel).
 Real-Time Alerting
•	Requirement: Immediate visual notification upon detection.
•	Timeline: Phase 1.
2.14.2 Medium-Priority Requirements
 User Management
•	Requirement: Role-based login (Admin/Guard).
•	Timeline: Phase 2.
 Event Logging History
•	Requirement: Database storage of past alerts for review.
•	Timeline: Phase 2.
2.14.3 Low-Priority Requirements
 Mobile Optimization
•	Requirement: Mobile-responsive view for guards on patrol.
•	Timeline: Future Phase.
 Email/SMS Notifications
•	Requirement: External API integration for off-site alerts.
•	Timeline: Future Phase.
2.15 Functional Requirements
•	FR1: User shall be able to log in securely.
•	FR2: Admin shall be able to add RTSP camera links.
•	FR3: System shall process video frames in real-time.
•	FR4: System shall detect defined anomalies (Weapon, Violence).
•	FR5: System shall display a bounding box around the threat.
•	FR6: System shall generate a dashboard alert with a timestamp.
•	FR7: System shall log the incident to the database.
•	FR8: Admin shall be able to filter and search past logs.

2.15.1 User Authentication
 Login: Secure entry for Admins and Guards.
 Session: Auto-logout after inactivity.
2.15.2 Video Processing
 Ingestion: Accept H.264/MJPEG streams.
 Preprocessing: Resize frames to 640x640 for YOLO model input.
2.15.3 AI-Based Prediction
 Inference: Model analyzes frame and outputs class IDs and confidence.
 Threshold: Only display alerts if confidence > 50%.
2.15.4 Results Display
 Live View: Show video with red bounding boxes on threats.
 Sidebar: List recent alerts chronologically.
2.15.5 Data Privacy
 Encryption: Encrypt user credentials.
 Storage: Securely store snapshot evidence.
2.15.6 Admin Panel
 Management: Add/Edit/Delete Camera feeds.
 Monitoring: View system resource usage (CPU/RAM).

2.16 Non-Functional Requirements
2.16.1 Performance Requirements
 Latency
•	Detection and alerting must occur within 2 seconds of the event.
 Frame Rate
•	System must process at least 15 FPS for smooth monitoring.
2.16.2 Reliability and Availability
 Uptime
•	The system is designed for 24/7 operation with automatic reconnection logic for dropped camera feeds.
2.16.3 Security Requirements
 Access Control
•	Role-Based Access Control (RBAC) to prevent unauthorized configuration changes.
 Secure Transmission
•	Use HTTPS for the dashboard and secure RTSP for video.
2.16.4 Usability Requirements
 Interface
•	Intuitive dashboard requiring minimal training for security guards.
 Responsiveness
•	UI should adapt to desktop and tablet screens.
2.16.5 Maintainability Requirements
 Modularity
•	The AI engine should be decoupled from the UI to allow for easy model updates (e.g., upgrading to YOLOv9 in the future).

















Chapter 3: USE CASE ANALYSIS
















3.1 Usecase Diagram User Login

 
Figure 1 Usecase Diagram User Login

Field	Description
Use Case ID	UC_01
Use Case Name	User Login
Description	Users authenticate themselves to access the dashboard.
Primary Actor	User (Admin or Security Guard)
Secondary Actor	Authentication Database
Pre-Condition	User must have a registered account.
Post-Condition	User is logged in and redirected to the dashboard.
Basic Flow	User enters email and password → System verifies credentials → Access granted.
Alternate Flow	Invalid password or server timeout.

Table 4 Usecase User Login



3.2 Usecase Diagram Add Camera Feed
 
Figure 2 Usecase Diagram Add Camera Feed

Field	Description
Use Case ID	UC_02
Use Case Name	Add Camera Feed
Description	Admin connects a new CCTV camera to the system for monitoring.
Primary Actor	Administrator
Secondary Actor	Camera Network
Pre-Condition	Admin is logged in; Camera RTSP link is available.
Post-Condition	Camera is online and streaming to the AI engine.
Basic Flow	Admin inputs RTSP URL → System tests connection → Feed added to the list.
Alternate Flow	Connection failed or duplicate camera name.

Table 5 Usecase Add Camera Feed





3.3 Usecase Diagram Detect Anomaly
 
Figure 3 Usecase Diagram Detect Anomaly

Field	Description
Use Case ID	UC_03
Use Case Name	Detect Anomaly
Description	The system processes video frames to identify threats such as weapons or violent behavior.
Primary Actor	CCTV Source
Secondary Actor	AI Engine (YOLOv8)
Pre-Condition	The camera must be actively streaming video.
Post-Condition	An anomaly is detected and event data is generated.
Basic Flow	Frame captured → AI analyzes visual features → Threat identified (confidence > 50%).
Alternate Flow	No anomaly detected (normal behavior).

Table 6 Usecase Detect Anomaly



3.4 Usecase Diagram Receive Real-Time Alert
 
Figure 4  Usecase Diagram Receive Real-Time Alert


Field	Description
Use Case ID	UC_04
Use Case Name	Receive Alert
Description	Security personnel receive immediate notifications when a threat is detected.
Primary Actor	Security Guard
Secondary Actor	Notification Service
Pre-Condition	An anomaly has been detected by the AI system.
Post-Condition	The guard is informed and aware of the threat.
Basic Flow	System pushes alert → Dashboard flashes red → Guard views alert details.
Alternate Flow	Guard is offline; the alert is saved to history.
 
Table 7 Usecase Receive Real-Time Alert


3.5 Usecase Diagram View History Logs
 
Figure 5 Usecase Diagram View History Logs

Field	Description
Use Case ID	UC_05
Use Case Name	View History Logs
Description	Users review past security incidents and related evidence.
Primary Actor	Administrator / Guard
Secondary Actor	Database System
Pre-Condition	The user is logged in.
Post-Condition	Historical records are successfully displayed.
Basic Flow	User selects a date range → System queries the database → Logs are displayed.
Alternate Flow	No logs found or database connection error.

Table 8 Usecase View History Logs
3.6 Usecase Diagram Flag False Alarm
 
Figure 6 Usecase Diagram Flag False Alarm

Field	Description
Use Case ID	UC_06
Use Case Name	Flag False Alarm
Description	The user marks an incorrect detection (e.g., dancing mistaken for fighting) to help improve system accuracy.
Primary Actor	Security Guard
Secondary Actor	AI Learning Module
Pre-Condition	An alert must exist in the system logs.
Post-Condition	The alert is tagged as a “False Positive.”
Basic Flow	User opens the alert → Clicks “Report False Alarm” → System updates the record.
Alternate Flow	The alert has already been verified.
Table 9 Usecase Flag False Alarm
3.7 Usecase Diagram Manage Users
 
Figure 7 Usecase Diagram Manage Users

Field	Description
Use Case ID	UC_07
Use Case Name	Manage Users
Description	Admin creates or updates access for other staff members.
Primary Actor	Administrator
Secondary Actor	Database
Pre-Condition	Admin has root privileges.
Post-Condition	The user list is updated successfully.
Basic Flow	Admin selects “Users” → Adds new user details → Saves to the database.
Alternate Flow	Email already in use.

Table 10 Usecase Manage Users




3.8 Usecase Diagram Monitor System Health


 
Figure 8 Usecase Diagram Monitor System Health

Field	Description
Use Case ID	UC_08
Use Case Name	Monitor System Health
Description	Admin checks server performance to ensure the AI system is running smoothly.
Primary Actor	Administrator
Secondary Actor	Server Hardware
Pre-Condition	The system is running.
Post-Condition	Performance metrics are displayed.
Basic Flow	Admin views the status dashboard → System retrieves GPU/CPU stats → Metrics are displayed as graphs.
Alternate Flow	Sensor data unavailable.

Table 11 Usecase Monitor System Health














CHAPTER 4: SYSTEM DESIGN










4.1 Architecture Diagram
Overview:
The architecture of the Behavioural Anomaly Detection and Classifications Using Deep Learning framework follows a modular, layered architecture that integrates a video ingestion layer, a deep learning processing engine, a backend server, and a frontend dashboard.
4.1.1 Layers in the Architecture:
4.1.1.1 Frontend (Web UI)
 Built using HTML/CSS/JavaScript or React.js.
 Provides interfaces for:
•	Viewing live multi-camera grids.
•	Receiving visual alerts.
•	Managing camera configurations.
 Sends API requests to the backend server.
4.1.1.2 Backend (Flask/Django API)
 Acts as the controller between the user and the AI engine.
 Handles:
•	User authentication (Login/Logout).
•	RTSP stream management.
•	Database operations (CRUD).
•	Serving video streams to the client.
4.1.1.3 AI Engine (YOLOv8 Processing Unit)
 Developed using Python, OpenCV, and Ultralytics YOLO.
 Performs:
•	Frame extraction from live video.
•	Object and Action detection (Person, Weapon, Fight).
•	Confidence score calculation (e.g., 92% Weapon Detected).
4.1.1.4 Database (MySQL/Firebase)
 Stores:
•	User credentials.
•	Camera details (IP, Name, Location).
•	Incident Logs (Timestamp, Type, Snapshot Path).


4.1.2 Flow of Data:
 Camera streams video to the server.
•	Backend captures frames using OpenCV.
•	Frames are passed to the AI Model.
•	AI Model detects an anomaly and returns coordinates/labels.
•	System saves the event to the Database.
•	System pushes an alert to the Frontend UI.

 
Figure 9 System Architecture














4.2 Entity Relationship Diagram (ERD)
The Entity Relationship Diagram illustrates the logical structure of the database. It shows how different entities in the system are related to one another. This is crucial for understanding how data regarding users, cameras, and alerts will be stored.
4.2.1 Main Entities and Their Descriptions:
4.2.1.1 User
Represents the operators of the system.
 Attributes:
•	UserID (PK): Unique identifier.
•	Username: Name used for login.
•	Password: Encrypted string.
•	Role: Admin or Viewer.
4.2.1.2 Camera
Stores connection details for CCTV feeds.
 Attributes:
•	CameraID (PK): Unique identifier.
•	CameraName: Descriptive location name.
•	RTSP_URL: Network address of the stream.
•	Status: Online/Offline.
4.2.1.3 Alert
Stores details of detected anomalies.
 Attributes:
•	AlertID (PK): Unique identifier.
•	CameraID (FK): Reference to the source camera.
•	Type: Fighting, Weapon, etc.
•	Confidence: Accuracy score.
•	Timestamp: Time of detection.
•	Snapshot: Path to the saved image evidence.
4.2.2 Relationships Between Entities:
•	User–Camera: One Admin can manage multiple Cameras.
•	Camera–Alert: One Camera can generate multiple Alerts.


 
Figure 10 Entity Relationship Diagram
ERD Summary Table:
Table 12 ERD Summary
Entity	Relationships
User	1:N with Camera (Management)
Camera	1:N with Alert
Alert	N:1 with Camera

4.2.3 Data Dictionary
A Data Dictionary defines the structure of the database by listing all the data elements, their types, and constraints.
Table 13 User
Table 4.2.3.1 User

Field Name	Data Type	Description	Constraints
UserID	INT	Unique ID	Primary Key, Auto Increment
Username	VARCHAR	Login Name	NOT NULL, UNIQUE
Password	VARCHAR	Password Hash	NOT NULL
Role	ENUM	Access Level	Default: Viewer
 






Table 14 Camera
Table 4.2.3.2 Camera

Field Name	Data Type	Description	Constraints
CameraID	INT	Unique ID	Primary Key
Name	VARCHAR	Camera Location	NOT NULL
Link	VARCHAR	RTSP URL	NOT NULL
Status	BOOLEAN	Connection State	Default: FALSE

Table 15 Alert
Table 4.2.3.3 Alert

Field Name	Data Type	Description	Constraints
AlertID	INT	Unique ID	Primary Key
CameraID	INT	Source Camera	Foreign Key
Type	VARCHAR	Anomaly Type	NOT NULL
Timestamp	DATETIME	Time of Event	Default: CURRENT_TIMESTAMP











4.3 Class Diagram
Definition:
A Class Diagram is a type of UML diagram that models the classes in a system and their relationships. It is especially useful for object-oriented design in the Python backend.
4.3.1 Main Classes in the System:
4.3.1.1 CameraManager
 Attributes:
•	cameraList: list
•	activeStreams: int
 Methods:
•	addCamera()
•	removeCamera()
•	getStream()
4.3.1.2 AI_Detector
 Attributes:
•	modelPath: string
•	confidenceThreshold: float
 Methods:
•	loadModel()
•	predict(frame)
•	drawBoundingBox()
4.3.1.3 AlertService
 Attributes:
•	alertLog: list
 Methods:
•	createAlert()
•	saveToDB()
•	notifyUser()

 
Figure 11 Class Diagram






4.4 Activity Diagram
Definition:
An Activity Diagram models the workflow of the detection process.
4.4.1 Use Case: "Detect Threat in Live Feed"
 Workflow Steps:
•	Start
•	System Connects to Camera
•	System Grabs Frame
•	Decision Point: Is Frame Valid?
o	No → Retry/Log Error
o	Yes → Send to AI
•	
•	AI Model Processes Frame
•	Decision Point: Is Anomaly Detected?
o	No → Loop to Next Frame
o	Yes → Continue
•	
•	Generate Alert Data
•	Save to Database
•	Update Dashboard
•	Loop to Next Frame
 
Figure 12 Activity Diagram
4.5 Sequence Diagram
Definition:
A Sequence Diagram shows how objects interact over time.
Use Case: Detection and Alerting Flow
Message Flow:
•	Camera → Backend: Streams video data.
•	Backend → AI Engine: Passes frame for inference.
•	AI Engine → Backend: Returns "Weapon Detected" (Confidence 0.95).
•	Backend → Database: Inserts new Alert record.
•	Backend → Web UI: Pushes socket notification.
•	Web UI → User: Displays red warning box.


 
Figure 13 Sequence Diagram






4.6 Collaboration Diagram
Definition:
A Collaboration Diagram emphasizes the structural organization of the objects that send and receive messages.
Objects Involved:
•	CameraSource
•	VideoController
•	YOLO_Model
•	Database
•	DashboardView

 
Figure 14 Collaboration Diagram








4.7 State Transition Diagram
Definition:
Models the different states of the surveillance system.
States:
•	Idle (System on, no cameras).
•	Streaming (Processing video, no threats).
•	Analyzing (AI computation active).
•	Alert State (Threat detected).
•	Error (Camera signal lost).
Transitions:
•	Idle → Add Camera → Streaming.
•	Streaming → Detect Anomaly → Alert State.
•	Alert State → Acknowledge/Time passes → Streaming.
•	Streaming → Signal Loss → Error.

 
Figure 15 State-Chart Diagram
4.8 Component Diagram
Components:
 Frontend Module: Handles UI rendering.
 Stream Handler: Manages RTSP connections.
 Inference Engine: Runs the YOLOv8 model.
 Data Manager: Handles SQL/File storage.
 Notification Service: Manages alerts.


 
Figure 16 Component Diagram







4.9 Deployment Diagram
Nodes:
•	Client PC: Web Browser (Chrome/Edge).
•	Application Server: Hosting Python/Flask & AI Model.
•	Database Server: SQL Storage.
•	CCTV Hardware: IP Cameras on the network.
Connections:
•	C12ameras connect to Server via RTSP.
•	Client connects to Server via HTTP/HTTPS.
•	Server connects to Database via SQL Protocol.

 
Figure 17 Deployment Diagram



