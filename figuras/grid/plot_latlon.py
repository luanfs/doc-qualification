####################################################################################
# 
# Module for plotting routines.
#
# Luan da Fonseca Santos - January 2022
# (luan.santos@usp.br)
####################################################################################

import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt

####################################################################################
# This routine plots the latlon grid.
####################################################################################
fig_format = 'png' # Figure format
def plot_grid(map_projection, N, M):
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
  
   lon = np.linspace(-180.0, 180.0, N+1)
   lat = np.linspace( -90.0, 90.0, M+1)  
   #lat, lon = np.meshgrid(lat, lon)
   
   for i in range(0, N):
       for j in range(0, M):
       #    print(i,j,N)
           # Plot vertices
           A_lon, A_lat = lon[i],   lat[j]
           B_lon, B_lat = lon[i+1], lat[j]
           C_lon, C_lat = lon[i+1], lat[j+1]
           D_lon, D_lat = lon[i],   lat[j+1]

           plt.plot([A_lon, B_lon], [A_lat, B_lat],linewidth=1, color='blue', transform=ccrs.Geodetic())
           plt.plot([B_lon, C_lon], [B_lat, C_lat],linewidth=1, color='blue', transform=ccrs.Geodetic())
           plt.plot([C_lon, D_lon], [C_lat, D_lat],linewidth=1, color='blue', transform=ccrs.Geodetic())
           plt.plot([D_lon, A_lon], [D_lat, A_lat],linewidth=1, color='blue', transform=ccrs.Geodetic())
 
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
   plt.savefig("latlon_"+map_projection+'.'+fig_format, format=fig_format)
   print('Figure has been saved in latlon_'+map_projection+'.'+fig_format)
   print("--------------------------------------------------------\n")    
   plt.close()

map_projection = "mercator"
M = 30
N = 2*M
plot_grid(map_projection, N, M)

