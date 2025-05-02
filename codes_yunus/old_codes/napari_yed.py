import matplotlib.pyplot as plt
import numpy as np
from skimage import filters, morphology
from aicsimageio import AICSImage
file_name = f"/Users/demir/Documents/Hva_AI/afstudeerproject/Images Carolina/20240312_CKR_Exp35_STHdhQ97HA_96h_+BafA_CCT1_635P_HA_580_A11_460L_4.lif"

# img = AICSImage(file_name)
# c2 = img.get_image_data("CZYX", T=0, C=2)  # Assuming channel 2 is C2


# if c2.ndim == 4:
#     c2 = np.squeeze(c2)  # otomatik olarak boyutu düşürür
#     print("c2.shape:", c2.shape)

# # Normalize and threshold
# normalized = (c2 - c2.min()) / (c2.max() - c2.min())
# threshold = filters.threshold_otsu(normalized)
# binary = normalized > threshold

# # Clean
# binary = morphology.remove_small_objects(binary, min_size=50)


# from skimage.measure import label, regionprops_table
# import pandas as pd

# labeled = label(binary)
# props = regionprops_table(
#     labeled, intensity_image=c2,
#     properties=['label', 'area', 'centroid', 'mean_intensity', 'bbox']
# )

# df = pd.DataFrame(props)
# df["volume_voxels"] = df["area"]


# c1 = img.get_image_data("CZYX", T=0, C=1)
# c1 = np.squeeze(c1)
# from scipy.stats import pearsonr

# # Flatten both channels
# mask = (binary > 0)
# pearson_corr = pearsonr(c1[mask].flatten(), c2[mask].flatten())[0]

# print(f"Pearson correlation in colocalized region: {pearson_corr:.3f}")

# import napari

# viewer = napari.Viewer()

# viewer.add_image(c2, name="C2 - Aggregates")
# viewer.add_labels(labeled, name="Aggregates")
# viewer.add_image(c1, name="C1 - Other Channel")  # optional
# napari.run()  # GUI kontrolü biter, kullanıcı kapatınca devam eder

# --------------------
import numpy as np
# from aicsimageio import AICSImage
# import napari

# # Dosya yolu
# img = AICSImage(file_name)

# # Tüm kanalları çek (C, Z, Y, X)
# data = img.get_image_data("CZYX", T=0)

# print("Tüm görüntü şekli (C, Z, Y, X):", data.shape)

# # Napari ile tüm kanalları görselleştir
# viewer = napari.Viewer()

# channel_names = ["C0 - Nucleus", "C1 - A11", "C2 - HA", "C3 - CCT1"]

# for c in range(data.shape[0]):
#     viewer.add_image(data[c], name=channel_names[c] if c < len(channel_names) else f"Channel {c}")

# napari.run()


# ====

from aicsimageio import AICSImage
import napari


img = AICSImage(file_name)

# Veriyi (T, C, Z, Y, X) olarak al
data = img.get_image_data("TCZYX")

print("data.shape:", data.shape)

# Napari viewer
viewer = napari.Viewer()

# T boyutunu atarak sadece bir zaman dilimi kullan
data = data[0]  # shape: (C, Z, Y, X)
channel_names = ["C0 - Nucleus", "C1 - A11", "C2 - HA", "C3 - CCT1"]

# Her kanalı ayrı ayrı göster
for c in range(data.shape[0]):
    viewer.add_image(
        data[c],  # (Z, Y, X)
        name=channel_names[c] if c < len(channel_names) else f"Channel {c}"
    )


napari.run()

