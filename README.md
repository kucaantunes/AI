# AI

Use of AI for Vital Signs detection and image uploader

Body temperature:

![image](https://user-images.githubusercontent.com/26171557/187051252-ff50c380-c97f-44b4-aa50-6deffb193d83.png)


Breath Rate:

![image](https://user-images.githubusercontent.com/26171557/187051279-0c54354f-60e8-43ad-b049-5f2dccd4321f.png)

![image](https://user-images.githubusercontent.com/26171557/187051282-69b244e1-afc0-47b5-80ee-daac51ef0f11.png)



Blood Pressure:

![image](https://user-images.githubusercontent.com/26171557/187051266-8f75ed75-4a65-4216-9451-c4ee192f4e0a.png)



Oximetry:

![image](https://user-images.githubusercontent.com/26171557/187051291-29793c2a-c1e0-4d85-8e7a-3dde39b8200b.png)

![image](https://user-images.githubusercontent.com/26171557/187051293-fc61687d-8692-4489-95cf-615ec9c20328.png)

![image](https://user-images.githubusercontent.com/26171557/187051299-4b53f33c-5c22-42d7-9e80-81be9bcfc81b.png)


Heart rate:

![image](https://user-images.githubusercontent.com/26171557/187051315-2fb6dd35-c72e-41ee-9c85-ee0abb947cfa.png)


![image](https://user-images.githubusercontent.com/26171557/187051317-099ac757-8abf-4097-80d9-89d02c51f1ca.png)


Concerning Primary Care activities and to improve the current online consultation process, this dissertation presents a prototype based on obtaining the vital signs during consultation for the physician and also access to the patient history aiming to facilitate the process of detecting possible diseases and triggering the emergency procedure based on the country where the user is placed without physical contact avoiding also the contagion of the Covid-19 disease.
Currently it is possible to obtain the exact value of the vital signs: for blood pressure through the sphygmomanometer which also records the heart rate, concerning body temperature the actual values can be obtained with the thermometer; for the oxygen in the blood the correct values can be measured by an oximeter and heart rate can be obtained by different devices like the oximeters that also read this value, as do some sport watches and sphygmomanometers (blood pressure devices); Heart rate can also be assessed on arterial pulses (example given: on wrist and neck).
       
Figure 61. Data for a specific patient.

Whenever the program detects values above or below those recorded as a reference, an emergency procedure should be triggered and the user can communicate the problem to the attending physician or the professional who will assist him.
The patient should have information about the signs and symptoms that require urgent/emergent medical intervention, and, if possible, help from third parties, even if the parameter measurements are in the range considered normal in the program. Some examples are some types of chest pain (thoracic pain), sudden miss of air, signs of rapidly worsening breathlessness, deviation of the labial commissure, lack of strength in one of the limbs, among others (some possible emergency situations are chest pain, feeling faint, dizziness, shortness of breath and lack of strength). The vital signs allow doctors to understand the health state of a patient and determine the severity level.

4.4	Body Temperature
Body temperature refers to the production of heat in the body and the mechanisms for its regulation and maintenance, essential to maintain systemic homeostasis (stability that the body needs to perform its functions properly). The usage of OpenCV and Python allows to get the temperature values via web camera. The program requires the installation of OpenCV libraries. Two applications were developed to get the temperature via web camera, one in Python and the other in Matlab.
      
Figure 62. Obtaining body temperature via Python and Matlab. Adapted from the code [65].
4.5	Blood Pressure
Blood pressure or blood tension is the force that the blood exerts on the walls of the arteries during its circulation, and results in two measures:
• Systolic blood pressure or “maximum” blood pressure: appears first and measures the force with which the heart contracts and “expels” the blood from its interior.
• Diastolic blood pressure or “minimum” blood pressure: this is the second value and concerns the measurement of pressure when the heart relaxes between each beat.
The reading of blood pressure is usually measured in millimeters of mercury (mmHg). When blood pressure is normal, it allows blood to be distributed throughout the body, reaching all organs. If the blood pressure is chronically high (hypertension) or when it increases suddenly, it has negative consequences for health, being responsible, for example, for cerebrovascular accidents, cardiac infarctions (death of heart cells), among other possibilities. For cases where blood pressure is too low (hypotension) blood flow on cells can decrease, compromising the nutrition and oxygenation of the cells, including brain cells. A mobile application was developed in java to obtain this value using the camera of the phone and by detecting the face of the user.
     
Figure 63. Application developed in Java for mobile and a Pulse Blood Pressure Monitor.

4.6	Cardiac Frequency
The cardiac frequency rate is the number of times your heart beats per minute. Changes in heart rate may indicate the existence of cardiac and non-cardiac pathologies and may compromise the nutrition and oxygenation of the cells, including the brain cells; in order to measure the heartbeats during gameplay we have developed an application that measures the cardiac frequency in real time with the use of Python that is base in computer vision. Appearing on the monitor the reading obtained. The results from the webcam detection were compared and tested with the ones provided by medical devices and the clock sensor.
  
Figure 64. Heartbeat detection and comparison.
By analyzing the python code, we can see that the values obtained by the green channel allowed to determine the heart frequency.
The information provided will facilitate a clinical analysis. During the gameplay the application will track the face of the player first and afterwards will report the heartbeat in real time. The picture below is the heartbeat measurement on a web application with the use of OpenCV.
   
Figure 65. Different processes for heartbeat detection and usage of a serious game to get the state of rest to perform the analysis.
Pulse measurement of the fingerprints is one of the several functionalities of AI Care being a bit related with the heartbeat detection project. It is calculating also the number of heart beatings but instead of measuring above chest, it is measuring the pulse from the fingerprint. In case the readings are too different from these two places, the patient most likely is facing a situation of cardiac arrhythmia and should see his doctor.
The application should have an alarm system that triggers a contact to the correspondent medical institution according with the national emergency system of the country in case. The user has to place his finger on the phone camera for a few seconds and check if the light is on. The measurement process is different from the one used in the heartbeat via webcam. After getting the reading, the user can press a button on the mobile Java application that will send the information to the AI Care web application, that will add this value to his profile, store in the database and report on the system the readings obtained every time the clinical record is checked.
The technologies used for the mobile application were Java, Android Studio and APIs and concerning the web application was used PHP, MySQL and JavaScript mainly.
A website was developed to obtain the information obtained from the mobile phone using the open source PubNub API, allowing the verification of the data obtained by the mobile phone. The website shown in the figure above was made with HTML, JavaScript and CSS languages, using an API that allows the passage of information between the phone and the website. The developed mobile application in java reads the heartbeat via the phone and sends the information obtained to the website.
   
   
Figure 66. Detection of heartbeats via finger (light required for reading) and the web application.
4.7	Oximetry
The Oximetry is a test that lets you know how much oxygen is being carried in the blood. The oxygen level measured with an oximeter is called the oxygen saturation level (SaO2). SaO2 is the percentage of oxygen that blood carries (in red blood cells) compared to its maximum carrying capacity on arteries. The lack of oxygen in the blood reduces its supply to the cells  and may be inadequate for its needs, a condition that can cause serious cell damage and even lead to death. The SPO2 percentage was obtained with MatLab. To perform this test, it is required appropriate lightning and placing the thumb close to the web cam.
The formula used to calculate the SpO2 can be based in the AC and DC of the blue and green channel [61].
(10)
   
Figure 67. Obtaining the percentage of oxygen on the blood arteries.

4.8	Respiratory Frequency
The respiratory rate is the number of breaths per minute, that is, the number of times the combination of inspiration (entry of air into the lungs) and exhalation (exit of air from the lungs) occurs in one minute. The respiratory rate can be evaluated by counting only the number of inspirations per minute, by observing the chest expansion at each inspiration, that is, by counting how many times the chest goes up.
The respiratory rate can be obtained by counting the number of breaths during one minute, for a more accurate result your body should be at rest as in example, it is better measured if you are in a sitting position or laid down in bed. The breath rate can be obtained by counting the number of pikes, maximum in the heart rate, every time the heart rate gets a maximum means you have inhaled, showing the number of breads per minute. On the plot it is possible to identify low frequency waveforms mixed with high frequency sawtooth (small spikes). Each small peak corresponds to a pulse beat (heartbeat). And the great peak-valley transition corresponds to the respiratory cycles.
  
Figure 68. Breath rate detection and comparison
The reference values considered in the Program for respiratory rate are: 12 to 18 breaths per minute. The developed prototype allows in the final presented solution to obtain this value using the Infra-Red (IR) sensor which can be a web cam and the exact value of the number of breaths in one minute is stored on the MySQL database.
  
Figure 69. Obtaining the breath rate and adding to the clinical record of the patient. Adjusted from the code [66].


