from deep_learning.dataset import Dataset

if __name__ == '__main__':
  
  path_to_dataset = 'data_example'
  dataset = Dataset(path_to_dataset)

  path_to_video = "path/to/videos/"

  videos = [{"name": "Basilic_1.m4v", "label": "basil"},
            {"name": "Basilic_2.m4v", "label": "basil"},
            {"name": "Basilic_3.m4v", "label": "basil"},
            {"name": "Basilic_4.m4v", "label": "basil"},
            {"name": "Basilic_5.m4v", "label": "basil"},
            {"name": "Basilic_6.m4v", "label": "basil"},
            {"name": "Basilic_7.m4v", "label": "basil"},
            {"name": "Basilic_8.m4v", "label": "basil"},
            {"name": "Basilic_9.m4v", "label": "basil"},
            {"name": "Basilic_10.m4v", "label": "basil"},
            {"name": "Basilic_11.m4v", "label": "basil"},
            {"name": "Basilic_12.m4v", "label": "basil"},
            {"name": "Basilic_13.m4v", "label": "basil"},
            {"name": "Basilic_14.m4v", "label": "basil"},
            {"name": "Basilic_15.m4v", "label": "basil"},
            {"name": "Basilic_16.m4v", "label": "basil"},
            {"name": "Basilic_17.m4v", "label": "basil"},
            {"name": "Basilic_18.m4v", "label": "basil"},
            {"name": "Basilic_19.m4v", "label": "basil"},
            {"name": "Basilic_20.m4v", "label": "basil"},
            {"name": "Basilic_pourpre_1.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_2.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_3.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_4.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_5.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_6.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_7.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_8.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_9.m4v", "label": "purple basil"},
            {"name": "Basilic_pourpre_10.m4v", "label": "purple basil"},
            {"name": "Melisse_1.m4v", "label": "melissa"},
            {"name": "Melisse_2.m4v", "label": "melissa"},
            {"name": "Melisse_3.m4v", "label": "melissa"},
            {"name": "Melisse_4.m4v", "label": "melissa"},
            {"name": "Melisse_5.m4v", "label": "melissa"},
            {"name": "Melisse_6.m4v", "label": "melissa"},
            {"name": "Melisse_7.m4v", "label": "melissa"},
            {"name": "Melisse_8.m4v", "label": "melissa"},
            {"name": "Melisse_9.m4v", "label": "melissa"},
            {"name": "Melisse_10.m4v", "label": "melissa"},
            {"name": "Melisse_11.m4v", "label": "melissa"},
            {"name": "Melisse_12.m4v", "label": "melissa"},
            {"name": "Menthe_1.m4v", "label": "mint"},
            {"name": "Menthe_2.m4v", "label": "mint"},
            {"name": "Menthe_3.m4v", "label": "mint"},
            {"name": "Menthe_4.m4v", "label": "mint"},
            {"name": "Menthe_5.m4v", "label": "mint"},
            {"name": "Menthe_6.m4v", "label": "mint"},
            {"name": "Menthe_7.m4v", "label": "mint"},
            {"name": "Menthe_8.m4v", "label": "mint"}  
  ]
  for video in videos:
    dataset.add_video_to_dataset(video['label'], path_to_video + video['name'], 5)