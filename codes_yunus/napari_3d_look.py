import numpy as np
from cellpose import io 
from skimage import morphology
from scipy.ndimage import label
import napari

# --------------
# FILE IMPORT

file_path = "/Users/demir/Documents/Hva_AI/afstudeerproject/E35_tif/20240312_CKR_Exp35_STHdhQ97HA_96h_+BafA_CCT1_635P_HA_580_A11_460L_2.tif"
img = io.imread(file_path) # (9, 4, 1024, 1024)
print(f'img       : {img.shape}')

img_nuclei = img[:, 0, :, :]
img_aggregate = img[:, 2, :, :]
img_cellbody = img[:, 3, :, :]

print(f'Nuclei    : {img_nuclei.shape} \nAggregate : {img_aggregate.shape} \nCell body : {img_cellbody.shape}')


# -----------------------
# THRESHOLD for AGGREGATE

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
labeled_aggregates, num_aggregates = label(aggregate_stack)


# -----------------------
# NUCLEI







# -------------------
# NAPARI 3D 

# viewer = napari.Viewer(ndisplay=3)  # 3D gösterim için
# viewer.add_image(img_nuclei, name="Nucleus", colormap="blue", scale=(1, 1, 1))
# viewer.add_image(img_cellbody, name="Cell Body", colormap="gray", blending="additive", scale=(1, 1, 1))
# viewer.add_labels(labeled_aggregates, name="Aggregates", opacity=0.6, scale=(1, 1, 1))
# napari.run()


# -------------------
# NAPARI 3D 

from skimage.measure import regionprops

# Kullanıcıya bağlı olarak gösterilsin mi?
show_labels = True  # ← bunu False yaparsan numaralar gösterilmez

# Labeled aggregateler üzerinden centroid'leri bul
regions = regionprops(labeled_aggregates)
points = []
labels = []

for region in regions:
    z, y, x = region.centroid
    points.append([z, y, x])
    labels.append(str(region.label))

points = np.array(points)

# Napari 3D görüntüleme
viewer = napari.Viewer(ndisplay=3)
viewer.add_image(img_nuclei, name="Nucleus", colormap="blue", scale=(1, 1, 1))
viewer.add_image(img_cellbody, name="Cell Body", colormap="gray", blending="additive", scale=(1, 1, 1))
viewer.add_labels(labeled_aggregates, name="Aggregates", opacity=0.9, scale=(1, 1, 1))

# Eğer kullanıcı isterse agregat ID'leri göster
if show_labels:
    viewer.add_points(points, name='Aggregate IDs', size=3, face_color='red', text=labels, scale=(1, 1, 1))

napari.run()
