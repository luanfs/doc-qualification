####################################################################################
# 
# Plotting routines.
#
# Luan da Fonseca Santos - July 2022
# (luan.santos@usp.br)
####################################################################################

import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt

####################################################################################
# This routine plots the icos grid.
####################################################################################
fig_format = 'png' # Figure format
def plot_grid(map_projection, lats, lons, N, name):
   # Figure resolution
   dpi = 100

   print("--------------------------------------------------------")
   print('Plotting latlon grid using '+map_projection+' projection...')   
   if map_projection == "mercator":
      plateCr = ccrs.PlateCarree()
      plt.figure(figsize=(1832/dpi, 977/dpi), dpi=dpi)
   elif map_projection == 'sphere':
      plateCr = ccrs.Orthographic(central_longitude=-60.0, central_latitude=40.0)   
      plt.figure(figsize=(800/dpi, 800/dpi), dpi=dpi)
   else:
      print('ERROR: Invalid map projection.')
      exit()

   plateCr._threshold = plateCr._threshold/10.
   ax = plt.axes(projection=plateCr)
   ax.stock_img()
   
   #for i in range(0, N-2):
   for i in range(0, N, 2):
       # Plot vertices
       A_lon, A_lat = lons[i],   lats[i]
       B_lon, B_lat = lons[i+1], lats[i+1]       
       plt.plot([A_lon, B_lon], [A_lat, B_lat],linewidth=1, color='blue', transform=ccrs.Geodetic())
   #plt.show()
      # Plot centers
      #if map_projection == 'mercator':
      #   center_lon, center_lat = lonc, latc
      #   center_lon, center_lat = np.ndarray.flatten(center_lon),np.ndarray.flatten(center_lat)
      #   print(np.shape(center_lon))
      #   plt.plot(center_lon, center_lat, marker='+',color = 'black')

   if map_projection == 'mercator':
      ax.gridlines(draw_labels=True)
      
   # Save the figure
   #plt.show()
   plt.savefig(name+map_projection+'.'+fig_format, format=fig_format)
   print('Figure has been saved in latlon_'+map_projection+'.'+fig_format)
   print("--------------------------------------------------------\n")    
   plt.close()
   
####################################################################################
# Convert from cartesian (x,y,z) to spherical coordinates (lat,lon)
# on the unit sphere.
# Outputs: latitude (ϕ), longitude (λ)
####################################################################################
def cart2sph(x, y, z):
   hypotxy = np.hypot(x, y)
   ϕ = np.arctan2(z, hypotxy)
   λ = np.arctan2(y, x)
   return λ, ϕ

#map_projection = "sphere"
map_projection = "mercator"
#name = "icos_pol_nopt_3_ed"
#name = "icos_pol_nopt_3_edhx"
name = "octg_pol_nopt_4_ed"
icos_ll = np.loadtxt(name+".gmt")	
lons = icos_ll[:,0]
lats = icos_ll[:,1]
N = len(lats)
plot_grid(map_projection, lats, lons, N, name)


