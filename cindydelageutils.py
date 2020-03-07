def sauvegarde(anim):
    anim.save('Animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    
def couleur():
    return 'viridis'

def police():
    return 7
