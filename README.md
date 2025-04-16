# Thermal Flux Simulation on a 10 cm Cube Satellite

This project simulates the thermal environment of a 10 cm aluminum cube satellite in low Earth orbit. It calculates the solar direct flux, Earth albedo, and infrared radiation received by the satellite on March 20, considering orbital eclipse conditions.

## 🛰️ Orbit Parameters

- Type: Sun-synchronous orbit (SSO)
- Inclination: 97.86°
- Altitude: ~630 km
- Period: ~98.7 minutes
- Shape: Near-circular (eccentricity ≈ 0)

## 🔥 Thermal Inputs

- Direct solar irradiance: 1361 W/m²  
- Albedo coefficient: 0.3  
- Earth IR flux: 237 W/m²  
- Emissivity: 1.0  
- Eclipse detection included

## 🛠️ Technologies Used

- Python 3  
- [Skyfield](https://rhodesmill.org/skyfield/)  
- NumPy  
- Matplotlib

## 📈 Outputs

The script generates three plots:
1. Direct solar flux over time
2. Albedo flux over time
3. Earth IR flux over time

All fluxes are expressed in W/m² along the satellite's nadir-facing surface.

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install skyfield numpy matplotlib


   ![Captura de pantalla](IRRADIANCIA IR.JPEG)
