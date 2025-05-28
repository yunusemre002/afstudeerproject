import numpy as np
import napari

# 3D maskeleri yükle
nuclei_masks_3d = np.load("/Users/demir/Downloads/nuclei_masks_3d.npy")
cellbody_masks_3d = np.load("/Users/demir/Downloads/cellbody_masks_3d.npy")

# Napari viewer başlat
viewer = napari.Viewer()

# 3D maskeleri volumetrik olarak ekle
viewer.add_labels(nuclei_masks_3d, name='Nuclei Masks')
viewer.add_labels(cellbody_masks_3d, name='Cellbody Masks')

napari.run()