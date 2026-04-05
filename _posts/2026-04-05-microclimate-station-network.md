---
title: "Microclimate Station Network for Salinity Monitoring"
date: 2026-04-05 08:25:00 +0700
categories: [Projects, AIoT]
tags: [lora, aiot, machine-learning, mobile-app, hardware]
image:
  path: /assets/img/projects/microclimate/page18_img4.jpeg
---

## Project Overview

Vietnam is one of the world's leading rice exporters, heavily relying on freshwater resources which account for 82% of total irrigation. However, climate change and rising sea levels have drastically increased **salinity intrusion**, severely impacting agricultural production in coastal regions. 

To tackle this problem, I designed and built the **Microclimate Station Network**—an end-to-end AIoT (Artificial Intelligence of Things) system aimed at monitoring and predicting salinity levels to support the agricultural sector. 

## My Role

For this comprehensive system, **I solely architected and developed the entire ecosystem from scratch**. My work traversed every layer of the technology stack, encompassing custom hardware design, firmware programming, AI model training, backend API deployment, and mobile app development.

![Installation](/assets/img/projects/microclimate/page18_img1.jpeg)

## System Architecture

### 1. Hardware: Nodes and Gateway
The network topology consists of multiple sensor nodes communicating with a central gateway via **LoRa**.
- **Sensor Nodes**: Custom-built boards equipped with various sensors to collect environmental data, specifically targeting salinity, temperature, humidity, and water levels.
- **LoRa Mesh**: The nodes feature LoRa wireless communication modules that allow them to network with nearby stations, relaying data securely.
- **Gateway**: The gateway node acts as the master, receiving payload data from the LoRa nodes and utilizing a 4G SIM module (or Wi-Fi) to push the information securely to a remote server.

![Node Design](/assets/img/projects/microclimate/page12_img2.png)

### 2. Artificial Intelligence (AI)
Collecting data is only half the battle. To provide actionable intelligence:
- I designed a predictive Machine Learning model focused on time-series forecasting to predict future salinity levels.
- The model utilizes the **Sliding Window Method** to leverage historical data sequences for near-future prediction.
- I underwent the entire pipeline: from data preprocessing and initial model drafting to hyperparameter tuning and final evaluation.

![AI Diagram](/assets/img/projects/microclimate/page16_img1.png)

### 3. Software: Server, API, and Mobile App
An ecosystem is only useful if the end-user can interact with it effortlessly.
- **Backend**: Deployed server-side infrastructure initially leveraging ThingSpeak to aggregate gateway data.
- **API Development**: Built robust APIs to serve data to the frontend effortlessly.
- **Mobile Application**: Developed a mobile app allowing users to monitor real-time sensor metrics and access the AI's predictive insights on future salinity levels. The app also features a secure user authentication system.

![Mobile App Preview](/assets/img/projects/microclimate/page21_img1.png)

## Evaluation and Limitations

The prototype system operates highly stably. The LoRa transmission between the nodes and gateway is reliable, and data efficiently syncs with the application.

However, as an independent project, there are areas I have identified for future iteration:
* **Calibration**: Currently lacking the budget for high-end commercial measuring devices to act as ground-truth for absolute sensor calibration.
* **Infrastructure**: Moving away from the free-tier limitations of ThingSpeak to a fully custom-hosted backend and AI server structure.
* **Power Optimization**: The current power footprint limits the battery lifespan in non-ideal conditions to just a few days. Implementing deep-sleep cycles and refined power management is the next priority.

Building the **Microclimate Station Network** was an incredible journey that allowed me to push my boundaries across hardware, software, and AI.
