import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import os
os.environ["PROJ_LIB"] = "C:\ProgramData\Anaconda3\envs\TEST\Library\share"
from mpl_toolkits.basemap import Basemap


dtoscnjs=Dataset('CMSFluxMISC_v1.nc4','r')
Cs=dtoscnjs.variables['ChemicalSources'][:]
lat=dtoscnjs.variables['lat'][:]
lon=dtoscnjs.variables['lon'][:]
for i in range(47):
    var=Cs[0][i][:][:]
    dpi = 100
    fig = plt.figure(figsize=(1100/dpi, 1100/dpi), dpi=dpi)
    ax  = fig.add_axes([0.1,0.1,0.8,0.9])

    #-- create map
    map = Basemap(projection='cyl',llcrnrlat= -90.,urcrnrlat= 90.,\
              resolution='c',  llcrnrlon=-180.,urcrnrlon=180.)

    #-- draw coastlines, state and country boundaries, edge of map
    map.drawcoastlines()
    map.drawstates()
    map.drawcountries()

    #-- create and draw meridians and parallels grid lines
    map.drawparallels(np.arange( -90., 90.,30.),labels=[1,0,0,0],fontsize=10)
    map.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1],fontsize=10)

#-- convert latitude/longitude values to plot x/y values
    x, y = map(*np.meshgrid(lon,lat))

#-- contour levels
    clevs = np.linspace(0,0.00000025,10)

#-- draw filled contours
    cnplot = map.contourf(x,y,var,clevs,cmap=plt.cm.jet)

#-- add colorbar
    cbar = map.colorbar(cnplot,location='bottom',pad="10%")      #-- pad: distance between map and colorbar
    cbar.set_label('kg/s*km2')                                      #-- add colorbar title string

#-- add plot title
    plt.title('Fuentes quimicas nivel'+str(i))

#-- displa on screen
    #plt.show()

#-- maximize and save PNG file
    plt.savefig('img'+str(i)+'.png', bbox_inches='tight', dpi=dpi)
    
    

#for i in range(12):
#    for x1 in range(47):
#        y1=Cs[i][x1][0][0]
#        plt.plot(x1, y1, 'o-')
#        plt.title('Basura en: '+str(i))
#        plt.xlabel('Nivel')
#        plt.ylabel('Sedimento')
#    plt.show()
#datos_prueba=Cs[1][0][4][12]
#print(datos_train.shape)
#model = keras.Sequential([
#    keras.layers.Flatten(input_shape=(46, 72)),
#    keras.layers.Dense(331, activation='relu'),
#    keras.layers.Dense(3, activation='softmax')
#])
#model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#model.fit(datos_train,epochs=10)

              