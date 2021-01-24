# Suggested constants

diffusity = 1
density = 1
diff_layer_thickness = 1
radius = 1
solubility = 1
volume_of_medium = 10

def noyes_whitney(time, solid_drug):
    '''
    A differential of the dissolution of drug particles in a medium.
    Returns the change in mass of solid drug. This gradient is negative as the solid drug decreases.
    '''
    
    dissolved_drug = mass_initial - solid_drug
    
    top = 3 * diffusity * mass_initial**(1/3) * solid_drug**(2/3)
    bottom = density * diff_layer_thickness * radius
    gradient = solubility - (dissolved_drug/volume_of_medium)
    
    return -(top/bottom) * gradient
