from NoyesWhitney.py import noyeswhitney
from RungeKutta import rungekutta

# Particle Constants
diffusity = 1
density = 1
diff_layer_thickness = 1
radius = 1
solubility = 1
volume_of_medium = 10
mass_initial = 5
solid_drug = 5

time = np.arange(0, 31, 1)



particles = pd.DataFrame(np.random.normal(5, 0.1, 16), columns=['Particle Size'])
particles_summed = [particles.apply(sum)]

for minute in time:
    new_particles = rungekutta(noyes_whitney, time, particles)
    particles_summed.append(new_particles.apply(sum))
    particles = new_particles
    

summed_particles = pd.DataFrame(particles_summed)
plt.plot(summed_particles)
