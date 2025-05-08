import numpy as np
from cellpose import models, core, io, plot
from pathlib import Path
from tqdm import trange
import matplotlib.pyplot as plt
from natsort import natsorted
from skimage import measure, morphology

file_name = f"/Users/demir/Documents/Hva_AI/afstudeerproject/codes_yunus/input/tif_deneme_1.tif"
img = io.imread(file_name) # (9, 4, 1024, 1024)
print(f'img       : {img.shape}')

# NUCLEI
img_nuclei = img[:, 0, :, :]
# img_nuclei = img_nuclei[6, :, :]
print(f'Nuclei    : {img_nuclei.shape}')

# NUCLEI
img_aggregate = img[:, 2, :, :]
# img_aggregate = img_aggregate[6, :, :]
print(f'Aggregate : {img_aggregate.shape}')

# CELL BODY
img_cellbody = img[:, 3, :, :]
# img_cellbody = img_cellbody[6, :, :]
print(f'Cell body : {img_cellbody.shape}')

# Process aggregates (Channel 2)
def process_aggregates(img):
    aggregate_masks = []
    for z_slice in range(img.shape[0]):
        slice_img = img[z_slice, 2, :, :]  # Channel 2 for aggregates
        threshold = 0.6 * np.max(slice_img)
        bright_spots = slice_img > threshold
        clean_mask = morphology.remove_small_objects(bright_spots, min_size=10)
        aggregate_masks.append(clean_mask)
    return aggregate_masks

aggregate_masks = process_aggregates(img)

aggregate_stack = np.stack(aggregate_masks, axis=0)  # shape: (Z, Y, X)


from scipy.ndimage import label
labeled_aggregates, num_aggregates = label(aggregate_stack)


from skimage.measure import regionprops

props = regionprops(labeled_aggregates)

for i, region in enumerate(props):
    print(f"Agregat {i+1}:")
    print("  - Voxel sayısı (hacim):", region.area)
    print("  - Ağırlık merkezi:", region.centroid)

total_aggregates = len(props)
total_volume = sum([r.area for r in props])
average_volume = total_volume / total_aggregates if total_aggregates > 0 else 0

import pandas as pd

# df = pd.DataFrame([{
#     'id': i+1,
#     'volume': r.area,
#     'centroid_z': r.centroid[0],
#     'centroid_y': r.centroid[1],
#     'centroid_x': r.centroid[2]
# } for i, r in enumerate(props)])

# df.to_csv("aggregates_summary.csv", index=False)


import matplotlib.pyplot as plt
from skimage.measure import label
import napari
import numpy as np

from scipy.ndimage import label

import napari
import numpy as np
from scipy.ndimage import label

# Z, C, Y, X boyutundaki img üzerinden çalışıyoruz

# Kanal 0: Nucleus (çekirdek), Kanal 1/3: Hücre, Kanal 2: Agregat
nucleus = img[:, 0, :, :]
cell_body = img[:, 3, :, :]  # ya da 1

file_name_masked = f"/Users/demir/Documents/Hva_AI/afstudeerproject/codes_yunus/masksed_Cell.tif"
img_masked = io.imread(file_name_masked)  # (Z, C, Y, X)
print(f'img_masked       : {img_masked.shape}')


aggregate_stack = np.stack(aggregate_masks, axis=0)
labeled_aggregates, num_aggregates = label(aggregate_stack)

# Napari ile 3D görselleştirme
viewer = napari.Viewer(ndisplay=3)  # 3D gösterim için
# viewer.add_image(nucleus, name="Nucleus", colormap="gray", blending="additive", scale=(1, 1, 1))
viewer.add_image(nucleus, name="Nucleus", colormap="gray", scale=(1, 1, 1))
viewer.add_image(cell_body, name="Cell Body", colormap="green", blending="additive", scale=(1, 1, 1))
viewer.add_labels(labeled_aggregates, name="Aggregates", opacity=0.6, scale=(1, 1, 1))

napari.run()

# # Napari ile görselleştir
# viewer = napari.Viewer()
# viewer.add_image(nucleus, name="Nucleus", colormap="gray", blending="additive")
# viewer.add_image(cell_body, name="Cell Body", colormap="green", blending="additive")
# viewer.add_labels(labeled_aggregates, name="Aggregates", opacity=0.6)
# napari.run()
