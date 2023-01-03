# Smart Agriculture system based on IoT

This is a system that enables farmers to monitor and control their farms with a web-based application built with Node-RED. It uses the IBM IoT Watson cloud platform as its backend.

## Description

  * Smart Agriculture System based on IoT can monitor soil moisture and climatic conditions to grow and yield a good crop.
  
  * The farmer can also get the realtime weather forecasting data by using external platforms like Open Weather API.
  
  * Farmer is provided a mobile app using which he can monitor the temperature, humidity and soil moisture parameters along with weather forecasting details.
  
  * Based on all the parameters he can water his crop by controlling the motors using the mobile application.
  
  * Even if the farmer is not present near his crop he can water his crop by controlling the motors using the mobile application from anywhere.
  
  * Here we are using the Online IoT simulator for getting the Temperature, Humidity and Soil Moisture values.

## Simulator

The data of the farm like soil moisture, humidity and temperature are collected from sensors and then need to be sent to cloud
but here I am using a simulator in which we are going to connect it to the IBM cloud account and send data to cloud.



## Web App User Interface

Web App is created using NodeRed.

There are two tabs in this Web App :

###  1.Home tab

   This tab contains measured and online weather forecast data displayed in guages.
  
   
   
###  2.Controls tab

   This tab contains the controls of motor to switch it on, off and also a button to specify motor to run for 30 minutes continuosly.
   
   
## NodeRed Program Flow

This is the program flow of the web app created using NodeRed. 


