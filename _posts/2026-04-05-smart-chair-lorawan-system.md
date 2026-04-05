---
title: "Smart Chair: LoRaWAN Beach Chair Management System"
date: 2026-04-05 09:05:00 +0700
categories: [Projects, Hardware]
tags: [lorawan, hardware, firmware-test, rak3172, ultra-low-power, e-ink]
image:
  path: /assets/img/projects/smart_chair/image.png
---

## Project Overview

Welcome to the **Smart Chair** project! This is a dedicated hardware engineering project implementing a beach chair management system utilizing the **LoRaWAN** protocol. 

The system provides a seamless experience, allowing users to remotely reserve beach chairs and pay for rentals for a specified period. The ecosystem incorporates a central Gateway device communicating with distributed Chair Kits.

## My Role & Contributions

In this system, I was contracted exclusively for **Hardware Design & Embedded Firmware Testing**. This was a collaborative product, and my responsibilities were strictly defined to ensure the underlying electronics functioned flawlessly before the overall system integration phase. 

*I did not handle the high-level system software; my work was exclusively the foundational hardware layer.*

![PCB Hardware Overview](/assets/img/projects/smart_chair/image.png)

### 1. Hardware Design
- Designed the core electronics for the Chair Kits based on the **RAK3172** LoRa module.
- Engineered a rigorous **Ultra-Low Power** architecture, breaking the incredibly challenging threshold of consuming **under 5uA** while in sleep mode. This ensures the chairs can remain deployed on the beach layout for entire seasons without battery replacement.
- Integrated multiple modular peripherals including an **E-ink Display**, **IMU** (Inertial Measurement Unit), and **GPS** for location tracking.

### 2. Embedded Firmware Testing & Bring-Up
- Developed and executed extensive low-level test firmware to validate the **E-ink Display** drivers, ensuring crisp rendering even in direct sunlight.
- Configured and thoroughly tested the **IMU** for theft and movement detection logic.
- Tested the precision of the **GPS** for accurate geofencing capabilities.
- Performed holistic block-by-block testing across the board, ensuring the RAK3172 LoRaWAN payload logic and peripheral power sequences operated flawlessly under the ultra-low-power constraints.

![Hardware and Assembly detail](/assets/img/projects/smart_chair/image1.png)

## Technical Specifications

- **Communication**: LoRaWAN (RAK3172 Module)
- **Power Consumption**: Ultra Low Power ( < 5uA )
- **Display**: E-ink Display (Sunlight readable)
- **Sensors**: IMU (Movement tracking), GPS (Location monitoring)
- **System Devices**: Gateway Device & Distributed Chair Kits

By isolating the hardware design and block-level firmware validation, I handed off a bulletproof, highly power-efficient physical board for the software integration teams to confidently build their payment and reservation system upon.
