# -*- coding: utf-8 -*-

class Detection:

  def label_image(self, path_image):
    """
      Detect the label of the given image

      :param path_images: Path to the image to detect the label
      :type path_images: string
        
      :return: The detected label
      :rtype: string
    """
    return 'label'

  def get_size_plant(self, path_image):
    """
      Get the size of the plants in the given image

      :param path_images: Path to the image to get the size
      :type path_images: string
        
      :return: The size
      :rtype: float
    """
    return 0

  def is_healthy(self, label, path_image):
    """
      Detect if the given plant is healthy or not

      :param path_images: Path to the image to analyse
      :type path_images: string

      :param label: label of the image to analyse
      :type label: string
        
      :return: The size
      :rtype: bool
    """
    return True
