from skyfield.api import load, EarthSatellite
import numpy as np
import matplotlib.pyplot as plt

# Cargar efemérides
ts = load.timescale()
eph = load('de421.bsp')
earth = eph['earth']
sun = eph['sun']

# TLE simulado SAOCOM
line1 = '1 99999U 24001A   25080.25000000  .00000000  00000-0  00000-0 0  9990'
line2 = '2 99999  97.8600  0.0000 0001000 000.0000 000.0000 14.57100000    01'
sat = EarthSatellite(line1, line2, 'SAOCOM', ts)

# Constantes
R_earth_km = 6371.0
S0 = 1361
albedo_coeff = 0.3
ir_flux = 237
epsilon = 1.0

# Nueva función para detectar eclipse (ángulo Sol–Tierra–Satélite)
def en_eclipse(pos_s, pos_sat):
    vec_s = pos_s / np.linalg.norm(pos_s)
    vec_sat = pos_sat / np.linalg.norm(pos_sat)
    cos_theta = np.dot(vec_s, vec_sat)
    theta = np.arccos(cos_theta)
    angle_umbra = np.arcsin(R_earth_km / np.linalg.norm(pos_sat))
    return theta < angle_umbra

# Día: 20 de marzo
times = ts.utc(2025, 3, 20, 0, np.linspace(0, 100, 100))
flux_dir, flux_alb, flux_ir = [], [], []

for t in times:
    obs = sat.at(t)
    pos_sat = obs.position.km
    vel_sat = obs.velocity.km_per_s
    pos_s = earth.at(t).observe(sun).position.km

    r_unit = pos_sat / np.linalg.norm(pos_sat)
    v_unit = vel_sat / np.linalg.norm(vel_sat)
    s_unit = pos_s / np.linalg.norm(pos_s)

    z_nadir = -r_unit
    x_orb = v_unit
    y_lat = np.cross(z_nadir, x_orb)

    sun_visible = not en_eclipse(pos_s, pos_sat)

    ft = S0 * max(0, np.dot(s_unit, z_nadir)) if sun_visible else 0
    flux_dir.append(ft)

    fa = S0 * albedo_coeff * max(0, np.dot(z_nadir, -r_unit)) if sun_visible else 0
    flux_alb.append(fa)

    fir = epsilon * ir_flux * max(0, np.dot(z_nadir, -r_unit))
    flux_ir.append(fir)

# Minutos
minutos = np.linspace(0, 100, 100)

# Gráfico 1: Solar directo
plt.figure(figsize=(10, 4))
plt.plot(minutos, flux_dir, color='gold')
plt.xlabel("Minutos desde inicio de órbita")
plt.ylabel("Irradiancia solar directa (W/m²)")
plt.title("Irradiancia solar directa - 20 de marzo (modelo corregido)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Albedo
plt.figure(figsize=(10, 4))
plt.plot(minutos, flux_alb, color='skyblue')
plt.xlabel("Minutos desde inicio de órbita")
plt.ylabel("Irradiancia por albedo (W/m²)")
plt.title("Irradiancia por albedo - 20 de marzo (modelo corregido)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3: Infrarrojo terrestre
plt.figure(figsize=(10, 4))
plt.plot(minutos, flux_ir, color='red')
plt.xlabel("Minutos desde inicio de órbita")
plt.ylabel("Irradiancia IR terrestre (W/m²)")
plt.title("Irradiancia IR terrestre - 20 de marzo")
plt.grid(True)
plt.tight_layout()
plt.show()
